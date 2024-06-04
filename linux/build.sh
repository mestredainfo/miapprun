#!/bin/bash

# Copyright (C) 2004-2024 Murilo Gomes Julio
# SPDX-License-Identifier: GPL-2.0-only

# Organização: Mestre da Info
# Site: https://linktr.ee/mestreinfo

while true; do
	echo ""
	echo "-------------------------------- CreateExecutable --------------------------------"
    echo "Selecione uma opção:"
    echo '1. Preparar o Ambiente'
    echo '2. Compilar o MIApp'
    echo "3. Sair"
    echo "-------------------------------- /CreateExecutable --------------------------------"
	echo ""
	
    read -p "Opção: " option

    case $option in
    	1)
    	    echo "Criando diretório mivenv..."
			python3 -m venv mivenv/

			echo "Instalando o pyinstaller..."
			mivenv/bin/pip install pyinstaller

			echo "Concluido!"
			;;
		2)
			echo "Compilando miapp.py..."
			
			mivenv/bin/pyinstaller -F miapp.py
			
			echo "Concluido!"
			;;
        3)
            echo "Saindo..."
            exit 0
            ;;
        *)
            echo "Opção inválida. Por favor, escolha uma opção válida."
            ;;
    esac
done
