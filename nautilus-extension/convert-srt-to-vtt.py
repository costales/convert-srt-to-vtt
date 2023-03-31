# convert-srt-to-vtt 0.0.1
# Copyright (C) 2023 Marcos Alvarez Costales https://costales.github.io/about/
#
# convert-srt-to-vtt is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# convert-srt-to-vtt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with convert-srt-to-vtt; if not, see http://www.gnu.org/licenses
# for more information.

import os, re

from gi.repository import Nautilus, GObject

# Python 2 or 3
try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote

class ConvertSrtToVtt(GObject.GObject, Nautilus.MenuProvider):
    """File Browser Menu"""
    def __init__(self):
        GObject.Object.__init__(self)

    def get_file_items(self, window, items):
        """Click on a file"""
        # Checks
        if len(items) != 1:
            return
        
        if items[0].is_directory():
            return

        file_name = unquote(items[0].get_uri()[7:])
        if file_name[-4:].lower() != ".srt":
            return

        # Menu
        menu_item_file = Nautilus.MenuItem(name="click_file", label="Convert to vtt")
        menu_item_file.connect("activate", self.menu_file, file_name)
        return menu_item_file,

    def menu_file(self, menu, filename):
        """Clicked menu"""
        os.system('ffmpeg -y -i ' + re.escape(filename) + " " + re.escape(os.path.splitext(filename)[0]) + '.vtt')
