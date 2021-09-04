@echo off

Title SQL Debugger

:someRoutine
setlocal

%@Try%
  REM Normal code goes here
 
  @echo.
  @echo Setting up Mysql general Log feature..
  cd %~dp0
  cd ../../common/
  general_log_switch.py
  
  cd %~dp0
  @echo.
  @echo Logging SQL (logs/log_sql_runtime.log)
  @echo Press Ctrl + C to stop logging...
  @echo.
  powershell -Command "& {Get-Content ../../logs/log_sql_runtime_windows.log -wait}"
%@EndTry%
:@Catch
  REM Exception handling code goes here
  TIMEOUT /T 7 /NOBREAK
  exit
:@EndCatch

exit