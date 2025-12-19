@echo off
chcp 65001 >nul
echo ====================================
echo   个人作品集网站 - 启动脚本
echo ====================================
echo.

REM 检查是否已安装依赖
if not exist "node_modules" (
    echo [1/2] 正在安装依赖，请稍候...
    call npm install
    if errorlevel 1 (
        echo.
        echo 依赖安装失败！请检查网络连接或 Node.js 是否已正确安装。
        pause
        exit /b 1
    )
    echo.
    echo [✓] 依赖安装完成！
    echo.
) else (
    echo [✓] 依赖已安装，跳过安装步骤
    echo.
)

echo [2/2] 正在启动开发服务器...
echo.
echo 网站将在浏览器中自动打开，地址通常是: http://localhost:5173
echo.
echo 按 Ctrl+C 可以停止服务器
echo ====================================
echo.

call npm run dev

pause





