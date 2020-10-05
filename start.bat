@echo off

Title Jesvi Bot
color A

@echo.
@echo ---- System Status ----
@echo.

@echo Program   : Jesvi Bot

for /f "tokens=3" %%i in ('netsh wlan show interface ^| findstr /i "SSID"') do set "myssid=%%i" & goto next
:next
if "%myssid%"=="" @echo Connected : - 
if "%myssid%"=="" @echo. 
if "%myssid%"=="" @echo No Network ! 
if "%myssid%"=="" @echo.

if "%myssid%"=="" color c 
if "%myssid%"=="" pause 
if "%myssid%"=="" exit
@echo Connected : %myssid%

set totalMem=
set availableMem=
set usedMem=
for /f "tokens=4" %%a in ('systeminfo ^| findstr Physical') do if defined totalMem (set availableMem=%%a) else (set totalMem=%%a)
set totalMem=%totalMem:,=%
set availableMem=%availableMem:,=%
set /a usedMem=totalMem-availableMem
@echo Memory    : %usedMem%/%totalMem% 


@echo Date      : %DATE% 
@echo Time      : %TIME%

@echo.
@echo ----- Live Status -----
@echo.

ping 192.0.2.1 -n 1 -w 100 >nul
@echo -activated

cd %~dp0
start logger_bot.bat
start logger_sql.bat
main.py


@echo -ended
@echo.

pause