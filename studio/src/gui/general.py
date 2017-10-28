#	Synfig-Reloaded: general.py
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
#  wxSynfig: Copyright (c) 2017 Austin Aigbe
#  Synfig: Copyright (c) 2002 Robert B. Quattlebaum Jr.

import gettext
import locale
import os
#import inspect

GETTEXT_PACKAGE = 'myapplication'
APP_NAME = "wxSynfig"
VERSION = "0.0.1"

gui_path = os.path.dirname(__file__)
src_path = os.path.dirname(gui_path)
studio_path = os.path.dirname(src_path)

images_path = os.path.join(studio_path, "images//")

#__FILE__ = 


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
