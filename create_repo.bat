@echo off
echo Creating GitHub Repository for Flood Management System...
echo.

REM Create repository using GitHub API
powershell -Command "Invoke-RestMethod -Uri 'https://api.github.com/user/repos' -Method POST -Headers @{'Authorization'='token YOUR_GITHUB_TOKEN';'Accept'='application/vnd.github.v3+json'} -Body '{\"name\":\"flood_is_coming\",\"description\":\"Flood Management System for Mumbai\",\"public\":true}'"

echo.
echo Repository created! Now pushing code...
echo.

REM Add remote and push
git remote add origin https://github.com/Akashkeote/flood_is_coming.git
git push -u origin main

echo.
echo Done! Your app will be available at: https://akashkeote.github.io/flood_is_coming/
pause 