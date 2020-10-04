@echo off
cls
@echo Logging (log_bot_runtime.log)
@echo Press Ctrl + C to stop logging...
@echo.
powershell -Command "& {Get-Content log_bot_runtime.log -wait}"
pause