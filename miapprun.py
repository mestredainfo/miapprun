#!/usr/bin/env python3

# Copyright (C) 2004-2024 Murilo Gomes Julio
# SPDX-License-Identifier: GPL-2.0-only

# Organização: Mestre da Info
# Site: https://linktr.ee/mestreinfo

import sys
import os
import webbrowser
import platform
import locale
from subprocess import Popen,PIPE

milang, _ = locale.getlocale()
milangpt = milang.split('_')[0]
    
def miConfirm():    
    if milangpt == "pt":    
    	sys.stdout.write("\nO MIApp não foi encontrado!\n\nO " + os.path.basename(sys.executable) + " requer o MIApp instalado, deseja baixar agora? [s/n]")
    else:
    	sys.stdout.write("\nMIApp was not found!\n\n" + os.path.basename(sys.executable) + " requires MIApp installed, want to download now? [y/n]")
    	
    miChoice = input().lower()
    if miChoice == 'y' or miChoice == 's':
        webbrowser.open_new('https://mestredainfo.wordpress.com/miapp/')

miAppFile = "/opt/miapp/miapp"
if (platform.system() == "Windows"):
    miAppFile = "C:\\\\miapp\\\\miapp.exe"

if os.path.isfile(miAppFile):
    miProc = Popen([miAppFile, os.path.dirname(sys.executable)])
else:
    miConfirm()

sys.exit()
