@echo off
REM ===== Safe Git sync for Windows (no delayed expansion) =====

echo ===============================================
echo Sync to GitHub...
echo ===============================================

REM 1) Check Git
git --version >NUL 2>&1
if errorlevel 1 (
  echo Git not found. Install from https://git-scm.com/
  goto end
)

REM 2) Check repo
git rev-parse --is-inside-work-tree >NUL 2>&1
if errorlevel 1 (
  echo Not a git repository here.
  goto end
)

REM 3) Any changes?
for /f %%i in ('git status --porcelain ^| find /c /v ""') do set CHANGES=%%i
if "%CHANGES%"=="0" (
  echo No changes to commit.
  goto push
)

REM 4) Stage
git add -A

REM 5) Commit message (no quotes required)
set "MSG=%*"
if "%~1"=="" set "MSG=Auto-update %date% %time%"

REM Strip surrounding quotes if user pasted them
if "%MSG:~0,1%"=="\"" if "%MSG:~-1%"=="\"" set "MSG=%MSG:~1,-1%"

REM Escape special CMD chars
set "MSG=%MSG:^=^^%"
set "MSG=%MSG:&=^&%"
set "MSG=%MSG:|=^|%"
set "MSG=%MSG:<=^<%"
set "MSG=%MSG:>=^>%"
set "MSG=%MSG:"=\"%"

git commit -m "%MSG%"
if errorlevel 1 (
  echo Commit failed.
  goto end
)

:push
REM 6) Push (first time or normal)
git rev-parse --abbrev-ref --symbolic-full-name @{u} >NUL 2>&1
if errorlevel 1 (
  for /f %%b in ('git rev-parse --abbrev-ref HEAD') do set "BRANCH=%%b"
  if "%BRANCH%"=="" set "BRANCH=main"
  echo First push to origin %BRANCH%
  git push -u origin %BRANCH%
) else (
  git push
)

if errorlevel 1 (
  echo Push failed (network/auth).
  goto end
)

echo Done.
:end
REM Avoid PowerShell oddities; comment next line if you don't want pause
pause
exit /b 0
