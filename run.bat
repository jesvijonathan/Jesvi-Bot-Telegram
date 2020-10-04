@echo off

color A

@echo.
@echo ---- System Status ----
@echo.

cd C:\Users\jesvi\PycharmProjects\Auto Aroma Py\venv\Scripts
call activate.bat

@echo Program   : Jesvi Bot

for /f "tokens=3" %%i in ('netsh wlan show interface ^| findstr /i "SSID"') do set "myssid=%%i" & goto next
:next
if "%myssid%"=="" @echo Connected : - | @echo. | @echo No Network ! | @echo. | pause | exit
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

@echo -activated

cd C:\Users\jesvi\Documents\GitHub\Jesvi-Bot
main.py

@echo -ended
@echo.

pause