import ctypes, requests, os, time


######################### VARIABLES

url_goes = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/"
latest = "latest.jpg"


######################### FUNCTIONS

def set_windows_wallpaper():
    ## Set current time, +0 GMT (-6 est)
    current_time = time.strftime("%Y%m%d_%H%M", time.gmtime())

    ## Format the URL (flexible for future use)
    goes_url = f"{url_goes}{latest}"

    ## Get the image using the requests library
    response = requests.get(goes_url)
    print(f"Downloaded latest image at {current_time}")

    ## Set the wallpaper to the downloaded image
    print("Setting Wallpaper")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, response.content, 0)
    print("Wallpaper updated!")
    
def main():
    print("Synchronizing....")
    while True:
        if time.strftime("%M", time.gmtime()) == "00" or time.strftime("%M", time.gmtime()) == "15" or time.strftime("%M", time.gmtime()) == "30" or time.strftime("%M", time.gmtime()) == "45":
            print("Ding! Downloading a new image.")
            set_windows_wallpaper()

            # Sleep the script for another 15 minutes
            time.sleep(60 * 15)

        ## Sleep the script until the above is true
        time.sleep(30)

######################### MAIN

if __name__ == "__main__":
    main()
