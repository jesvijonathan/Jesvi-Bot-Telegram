@echo off
cls
@echo Logging (bot_runtime.log)
@echo Press Ctrl + C to stop logging...
@echo.
powershell -Command "& {Get-Content bot_runtime.log -wait}"
pause