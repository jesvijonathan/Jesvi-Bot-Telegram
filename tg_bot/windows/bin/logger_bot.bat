@echo OFF

Title Bot Debugger

:someRoutine
setlocal
%@Try%
  REM Normal code goes here
  cd %~dp0
  @echo Logging BOT (logs/log_bot_runtime.log)
  @echo Press Ctrl + C to stop logging...
  @echo.

  powershell -Command "& {Get-Content ../../logs/log_bot_runtime.log -wait}"
%@EndTry%
:@Catch
  REM Exception handling code goes here
  pause
  exit
:@EndCatch

exit