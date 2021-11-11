# dce-emotes-tool
A python script that downloads emotes from a Discord Chat Exporter generated html file, and generates a new file using the downloaded emotes instead.

# Setup:
  1. Install the latest version of python from python.org
  2. This script requires the BeautifulSoup and requests python packages, so you will have to run `pip3 install bs4` and `pip3 install requests` in your terminal (command prompt for windows users) to install them
  3. move the script into whatever directory you want your emotes to be saved into (a subfolder will be created with them inside)

# Usage:
  1. Open your terminal and navigate to the directory you place the script in
  2. run: `python downloademotes.py <path to input file> <path to output file>`
  3. this will create the output file you specified, and a folder named emotes with all of the emojis used in that channel

# Notes:
  May require Linux & Mac users to change the two backslashes in the script to forward slashes
  
