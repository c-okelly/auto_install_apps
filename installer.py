# Author = "Conor O'Kelly"
import urllib.request

# Main file to call all of the installer links
def main():

    down_links = ["vlc.dmg","http://get.videolan.org/vlc/2.2.2/macosx/vlc-2.2.2.dmg"]

    donwload(down_links[0],down_links[1])



def donwload(file_name, url):

    urllib.request.urlretrieve(url, file_name)
    print("%s has finished downloading" % (file_name))


if __name__ == '__main__':
    print("Now downloading all files and saving to desktop")
    main()