@echo OFF

Title Requirements Installer
cd %~dp0
@echo Requirements Installer

@echo.
@echo.
@echo Installing dependencies listed on requirements.txt
@echo.
py -m pip install --upgrade pip
py -m pip install Twisted
py -m pip install wheel
@echo.
py -m pip install -r ../../../requirements.txt
@echo.

TIMEOUT /T 14 /NOBREAK
sleep 5
exit
