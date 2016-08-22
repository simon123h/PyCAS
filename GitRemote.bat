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
echo  [E]xit
goto choice


:choice
choice /c cpmueisdrbkl /n /m "> "
if %errorlevel%==1 goto :newCommit
if %errorlevel%==2 goto :push
if %errorlevel%==3 goto :more
if %errorlevel%==4 goto :pull
if %errorlevel%==5 goto :exit
if %errorlevel%==6 goto :init
if %errorlevel%==7 echo. & git status & goto startOver
if %errorlevel%==8 echo. & git diff & goto startOver
if %errorlevel%==9 goto :recommit
if %errorlevel%==10 goto :branching
if %errorlevel%==11 gitk & goto startOver
if %errorlevel%==12 echo. & git log & goto startOver


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
git push origin master
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
echo  [R]eturn

choice /c rlnsd /n /m "> "
if %errorlevel%==1 goto :startOver
if %errorlevel%==2 goto :listBranches
if %errorlevel%==3 goto :newBranch
if %errorlevel%==4 goto :switchBranch
if %errorlevel%==5 goto :deleteBranch

:listBranches
echo .
git branch -av
goto startOver

:newBranch
echo .
set /p name="Branch name: "
git checkout -b %name%
goto startOver

:switchBranch
echo .
set /p name="Branch name: "
git checkout %name%
goto startOver

:deleteBranch
echo .
set /p name="Branch name: "
git branch -d %name%
goto startOver



:exit
