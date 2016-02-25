# Author = "Conor O'Kelly"
import urllib.request
import os

# Main file to call all of the installer links
def main(user_name):

    down_links = ["vlc.dmg","http://get.videolan.org/vlc/2.2.2/macosx/vlc-2.2.2.dmg"]

    donwload(down_links[0],down_links[1],user_name)

    os.mknod("downloads")


def donwload(file_name, url,user_name):

    user_desktop = ("/Users/" + user_name + "/Desktop")
    download_file = os.path.join(user_desktop, file_name)
    urllib.request.urlretrieve(url, download_file)

    print("%s has finished downloading" % (file_name))


if __name__ == '__main__':
    print("Now downloading all files and saving to desktop")
    main("cokelly")