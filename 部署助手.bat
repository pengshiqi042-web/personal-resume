@echo off
chcp 65001 >nul
echo ========================================
echo 个人简历网站 - 部署助手
echo ========================================
echo.

echo [步骤 1] 检查 Node.js 和 npm...
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 未找到 Node.js，请先安装 Node.js
    pause
    exit /b 1
)
where npm >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 未找到 npm，请先安装 npm
    pause
    exit /b 1
)
echo ✅ Node.js 和 npm 已安装
echo.

echo [步骤 2] 安装依赖...
call npm install
if %errorlevel% neq 0 (
    echo ❌ 依赖安装失败
    pause
    exit /b 1
)
echo ✅ 依赖安装完成
echo.

echo [步骤 3] 测试构建项目...
call npm run build
if %errorlevel% neq 0 (
    echo ❌ 构建失败，请检查错误信息
    pause
    exit /b 1
)
echo ✅ 构建成功！项目可以正常部署
echo.

echo ========================================
echo 构建完成！接下来请：
echo 1. 在 GitHub 创建新仓库
echo 2. 运行 git 命令推送代码
echo 3. 在 Vercel 部署
echo.
echo 详细步骤请查看：部署准备清单.md
echo ========================================
pause

