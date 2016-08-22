@echo off

echo  ------------------------
echo         Git Remote       
echo  ------------------------
echo.


:legend
echo  [C]ommit now
echo  [P]ush now
echo  [M]ore
goto choice


:more
echo  [U]pdate from server
echo  [D]iff
echo  [S]tatus
echo  [L]og
echo  Git[K]
echo  [R]ecommit
echo  [I]nit new repo
echo  [B]ranching
goto choice


:choice
choice /c cpmuisdrbkl /n /m "> "
if %errorlevel%==1 goto :newCommit
if %errorlevel%==2 goto :push
if %errorlevel%==3 goto :more
if %errorlevel%==4 goto :pull
if %errorlevel%==5 goto :init
if %errorlevel%==6 echo. & git status & goto startOver
if %errorlevel%==7 echo. & git diff & goto startOver
if %errorlevel%==8 goto :recommit
if %errorlevel%==9 goto :branching
if %errorlevel%==10 gitk & goto startOver
if %errorlevel%==11 echo. & git log & goto startOver


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

:recommit
echo.
git add .
set /p msg="Commit message: "
git commit -m '%msg%' --amend
goto startOver


:push
echo.
REM git push origin master
git push
goto startOver


:pull
echo.
git pull
goto startOver


:init
echo.
git init
set /p url="Remote server url: "
if not "%url%" == "" git remote add origin %url%
goto startOver





:branching
echo.
echo Branching
echo  [N]ew branch
echo  [L]ist all
echo  [S]witch to branch
echo  [D]elete branch
echo  [M]erge
echo  [R]eturn

choice /c rlnsdm /n /m "> "
if %errorlevel%==1 goto :startOver
if %errorlevel%==2 goto :listBranches
if %errorlevel%==3 goto :newBranch
if %errorlevel%==4 goto :switchBranch
if %errorlevel%==5 goto :deleteBranch
if %errorlevel%==6 goto :mergeBranch

:listBranches
echo .
git branch -av
goto startOver

:newBranch
echo .
set /p name="Create branch named: "
git checkout -b %name%
git push -u origin %name%
goto startOver

:switchBranch
echo .
set /p name="Switch to branch named: "
git checkout %name%
git push -u origin %name%
goto startOver

:deleteBranch
echo .
set /p name="Delete branch named: "
git branch -d %name%
goto startOver

:mergeBranch
echo .
set /p name="Merge with branch named: "
git merge %name%
goto startOver



