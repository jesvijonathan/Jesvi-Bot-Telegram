@echo off

Title Auto Start Set

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

cd ../

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Jesvi Bot.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%

echo oLink.TargetPath = ("%cd%\Jesvi-Bot\Jesvi Bot.exe")>> %SCRIPT%

echo oLink.Description = "Jesvi Bot By Jesvi Jonathan" >> %SCRIPT%
echo oLink.IconLocation = ("%~dp0icon.ico") >> %SCRIPT%
echo oLink.WorkingDirectory = "%cd%\Jesvi-Bot\" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%


set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\Jesvi Bot.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%

echo oLink.TargetPath = ("%cd%\Jesvi-Bot\Jesvi Bot.exe")>> %SCRIPT%

echo oLink.Description = "Jesvi Bot By Jesvi Jonathan" >> %SCRIPT%
echo oLink.IconLocation = ("%~dp0icon.ico") >> %SCRIPT%
echo oLink.WorkingDirectory = "%cd%\Jesvi-Bot\" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%


exit