@echo off
chcp 65001 >nul
echo ========================================
echo 个人简历网站 - 完成部署
echo ========================================
echo.

echo ✅ 构建已成功！dist 文件夹已生成
echo.

echo 接下来需要完成以下步骤：
echo.
echo [步骤 1] 初始化 Git 仓库
echo [步骤 2] 创建 GitHub 仓库
echo [步骤 3] 推送代码到 GitHub
echo [步骤 4] 在 Vercel 部署
echo.

set /p CONTINUE="是否现在开始 Git 初始化？(Y/N): "
if /i not "%CONTINUE%"=="Y" (
    echo 已取消
    pause
    exit /b 0
)

echo.
echo [步骤 1] 初始化 Git 仓库...
if not exist .git (
    call git init
    echo ✅ Git 仓库已初始化
) else (
    echo ✅ Git 仓库已存在
)

echo.
echo [步骤 2] 添加文件到 Git...
call git add .
echo ✅ 文件已添加

echo.
echo [步骤 3] 提交代码...
call git commit -m "Initial commit: 个人简历网站"
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  提交失败，可能已经提交过了
) else (
    echo ✅ 代码已提交
)

echo.
echo ========================================
echo ✅ Git 初始化完成！
echo ========================================
echo.
echo 下一步操作：
echo.
echo 1. 访问 https://github.com
echo 2. 登录你的账号（如果没有账号，先注册）
echo 3. 点击右上角 "+" → "New repository"
echo 4. 填写信息：
echo    - Repository name: personal-resume（或你喜欢的名称）
echo    - 选择 Public（公开）
echo    - 不要勾选 "Initialize this repository with a README"
echo 5. 点击 "Create repository"
echo.
echo 创建完成后，运行 "Git推送助手.bat" 来推送代码
echo.
pause

