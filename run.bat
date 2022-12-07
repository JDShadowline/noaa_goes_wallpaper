@echo off
echo +----------------------------+
echo  This is a python script
echo  that gathers NOAA GOES
echo  east images and set them
echo  as the current wallpaper
echo +----------------------------+


set curr_dir=%CD%
call .venv\Scripts\activate && python.exe -m pip install --upgrade pip & pip install -r requirements.txt & python main.py