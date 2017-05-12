#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 	File: general.py
#	Description: General header file for synfigstudio
#
#	This package is free software; you can redistribute it and/or
#	modify it under the terms of the GNU General Public License as
#	published by the Free Software Foundation; either version 2 of
#	the License, or (at your option) any later version.
#
#	This package is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#	General Public License for more details.
#
# Author: Austin Aigbe <eshikafe@gmail.com>

import gettext
import locale

GETTEXT_PACKAGE = 'myapplication'
APP_NAME = "wxSynfig"

gettext.install(GETTEXT_PACKAGE)

def _(x):
	return gettext.gettext(x)

def N_(x):
		return x

def locale_from_utf8(utf8_str):
    try:
        retval = unicode (utf8_str, "utf-8").encode(locale.getpreferredencoding())
    except:
        retval = utf8_str
    return retval
