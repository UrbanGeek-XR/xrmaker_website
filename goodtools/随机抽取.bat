@echo off
setlocal enabledelayedexpansion
chcp 936 >nul
cls

:MENU
cls
echo.
echo ==============================
echo        随机抽取工具（循环版）
echo ==============================
echo  1 = 仅抽取【文件】
echo  2 = 抽取【文件+文件夹】
echo  3 = 退出程序
echo ==============================
echo.

set "c="
set /p "c=请输入选项(1/2/3)："

:: 退出
if "%c%"=="3" (
    echo 再见！
    exit
)

:: 初始化计数
set cnt=0

:: 选项1：只抽文件
if "%c%"=="1" (
    echo.
    echo [模式] 仅抽取文件
    for %%f in (*) do (
        if not "%%~nf"=="随机抽取" (
            set /a cnt+=1
            set "item!cnt!=%%f"
        )
    )
)

:: 选项2：文件+文件夹
if "%c%"=="2" (
    echo.
    echo [模式] 抽取文件+文件夹
    for /f "delims=" %%f in ('dir /b') do (
        if not "%%~nf"=="随机抽取" (
            set /a cnt+=1
            set "item!cnt!=%%f"
        )
    )
)

:: 无内容
if !cnt! equ 0 (
    echo.
    echo 没有可抽取的内容！
    pause >nul
    goto MENU
)

:: 随机抽取
set /a r=!random! %% !cnt! + 1
echo.
echo ======================================
echo              抽取结果
echo ======================================
echo.
echo  随机选中：!item%r%!
echo  总数量：!cnt! 个
echo.
echo ======================================
echo.
pause >nul

:: 返回菜单（循环）
goto MENU