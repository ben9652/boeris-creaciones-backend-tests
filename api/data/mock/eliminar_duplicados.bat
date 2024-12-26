@echo off
setlocal enabledelayedexpansion

rem Verifica si se proporcionó un archivo como argumento
if "%~1"=="" (
    echo Uso: %~nx0 [archivo.txt]
    echo Ejemplo: %~nx0 input.txt
    exit /b
)

rem Archivo de entrada
set "archivo=%~1"

rem Verifica si el archivo existe
if not exist "%archivo%" (
    echo El archivo "%archivo%" no existe.
    exit /b
)

rem Archivo temporal para almacenar líneas únicas
set "temp=temp_sorted.txt"

rem Ordenar y eliminar duplicados
sort "%archivo%" > "%temp%"

rem Reemplazar el archivo original por el archivo sin duplicados
move /y "%temp%" "%archivo%" >nul

rem Confirmación de éxito
echo Las líneas duplicadas se han eliminado del archivo "%archivo%".
