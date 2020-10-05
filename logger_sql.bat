@echo off

:someRoutine
setlocal
%@Try%
  REM Normal code goes here
  Title SQL Debugger
  @echo Logging SQL (log_sql_runtime.log)
  @echo Press Ctrl + C to stop logging...
  @echo.
  powershell -Command "& {Get-Content log_sql_runtime.log -wait}"

%@EndTry%
:@Catch
  REM Exception handling code goes here
  exit
:@EndCatch