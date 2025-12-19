@echo off
chcp 65001 >nul
echo ========================================
echo Git 推送助手
echo ========================================
echo.

set /p GITHUB_USER="请输入你的 GitHub 用户名: "
set /p REPO_NAME="请输入仓库名称 (例如: personal-resume): "

echo.
echo 正在初始化 Git 仓库...
if not exist .git (
    call git init
    echo ✅ Git 仓库已初始化
) else (
    echo ✅ Git 仓库已存在
)

echo.
echo 正在添加文件...
call git add .
echo ✅ 文件已添加

echo.
echo 正在提交...
call git commit -m "Initial commit: 个人简历网站"
echo ✅ 提交完成

echo.
echo 正在设置远程仓库...
call git remote remove origin 2>nul
call git remote add origin https://github.com/%GITHUB_USER%/%REPO_NAME%.git
echo ✅ 远程仓库已设置

echo.
echo 正在推送到 GitHub...
call git branch -M main
call git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo ✅ 代码已成功推送到 GitHub！
    echo ========================================
    echo.
    echo 仓库地址: https://github.com/%GITHUB_USER%/%REPO_NAME%
    echo.
    echo 下一步：
    echo 1. 访问 https://vercel.com
    echo 2. 使用 GitHub 账号登录
    echo 3. 点击 "Add New..." → "Project"
    echo 4. 选择仓库: %REPO_NAME%
    echo 5. 点击 "Deploy"
    echo.
) else (
    echo.
    echo ❌ 推送失败，请检查：
    echo 1. GitHub 仓库是否已创建
    echo 2. 仓库名称是否正确
    echo 3. 是否有推送权限
    echo.
)

pause

