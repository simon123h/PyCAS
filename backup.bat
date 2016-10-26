@echo off
echo.

if exist backup.py (
	py backup.py -d .backup/ -t %%Y-%%m-%%d_%%H-%%M -excl [%~nx0]
) else (
	echo.
	py D:\Sourcecode\Python\backupProject\backup.py -d .backup/ -t %%Y-%%m-%%d_%%H-%%M -excl [%~nx0,FILE_TO_EXCLUDE]
)

echo.
pause