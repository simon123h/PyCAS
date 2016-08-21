@echo off

:choice
echo.
choice /c npue /m '[N]ew commit, [P]ush now, [M]ore, [E]xit'
if %errorlevel%==1 goto :newCommit
if %errorlevel%==2 goto :push
if %errorlevel%==3 goto :more
if %errorlevel%==4 goto :exit


:more
choice /c npue /n /m '[N]ew commit, [P]ush now, [M]ore, [E]xit'
if %errorlevel%==1 goto :newCommit
if %errorlevel%==2 goto :push
if %errorlevel%==3 goto :more
if %errorlevel%==4 goto :exit


:newCommit
echo.
git add .
set /p msg="Commit message: "
git commit -m '%msg%'
goto choice


:push
git push
goto choice


:pull
git pull
goto choice


:exit
