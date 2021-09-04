@echo off

Title Restart MySQL Database

@echo off
if _%1_==_payload_  goto :payload

:getadmin
    echo Requesting Administrator Rights
    set vbs=%temp%\getadmin.vbs
    echo Set UAC = CreateObject^("Shell.Application"^)                >> "%vbs%"
    echo UAC.ShellExecute "%~s0", "payload %~sdp0 %*", "", "runas", 1 >> "%vbs%"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit
goto :eof

:payload

::--------------------------------------

@echo.
@echo Restarting MYSQL Database.. (~30sec)
@echo.

cd %~dp0
::py general_log_switch.py
@echo.

:: Change the below if the it does not work, also try "MySQL", "MySQL80", "mysql" 
net stop mysql
net start mysql


TIMEOUT /T 3 /NOBREAK
exit