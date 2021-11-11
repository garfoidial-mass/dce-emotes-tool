from bs4 import BeautifulSoup
import requests
import shutil
import sys
import os

with open(sys.argv[1], encoding='utf8') as fp:
    soup = BeautifulSoup(fp,"html.parser")

emojilinks = []
emotes = soup.find_all("img",class_="emoji")
emotescopy = []
for x in range(0,len(emotes)):
    if emotes[x]["src"] not in emojilinks:
        if "https://cdn.discordapp.com/emojis/" in emotes[x]["src"]:
            emojilinks.append(emotes[x]["src"])
            emotescopy.append(emotes[x])

emotes = emotescopy

def findfileformat(link):
    link = link.replace("https://cdn.discordapp.com/emojis/","",1)
    newlink = ""
    for x in range(0,len(link)):
        if link[x] == ".":
            link = link[slice(x, len(link),1)]
            return link

if not os.path.isdir('emotes'):
    os.mkdir('emotes')

for x in range(0,len(emojilinks)):
    print(f">\emotes\{emotes[x]['title']}{findfileformat(emojilinks[x])}")
    r = requests.get(emojilinks[x], stream=True)
    if r.status_code == 200:                     #200 status code = OK
        with open(f"{os.getcwd()}\emotes\{emotes[x]['title']}{findfileformat(emojilinks[x])}", 'wb', encoding='utf8') as f: 
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

for i in range(0,len(emotes)):
    emotes[i]["src"] = f"{os.getcwd()}\emotes\{emotes[i]['title']}{findfileformat(emojilinks[i])}".strip()

with open(f"{sys.argv[2]}", "w", encoding='utf8') as f_output:
    f_output.write(str(soup))  


#print(emojilinks)