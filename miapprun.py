#!/usr/bin/env python3

# Copyright (C) 2004-2024 Murilo Gomes Julio
# SPDX-License-Identifier: GPL-2.0-only

# Organização: Mestre da Info
# Site: https://linktr.ee/mestreinfo

import sys
import os
import platform
from subprocess import Popen,PIPE

if (platform.system() == "Linux"):
    miAppFile = "/opt/miapp/miapp"
else:
	miAppFile = "C:\\\\miapp\\\\miapp.exe"

if os.path.isfile(miAppFile):
    miProc = Popen([miAppFile, os.path.dirname(sys.executable)])

sys.exit()
