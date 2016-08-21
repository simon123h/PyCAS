@echo off

:legend
echo [N]ew commit
echo [P]ush now
echo [M]ore
goto choice


:more
echo [U]pdate from server
echo [E]xit
goto choice


:choice
choice /c npmue /n /m ">>> "
if %errorlevel%==1 goto :newCommit
if %errorlevel%==2 goto :push
if %errorlevel%==3 goto :more
if %errorlevel%==4 goto :pull
if %errorlevel%==5 goto :exit


:startOver
echo.
echo.
goto legend



:newCommit
echo.
git add .
set /p msg="Commit message: "
git commit -m '%msg%'
goto startOver


:push
echo.
git push
goto startOver


:pull
echo.
git pull
goto startOver


:fastCommitPush


:exit
