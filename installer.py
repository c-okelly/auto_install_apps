# Author = "Conor O'Kelly"
import urllib.request
import os
import getpass
from time import gmtime,strftime

# Main file to call all of the installer links
def main():

    # Get folder name
    current_time = time_stamped_folder_name()
    folder_name = ("Downloads_at_" + current_time)


    # Created downloads folder on the user Desktop
    user_name = getpass.getuser()
    save_location = ("/Users/" + user_name + "/Desktop/" + folder_name)
    os.mkdir(save_location)

    # Get download links
    down_links = get_download_links()

    # Complete download

    download(down_links[0],down_links[1], save_location)

    # Notify that donwload has completed

def time_stamped_folder_name():

    current_time = strftime("%H:%M:%S", gmtime())
    return current_time

def get_download_links():

    down_links = ["vlc.dmg","http://get.videolan.org/vlc/2.2.2/macosx/vlc-2.2.2.dmg"]

    return down_links


def download(file_name, url, save_location):

    user_name = getpass.getuser()
    user_desktop = save_location
    download_file = os.path.join(user_desktop, file_name)
    urllib.request.urlretrieve(url, download_file)

    print("%s has finished downloading" % (file_name))


if __name__ == '__main__':
    print("Now downloading all files and saving to desktop")
    main()