import requests

Website_Wordlist = open('parsed.txt','r')

for line in Website_Wordlist:

    try:
        page = requests.get('http://' + line.replace('\n','') + '/license.txt')
        txt = page.text

        if 'WordPress' in txt:
            print( '\n\033[1;32m {}is powered by wordpress \033[1;m'.format(line) )

            outF = open("wp.txt", "a")
            outF.write(line)
            outF.close()
        else:
            print( "\n{}is not powered by wordpress ".format(line) )

    except:

        print( "\n" + line + "Website is down")
        continue



