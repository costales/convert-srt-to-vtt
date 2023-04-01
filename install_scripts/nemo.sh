#!/bin/bash
sed -i 's/Nautilus/Nemo/g' ../nautilus-extension/convert-srt-to-vtt.py
sudo cp ../nautilus-extension/convert-srt-to-vtt.py /usr/share/nemo-python/extensions/
