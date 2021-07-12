@echo off
Title Requirements Generator

@echo Powered by pigar
@echo.
@echo Started Requirements.bat
@echo.
@echo Installing pigar..
@echo.
@echo.
py -m pip install pigar
@echo.
@echo.
@echo Creating list..
@echo.
py -m pigar
@echo.
@echo Done listing dependencies to "requirements.txt"
start notepad "requirements.txt"
::pause
TIMEOUT /T 7 /NOBREAK