# -*- coding: utf-8 -*-
# Datei: python-locale/umlaut.py

import time, locale
locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
print("Fix Schwyz! quäkt Jürgen blöd vom Paß")
print(time.strftime("%c"))
