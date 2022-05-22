@echo off

Title Jesvi Bot Setup

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

echo Downloading Latest Jesvi Bot package
cd c:\
::dir
Remove-item alias:curl
curl -L -O https://github.com/jesvijonathan/Jesvi-Bot-Telegram/releases/download/v2.1/Jesvi-Bot-Telegram.zip
::mkdir C:\Jesvi-Bot-Telegram

echo.
echo.
echo Winget Package is *MUST* For installing required softwares, You will now be redirected to microsoft store.
echo Click on install and press ENTER after the installation is over to continue with setup..
SET /P AREYOUSURE=Press "y" to continue. (Y/[N]) 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO pytt
start /W ms-windows-store://pdp/?productid=9nblggh4nns1
pause
:pytt
echo Skipping Winget Installation..
echo Skip only if already installed ! else it will break most part of the script during the installation !

 
echo.
setlocal
:PROMPT
SET /P AREYOUSURE=Do you want to install 7zip ? Skip (n) if already installed.  (Y/[N])
IF /I "%AREYOUSURE%" NEQ "Y" GOTO pyt
echo Installing 7zip
echo Required for unparsing package, can skip if already installed.. 
winget install 7zip.7zip
:pyt
echo Skipping 7zip installation

::robocopy C:\Intel\a C:\ /e

echo.
echo Extracting Zip 
"C:\Program Files\7-Zip\7z.exe" x C:\Jesvi-Bot-Telegram.zip -oc:\Jesvi-Bot-Telegram -aoa -y -r

echo Deleting Zip
del c:\Jesvi-Bot-Telegram.zip

echo Opening Resource Folder
start /min explorer c:\Jesvi-Bot-Telegram

::7z e C:\abc\abc.zip -y oC:\abc

::"C:\Program Files\7-Zip\7z.exe" e C:\Jesvi-Bot-Telegram.zip

::"C:\Program Files\7-Zip\7z.exe" e -oc:\Jesvi-Bot-Telegram *.zip


echo Creating Shortcut
start /B CMD /C CALL C:\Jesvi-Bot-Telegram\tg_bot\windows\bin\shortcut_create_2.bat >NUL 2>&1
start /B CMD /C CALL C:\Jesvi-Bot-Telegram\tg_bot\windows\bin\auto_start_sc_2.bat >NUL 2>&1

 
echo.
setlocal
:PROMPT
SET /P AREYOUSURE=Do you want to install Python 3 ? (Y/[N])
IF /I "%AREYOUSURE%" NEQ "Y" GOTO pyt
echo Installing python
echo Tested on python 3.8 and greater (v3.10 recommended.)
winget install python3
:pyt
echo Skipping python installation

 
echo.
setlocal
:PROMPT
SET /P AREYOUSURE=Do you want to install MySQL ? (Y/[N])
IF /I "%AREYOUSURE%" NEQ "Y" GOTO pyt
echo Installing MySQL
echo Open mysql installer from start and Select developer bundle along with default parameters...
echo Create a user and a password when asked in mysql installer with full privilege/access given to the user.
echo Remember this, as you will have to add this to the config file later...
winget install Oracle.MySQL
:pyt
echo Skipping mysql installation

 
echo.
echo Installing requirements
start /W C:\Jesvi-Bot-Telegram\tg_bot\windows\bin\requirements_installer.bat


echo Opening Config File
start notepad C:\Jesvi-Bot-Telegram\tg_bot\scripts\config.py


echo Starting bot utlity
start "C:\Jesvi-Bot-Telegram\tg_bot\windows\bin" "Jesvi Bot.exe"


echo Installer Quiting in 15 seconds..
timeout /t 15