#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc
import os
import xbmcaddon
import subprocess

addon = xbmcaddon.Addon()
script_path = addon.getAddonInfo('path')
script_file = 'gclauncher.bat'
script = os.path.join(script_path, script_file)
xbmc.executebuiltin('ActivateWindow(busydialog)')
xbmc.executebuiltin('XBMC.PlayerControl(Stop)')
subprocess.Popen(script, shell=True, close_fds=True)