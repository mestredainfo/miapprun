#!/usr/bin/env python3

# Copyright (C) 2004-2024 Murilo Gomes Julio
# SPDX-License-Identifier: GPL-2.0-only

# Organização: Mestre da Info
# Site: https://linktr.ee/mestreinfo

import sys
import os
import platform
from subprocess import Popen,PIPE

miSeparator = ""

if (platform.system() == "Linux"):
	miAppFile = "/opt/mestredainfo/miapp/miapp"
	miAppPath = miSeparator.join([os.path.dirname(sys.executable), "/app/"])
else:
	miAppFile = "C:\\\\mestredainfo\\\\miapp\\\\miapp.exe"
	miAppPath = miSeparator.join([os.path.dirname(sys.executable), "\\app\\"])

if os.path.isfile(miAppFile):
	if os.path.exists(miAppPath):
		miProc = Popen([miAppFile, os.path.dirname(sys.executable)])
	else:
		print("Pasta app não encontrada!")
else:
	print("MIApp não encontrado!")

sys.exit()
