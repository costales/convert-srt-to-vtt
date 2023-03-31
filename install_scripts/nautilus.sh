#!/bin/bash
sed -i 's/Nautilus/Caja/g' ../nautilus-extension/convert-srt-to-vtt.py
sudo cp ../nautilus-extension/convert-srt-to-vtt.py /usr/share/nautilus-python/extensions/
