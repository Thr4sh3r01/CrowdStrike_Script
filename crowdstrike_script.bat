@echo off
setlocal

set "ruta_crowdstrike=C:\Windows\System32\drivers\CrowdStrike"
set "nombre_archivo=C-00000291*.sys"

for %%F in ("%ruta_crowdstrike%\%nombre_archivo%") do (
    echo Eliminando "%%~nxF"...
    del "%%~fF"
)

echo.
echo Archivos de CrowdStrike eliminados correctamente.
pause