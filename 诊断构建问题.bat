@echo off
chcp 65001 >nul
echo ========================================
echo 构建问题诊断工具
echo ========================================
echo.

echo [1] 检查 Node.js 版本...
node --version
if %errorlevel% neq 0 (
    echo ❌ Node.js 未安装或不在 PATH 中
    pause
    exit /b 1
)
echo ✅ Node.js 已安装
echo.

echo [2] 检查 npm 版本...
npm --version
if %errorlevel% neq 0 (
    echo ❌ npm 未安装或不在 PATH 中
    pause
    exit /b 1
)
echo ✅ npm 已安装
echo.

echo [3] 检查 node_modules 是否存在...
if not exist node_modules (
    echo ⚠️  node_modules 不存在，正在安装依赖...
    call npm install
    if %errorlevel% neq 0 (
        echo ❌ 依赖安装失败
        pause
        exit /b 1
    )
) else (
    echo ✅ node_modules 存在
)
echo.

echo [4] 检查关键文件...
if not exist package.json (
    echo ❌ package.json 不存在
    pause
    exit /b 1
)
if not exist vite.config.js (
    echo ❌ vite.config.js 不存在
    pause
    exit /b 1
)
if not exist index.html (
    echo ❌ index.html 不存在
    pause
    exit /b 1
)
if not exist src\main.jsx (
    echo ❌ src\main.jsx 不存在
    pause
    exit /b 1
)
echo ✅ 关键文件都存在
echo.

echo [5] 尝试构建项目（显示详细错误）...
echo.
call npm run build 2>&1
set BUILD_RESULT=%errorlevel%

echo.
echo ========================================
if %BUILD_RESULT% equ 0 (
    echo ✅ 构建成功！
    echo.
    echo 构建文件在 dist 文件夹中
) else (
    echo ❌ 构建失败
    echo.
    echo 请查看上面的错误信息
    echo.
    echo 常见问题：
    echo 1. 检查是否有语法错误
    echo 2. 检查导入路径是否正确
    echo 3. 尝试删除 node_modules 和重新安装：
    echo    rmdir /s /q node_modules
    echo    npm install
)
echo ========================================
pause

