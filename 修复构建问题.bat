@echo off
chcp 65001 >nul
echo ========================================
echo 构建问题修复工具
echo ========================================
echo.

echo [步骤 1] 清理旧的构建文件...
if exist dist (
    rmdir /s /q dist
    echo ✅ 已删除 dist 文件夹
)
if exist node_modules\.vite (
    rmdir /s /q node_modules\.vite
    echo ✅ 已清理 Vite 缓存
)
echo.

echo [步骤 2] 检查并重新安装依赖...
if exist node_modules (
    echo 正在删除 node_modules...
    rmdir /s /q node_modules
)
if exist package-lock.json (
    del /f /q package-lock.json
    echo ✅ 已删除 package-lock.json
)
echo.

echo [步骤 3] 重新安装依赖（这可能需要几分钟）...
call npm install
if %errorlevel% neq 0 (
    echo.
    echo ❌ 依赖安装失败
    echo.
    echo 尝试使用国内镜像...
    call npm install --registry=https://registry.npmmirror.com
    if %errorlevel% neq 0 (
        echo ❌ 使用镜像安装也失败，请检查网络连接
        pause
        exit /b 1
    )
)
echo ✅ 依赖安装完成
echo.

echo [步骤 4] 尝试构建项目...
echo.
call npm run build
set BUILD_RESULT=%errorlevel%

echo.
echo ========================================
if %BUILD_RESULT% equ 0 (
    echo ✅✅✅ 构建成功！✅✅✅
    echo.
    echo 构建文件已生成在 dist 文件夹中
    echo 现在可以继续部署步骤了
) else (
    echo ❌ 构建仍然失败
    echo.
    echo 请查看上面的错误信息，常见问题：
    echo.
    echo 1. 语法错误：
    echo    - 检查所有 .jsx 和 .js 文件是否有语法错误
    echo    - 检查是否有未闭合的括号、引号等
    echo.
    echo 2. 导入路径错误：
    echo    - 检查所有 import 语句的路径是否正确
    echo    - 确保文件扩展名正确（.jsx 或 .js）
    echo.
    echo 3. 缺失文件：
    echo    - 检查所有导入的文件是否存在
    echo    - 检查图片文件是否在 public 文件夹中
    echo.
    echo 4. 依赖问题：
    echo    - 尝试手动运行: npm install
    echo    - 检查 package.json 是否正确
    echo.
    echo 如果问题仍然存在，请将完整的错误信息发给我
)
echo ========================================
pause

