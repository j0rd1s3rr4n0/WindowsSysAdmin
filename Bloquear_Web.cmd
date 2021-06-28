@echo off
if  "%1"=="/?" (
echo.
echo Con este comando bloquearas el ingreso
echo a alguna pagina web especificada...
echo.
echo Sintaxis:
echo.
echo bloquear www.google.com [enter] = Web Bloqueada
exit/b
)
:ini1
set "opc="
set web=%1
echo 127.0.0.1 %web% >> "%windir%\System32\drivers\etc\hosts"
cls
echo Web Correctamente Bloqueada...
echo.
pause
cls
exit/b