@echo off

Title Auto Start Set

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

cd ../

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Jesvi Bot.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%

echo oLink.TargetPath = ("%cd%\bin\auto_start.bat")>> %SCRIPT%

echo oLink.Description = "Jesvi Bot By Jesvi Jonathan" >> %SCRIPT%
echo oLink.IconLocation = ("%~dp0icon.ico") >> %SCRIPT%
echo oLink.WorkingDirectory = "%cd%\bin" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%

exit