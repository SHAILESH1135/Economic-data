@echo off
set OUT_FILE="C:\SHAILESH\My work space\India economic data analysis\diagnostics.txt"
echo Fast diagnostics... > %OUT_FILE%
echo. >> %OUT_FILE%

echo [Node Version] >> %OUT_FILE%
call node -v >> %OUT_FILE% 2>&1
echo. >> %OUT_FILE%

echo [NPM Version] >> %OUT_FILE%
call npm -v >> %OUT_FILE% 2>&1
echo. >> %OUT_FILE%

echo [Vite Version] >> %OUT_FILE%
call npx vite -v >> %OUT_FILE% 2>&1
echo. >> %OUT_FILE%
