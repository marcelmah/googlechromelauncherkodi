(timeout /t 3 && tasklist /nh /fi "imagename eq Kodi.exe" | find /i "Kodi.exe" >nul && (taskkill /f /im Kodi.exe))&
cd "C:\Program Files (x86)\Google\Chrome\Application\"
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --incognito
"C:\Program Files (x86)\Kodi\Kodi.exe"