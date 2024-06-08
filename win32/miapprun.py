#!/usr/bin/env python3

# Copyright (C) 2004-2024 Murilo Gomes Julio
# SPDX-License-Identifier: GPL-2.0-only

# Organização: Mestre da Info
# Site: https://linktr.ee/mestreinfo

import sys
import os
import webbrowser
import tkinter.messagebox
from subprocess import Popen,PIPE

def miConfirm():
    miMessage = tkinter.messagebox.askyesno(title="Requer MIApp", message="Para executar esse software você precisa do MIApp instalado, deseja baixar o MIApp agora?")

    if miMessage:
        webbrowser.open_new('https://mestredainfo.wordpress.com/miapp/')

if os.path.isfile("C:\\\\miapp\\\\miapp.exe"):
    miProc = Popen(["C:\\\\miapp\\\\miapp.exe", os.path.dirname(sys.executable)])
else:
    miConfirm()

sys.exit()