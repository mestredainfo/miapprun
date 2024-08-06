#!/bin/bash

# Copyright (C) 2004-2024 Murilo Gomes Julio
# SPDX-License-Identifier: GPL-2.0-only

# Organização: Mestre da Info
# Site: https://linktr.ee/mestreinfo

while true; do
	echo ""
	echo "-------------------------------- CreateExecutable --------------------------------"
    echo "Selecione uma opção:"
    echo '1. Preparar o Ambiente (Linux)'
    echo '2. Preparar o Ambiente (Windows)'
    echo '3. Compilar o MIAppRun (Linux)'
    echo '4. Compilar o MIAppRun (Windows)'
    echo "5. Sair"
    echo "-------------------------------- /CreateExecutable --------------------------------"
	echo ""
	
    read -p "Opção: " option

    case $option in
    	1)
            echo "Preparando o ambiente para Linux..."
            rm -rf linux/
            mkdir -p linux/
            cd linux/

    	    echo "Criando diretório mivenv..."
			python3 -m venv mivenv/

			echo "Instalando o pyinstaller..."
			mivenv/bin/pip install pyinstaller
            
            cd ../

			echo "Concluido!"
			;;
        2)
            echo "Preparando o ambiente para Windows..."
            rm -rf win32/
            mkdir -p win32/
            cd win32/

            miDir=$(pwd)

			echo "Criando diretório build/tmp/..."
			mkdir -p build/tmp/
			
    		echo "Baixando o Python-3.11.2..."
			wget -O build/tmp/python-3.11.2.exe https://www.python.org/ftp/python/3.11.2/python-3.11.2.exe

			echo "Configurar para Windows 10..."
			WINEPREFIX="$miDir/build/.wine/" winecfg

			echo "Instalando o Python3... (Remover tudo, deixar só o pip ativado e alterar a localização para C:\Python3\)"
			WINEPREFIX="$miDir/build/.wine/" wine build/tmp/python-3.11.2.exe

			echo "Instalando o PyInstaller..."
			WINEPREFIX="$miDir/build/.wine/" wine build/.wine/drive_c/Python3/python.exe build/.wine/drive_c/Python3/Scripts/pip.exe install pyinstaller
			
            cd ../

			echo "Concluido!"
			;;
	    3)
			echo "Compilando 'miapprun.py' para Linux..."
			
            rm -f linux/miapprun.py
            rm -f linux/miapprun.spec
            rm -rf linux/dist/

            cp miapprun.py linux/miapprun.py

            cd linux/

			mivenv/bin/pyinstaller -F miapprun.py

            cd ../
			
			echo "Concluido!"
			;;
        4)
            echo "Compilando 'miapprun.py' para Windows..."
			
            rm -f win32/miapprun.py
            rm -f win32/miapprun.spec
            rm -rf win32/dist/

            cp miapprun.py win32/miapprun.py

            cd win32/
            
			miDir=$(pwd)
			WINEPREFIX="$miDir/build/.wine/" wine build/.wine/drive_c/Python3/Scripts/pyinstaller.exe --onefile miapprun.py
			
            cd ../

			echo "Concluido!"
			;;
        5)
            echo "Saindo..."
            exit 0
            ;;
        *)
            echo "Opção inválida. Por favor, escolha uma opção válida."
            ;;
    esac
done
