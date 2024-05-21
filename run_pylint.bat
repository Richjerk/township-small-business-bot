@echo off
setlocal enabledelayedexpansion
set files=
for /f "delims=" %%i in ('git ls-files *.py') do (
    set files=!files! %%i
)
pylint %files%
endlocal
