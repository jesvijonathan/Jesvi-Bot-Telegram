@echo off

Title Auto Start Set

cd ../

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\Jesvi Bot.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%

echo oLink.TargetPath = ("%cd%\bin\Jesvi Bot.exe")>> %SCRIPT%

echo oLink.Description = "Jesvi Bot By Jesvi Jonathan" >> %SCRIPT%
echo oLink.IconLocation = ("%~dp0icon.ico") >> %SCRIPT%
echo oLink.WorkingDirectory = "%cd%\bin" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%


::run as admin to create start shortcut

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Jesvi Bot.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%

echo oLink.TargetPath = ("%cd%\bin\Jesvi Bot.exe")>> %SCRIPT%

echo oLink.Description = "Jesvi Bot By Jesvi Jonathan" >> %SCRIPT%
echo oLink.IconLocation = ("%~dp0icon.ico") >> %SCRIPT%
echo oLink.WorkingDirectory = "%cd%\bin" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%


exit