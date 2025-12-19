@echo off
chcp 65001 >nul
echo ====================================
echo   个人作品集网站 - 快速安装
echo ====================================
echo.
echo 正在安装项目依赖，这可能需要几分钟...
echo.

call npm install

if errorlevel 1 (
    echo.
    echo 安装失败！可能的原因：
    echo 1. 未安装 Node.js - 请访问 https://nodejs.org/ 下载安装
    echo 2. 网络连接问题 - 请检查网络或使用国内镜像
    echo.
    echo 使用国内镜像安装（如果上面失败，可以尝试）：
    echo npm install --registry=https://registry.npmmirror.com
    echo.
    pause
    exit /b 1
) else (
    echo.
    echo ====================================
    echo [✓] 安装成功！
    echo ====================================
    echo.
    echo 下一步：运行 "启动.bat" 来启动网站
    echo 或者运行命令: npm run dev
    echo.
)

pause

