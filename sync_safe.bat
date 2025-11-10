@echo off
REM ===== Safe Git sync for Windows =====

echo ===============================================
echo Sync to GitHub
echo ===============================================

REM 1) Check Git
git --version >NUL 2>&1
if errorlevel 1 (
  echo Git not found. Install from https://git-scm.com/
  exit /b 1
)

REM 2) Check repo
git rev-parse --is-inside-work-tree >NUL 2>&1
if errorlevel 1 (
  echo Not a git repository here.
  exit /b 1
)

REM 3) Any changes?
for /f %%i in ('git status --porcelain ^| find /c /v ""') do set CHANGES=%%i
if "%CHANGES%"=="0" goto push

REM 4) Stage and commit
git add -A
set "MSG=%*"
if "%~1"=="" set "MSG=Auto-update %date% %time%"

REM Strip surrounding quotes if present
if "%MSG:~0,1%"=="\"" if "%MSG:~-1%"=="\"" set "MSG=%MSG:~1,-1%"

REM Escape special chars
set "MSG=%MSG:^=^^%"
set "MSG=%MSG:&=^&%"
set "MSG=%MSG:|=^|%"
set "MSG=%MSG:<=^<%"
set "MSG=%MSG:>=^>%"
set "MSG=%MSG:"=\"%"

git commit -m "%MSG%"
if errorlevel 1 exit /b 1

:push
REM 5) Push (first time or normal)
git rev-parse --abbrev-ref --symbolic-full-name @{u} >NUL 2>&1
if errorlevel 1 (
  for /f %%b in ('git rev-parse --abbrev-ref HEAD') do set "BRANCH=%%b"
  if "%BRANCH%"=="" set "BRANCH=main"
  git push -u origin %BRANCH%
) else (
  git push
)

if errorlevel 1 exit /b 1

echo Done
exit /b 0
