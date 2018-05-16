from bs4 import *
import requests
import re
sickloop=0
page="https://www.top.ge/index.php?pagenr="
My_List=[]

for i in range (1,824):

    page2=page+str(sickloop)
    resp = requests.get(page2)
    txt = resp.text
    sickloop += 1
    soup = BeautifulSoup(txt,"html.parser")

    for link in soup.findAll('a', attrs={'href': re.compile("^http://") ,     }):

       a=(link.get("href"))
       b = re.split( "/" , a)
       c=b[2]
       My_List.append(b[2])


    aa=[x for x in My_List if not '?' in x]

    unique=[]
    for i in aa:
        if i not in unique:
            unique.append(i)

    outF = open("parsed.txt", "w")
    for line in unique:
      print(line)
      outF.write(line)
      outF.write("\n")
    outF.close()
