#!/usr/bin/env python3

# Copyright (C) 2004-2024 Murilo Gomes Julio
# SPDX-License-Identifier: GPL-2.0-only

# Organização: Mestre da Info
# Site: https://linktr.ee/mestreinfo

import sys
import os
import webbrowser
import tkinter
import tkinter.messagebox
from subprocess import Popen,PIPE

def confirm():
    window = tkinter.Tk()
    window.wm_withdraw()
    message = tkinter.messagebox.askyesno(title="Requer MIApp", message="Para executar esse software você precisa do MIApp instalado, deseja baixar o MIApp agora?")

    if message:
        webbrowser.open_new('https://mestredainfo.wordpress.com/miapp/')


if os.path.isfile("/opt/miapp/miapp"):
    proc = Popen(["/opt/miapp/miapp", os.path.dirname(sys.executable)])
else:
    confirm()

sys.exit()