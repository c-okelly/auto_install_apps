# Author = "Conor O'Kelly"
import urllib.request
import os
import getpass
import time

# Main file to call all of the installer links
def main():

    # Created downloads folder on the user Desktop
    user_name = getpass.getuser()
    os.mkdir("/Users/" + user_name + "/Desktop/App_Downloads")

    # Get download links
    down_links = get_download_links()

    download(down_links[0],down_links[1])

def time_stamped_folder_name():

    time_object = time.gmtime()
    hour = time.gmtime()
    print(time_object[6])


def get_download_links():

    down_links = ["vlc.dmg","http://get.videolan.org/vlc/2.2.2/macosx/vlc-2.2.2.dmg"]

    return down_links


def download(file_name, url):

    user_name = getpass.getuser()
    user_desktop = ("/Users/" + user_name + "/Desktop/App_Downloads")
    download_file = os.path.join(user_desktop, file_name)
    urllib.request.urlretrieve(url, download_file)

    print("%s has finished downloading" % (file_name))


if __name__ == '__main__':
    print("Now downloading all files and saving to desktop")
    # main()
    time_stamped_folder_name()