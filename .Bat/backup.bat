cls
echo off
cls
REM -
REM - 100SECURITY
REM - 
REM - Criado por: Marcos Henrique
REM - Site: www.100security.com.br
REM -
REM - VARIAVEIS
set hora=%time:~0,2%hs%time:~3,2%min
set dia=%date:/=-%
set ORIGEM="E:\Teste"
set DESTINO="E:\Backup\BKP_%dia%_%hora%"
set LOG="E:\Backup Bat\backup\LOG"
set EMAIL=andrebmarcos@gmail.com
REM - ESTRUTURA

echo # - - - - - - - - - - - - - - - - - - - - - - - - - #
echo #                  Retenção                         #
echo # - - - - - - - - - - - - - - - - - - - - - - - - - #

REM -p "E:\Backup\" -s -d -1 -m * -c "cmd /c del /f /q @path"

echo # - - - - - - - - - - - - - - - - - - - - - - - - - #
echo #                  CRIANDO PASTA                    #
echo # - - - - - - - - - - - - - - - - - - - - - - - - - #

md %DESTINO%

echo # - - - - - - - - - - - - - - - - - - - - - - - - - #
echo #         COPIA DE ARQUIVOS E/OU DIRETORIOS         #
echo # - - - - - - - - - - - - - - - - - - - - - - - - - #
xcopy %ORIGEM% %DESTINO% /E /Y /C /H
REM /E - Copia diretórios e subdiretórios, inclusive os vazios.
REM /Y - Suprime o prompt para você confirmar se deseja substituir um arquivo de destino existente.
REM /C - Continua copiando, mesmo que ocorram erros.
REM /H - Copia arquivos ocultos e do sistema também.
echo # - - - - - - - - - - - - - - - - - - - - - - - - - #
echo # GERANDO LOG DE ARQUIVOS E/OU DIRETORIOS COPIADOS  #
echo # - - - - - - - - - - - - - - - - - - - - - - - - - #
dir /s %DESTINO% > "%LOG%\Arquivos.txt"
echo # - - - - - - - - - - - - - - - - - - - - - - - - - #
echo #          ENVIANDO E-MAIL COM LOG EM ANEXO         #
echo # - - - - - - - - - - - - - - - - - - - - - - - - - #
mailsend1.20b.exe -t andrebmarcos@gmail.com -f %EMAIL% -ssl -port 465 -auth -smtp smtp.gmail.com -sub Backup -M "Backup Realizado com Sucesso" -attach "C:\Teste\backup\Arquivos.txt" -user %EMAIL% -pass rnvwmcvndpwmkkgv
