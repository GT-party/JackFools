@echo off
git clone https://github.com/Geardung/JackFools
cd JackFools
git config --global --add safe.directory %cd%
py -m pip install --upgrade pip
py -m pip install -r reqs.txt
%SystemRoot%\explorer.exe %cd%