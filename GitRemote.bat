@echo off

echo  -----------------------
echo        Git Remote
echo  -----------------------
echo.


:legend
echo  [C]ommit now
echo  [P]ush now
echo  [M]ore
goto choice


:more
echo  [R]ecommit
echo  [U]pdate from server
echo  [S]tatus
echo  [D]iff
echo  [I]nit new repo
echo  [E]xit
goto choice


:choice
choice /c cpmueisdr /n /m "> "
if %errorlevel%==1 goto :newCommit
if %errorlevel%==2 goto :push
if %errorlevel%==3 goto :more
if %errorlevel%==4 goto :pull
if %errorlevel%==5 goto :exit
if %errorlevel%==6 goto :init
if %errorlevel%==7 goto :status
if %errorlevel%==8 goto :diff
if %errorlevel%==8 goto :recommit


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

:newCommit
echo.
git add .
set /p msg="Commit message: "
git commit -m '%msg%' --amend
goto startOver


:push
echo.
git push
goto startOver


:pull
echo.
git pull
goto startOver

:asfasa


:init
echo.
git init
set /p url="Clone URL: "
if not "%url%" == "" git clone %url%
goto startOver


:status
echo.
git status
goto startOver


:diff
echo.
git diff
goto startOver



:exit
