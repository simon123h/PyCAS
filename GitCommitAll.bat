@echo off

:newCommit
git add .

set /p msg="Commit message: "
git commit -m '%msg%'

git push

echo Neuer Commit?
pause

goto newCommit