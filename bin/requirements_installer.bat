@echo off
Title Requirements Installer
@echo Requirements Installer
@echo.
@echo Installing dependencies listed in requirements.txt
@echo.
@echo.
py -m pip install -r requirements.txt
@echo.
@echo.
pause
::TIMEOUT /T 10 /NOBREAK