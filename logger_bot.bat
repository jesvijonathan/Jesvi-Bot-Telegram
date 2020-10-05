@echo off
Title Bot Debugger
:someRoutine
setlocal
%@Try%
  REM Normal code goes here
  @echo Logging BOT (log_bot_runtime.log)
  @echo Press Ctrl + C to stop logging...
  @echo.

  powershell -Command "& {Get-Content log_bot_runtime.log -wait}"
%@EndTry%
:@Catch
  REM Exception handling code goes here
  exit
:@EndCatch