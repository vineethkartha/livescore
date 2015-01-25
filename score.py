from bs4 import BeautifulSoup
import requests
import time
import Tkinter
import tkMessageBox

today=time.strftime("%Y-%m-%d");

url="http://www.livescore.com/soccer/"+today+"/";
r=requests.get(url);

data=r.text
soup=BeautifulSoup(data);
count=0;
pl1=""
pl2=""
score=""
line=""
for link in soup.find_all('div'):
    if (link.get('class')==['row','row-tall','mt4']):
        count=count+1;
    if(link.get('class')==['ply','tright','name']):
        pl1= ''.join(link.contents)
    if(link.get('class')==['sco']):
        for st in link.stripped_strings:
            score=''.join(repr(st))
    if(link.get('class')==['ply','name']):
        pl2= ''.join(link.contents)
        line=line +pl1+" : "+score+" : "+pl2+"\n";
    if(count>1):
        break;

tkMessageBox.showinfo("Score", line)

window.mainloop()
