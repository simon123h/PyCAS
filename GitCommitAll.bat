@echo off

:newCommit
git add .
set /p msg="Commit message: "
git commit -m '%msg%'


:choice
echo.
echo [P]ush now, [E]xit, [N]ew commit
choice /c pen /n
if %errorlevel%==1 goto :push
if %errorlevel%==2 exit
if %errorlevel%==3 goto :newCommit


:push
git push
goto choice
