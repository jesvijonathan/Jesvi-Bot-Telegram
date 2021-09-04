if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

@echo off

Title Jesvi Bot Auto Start
cd %~dp0

timeout 1 >nul

:inter
cls

MODE CON: COLS=39 LINES=25

@echo "         _______   _______          " 
@echo "    __  ___  __ \ / __  __ _____    "
@echo "   |_ \| __/' _| | |  \/__|_   _|   "
@echo "    _\ | _|`._`` | | ~| \/ || |     "
@echo "   /___|___|___/ | |__/\__/ |_|     "
@echo "         _______/ \_______          "
@echo "                                    "
@echo -------------Simple Mode--------------
@echo.

::for /l %%x in (1, 1, 100) do (
::   MODE CON: COLS=%%x LINES=22
::)

for /f "tokens=3" %%i in ('netsh wlan show interface ^| findstr /i "SSID"') do set "myssid=%%i" & goto next
:next
if "%myssid%"=="" @echo             No Internet ! 
if "%myssid%"=="" @echo.

if "%myssid%"=="" color c 
if "%myssid%"=="" timeout /t 7
if "%myssid%"=="" goto inter

@echo         Connected : %myssid%
color d

set totalMem=
set availableMem=
set usedMem=
for /f "tokens=4" %%a in ('systeminfo ^| findstr Physical') do if defined totalMem (set availableMem=%%a) else (set totalMem=%%a)
set totalMem=%totalMem:,=%
set availableMem=%availableMem:,=%
set /a usedMem=totalMem-availableMem
@echo         Memory    : %usedMem%/%totalMem% 

@echo         Started   : %TIME%


@echo.
@echo ------------ Live Status -------------
@echo.

:someRoutine
setlocal
%@Try%
  REM
  cd %~dp0
  cd ../../scripts/
  main.py
%@EndTry%
:@Catch
  REM
  exit
  exit
:@EndCatch

@echo -ended
@echo.
exit
exit