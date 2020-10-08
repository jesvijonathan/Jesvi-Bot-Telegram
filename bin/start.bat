@echo off

Title Jesvi Bot Status
cd %~dp0


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


@echo Started   : %DATE% (%TIME%)


@echo.
@echo ----- Live Status -----
@echo.

:someRoutine
setlocal
%@Try%
  REM Normal code goes here
  cd %~dp0
  ..\main.py
%@EndTry%
:@Catch
  REM Exception handling code goes here
  exit
  exit
:@EndCatch

@echo -ended
@echo.
exit
exit