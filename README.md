# GOES Wallpaper Downloader

This program is free software that fetches images from the GOES satellite and saves them to a directory that then gets used as a wallpaper.
Requirements

- Python 3
- requests
- ctypes

## Usage

To run the script, simply type the following in your terminal:

    python goes_wallpaper_downloader.py

The script will run in the background and automatically update your wallpaper every 15 minutes with the latest GOES image.
License

This program is licensed under the MIT License. For more information, see the LICENSE file.

## TODO

It is currently not required to save each of the images to a folder. The original idea was to use these for a high quality animation but we can also just get the lastest n amount from the NOAA url to create that on the fly.
