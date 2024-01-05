@echo off
git clone https://github.com/GT-party/JackFools
cd JackFools
git config --global --add safe.directory %cd%
py -m pip install --upgrade pip
py -m pip install -r reqs.txt
del install.bat
del README.md
%SystemRoot%\explorer.exe %cd%