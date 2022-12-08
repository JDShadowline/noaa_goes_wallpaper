###############################################################################
#                        GOES wallpaper downloader                            #
###############################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program fetches images from the GOES satellite and saves them to a
# directory that then gets used as a wallpaper.
###############################################################################

######################### IMPORTS

import ctypes, requests, os, time


######################### VARIABLES
url_goes = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/"
latest = "latest.jpg"


current_dir = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(script_dir,"images")


running = False


######################### FUNCTIONS

def testvideo():
    import cv2, numpy as np
    writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30,(640,480))

    for frame in range(1000):
        # Create some static
        writer.write(np.random.randint(0, 255, (480,640,3)).astype('uint8'))

    writer.release()

def animation_maker():
    import cv2
    from tqdm import tqdm

  
    # Create a VideoWriter object
    # The first argument is the file name of the video to be created
    # The second argument is the FourCC code, which specifies the codec to be used
    # The third and fourth arguments are the frame size of the video
    # It is important to match the input frame size to the output frame size.
    # The fifth argument is the frames per second
    output = cv2.VideoWriter("animation0.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30, (5000,3000))
    
    # Loop through all the images in the folder
    files = os.listdir(images_path)
    for file in tqdm(files, desc="Processing image animation", total=len(files)):
    
    # Loop through all the files in the sorted list
    # for file in files:
        # Load the image
        # print(file)
        img = cv2.imread(os.path.join(images_path, file))

        # Write the image to the output video file
        output.write(img.astype('uint8'))
    
    # Release the VideoWriter object
    output.release()
    
def get_noaa_goes_image():
    ## Set current time, +0 GMT (-6 est)
    current_time = time.strftime("%Y%m%d_%H%M", time.gmtime())
    
    ## Check if the output directory exists
    if not os.path.exists(images_path):
        os.makedirs(images_path)
        
    ## Format the URL (flexible for future use)
    goes_url = f"{url_goes}{latest}"
    
    ## Get the data using the response lib
    response = requests.get(goes_url)
    print(f"Downloaded latest image at {current_time}")
    
    ## Define the output paths, filename, and write it to the file.
    filename = current_time + ".jpg"
    fullpath = os.path.join(images_path, filename)
    with open(fullpath, "wb") as file:
        file.write(response.content)
        
    return fullpath
    
def set_windows_wallpaper(fullpath):
    print("Setting Wallpaper")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, fullpath , 0)
    print("Wallpaper updated!")
    
def main():
    print("Synchronizing....")
    while True:
        if time.strftime("%M", time.gmtime()) == "00" or time.strftime("%M", time.gmtime()) == "15" or time.strftime("%M", time.gmtime()) == "30" or time.strftime("%M", time.gmtime()) == "45":
            print("Ding! Downloading a new image.")
            set_windows_wallpaper(get_noaa_goes_image())

            # Sleep the script for another 15 minutes
            time.sleep(60 * 15)
        if time.strftime("%M", time.gmtime()) == "00":
            # Create an animation with this new image every hour
            try:
                animation_maker()
            except:
                pass
        ## Sleep the script until the above is true
        time.sleep(30)

######################### MAIN

if __name__ == "__main__":
    main()
    # animation_maker()
    # testvideo()
