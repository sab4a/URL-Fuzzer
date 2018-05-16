import requests

Tofuzz = open('parsed.txt','r')
wordlist=open('wordlist.txt','r')

zero=0
zero2=0
wp_sites=[]
word_list=[]

for line in Tofuzz :
    wp_sites.append(line)

for words in wordlist:
    word_list.append(words)


while len(word_list)!=zero2 and len(wp_sites)!=zero:
    url = ('http://' + wp_sites[zero].replace('\n', '/') + word_list[zero2])
    zero2 += 1
    url2 = url.replace('://', '').replace('/', '^slash^').replace('.', '^dot^')
    print(url)

    if len(word_list)==zero2:
        zero2=0
        zero+=1

    try:
        r=requests.get(url)
        print(r.status_code)
        if r.status_code==200:
            print("file found {} ".format(url))
            # with open("r{} .zip".format(url2), "wb") as code:
            #     code.write(r.content)
    except:
        continue