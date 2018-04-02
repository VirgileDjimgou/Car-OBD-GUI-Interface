import requests
import os
from timeit import default_timer as timer


def fct (code):
    val = "000000000"
    b_code = bytearray(code)
    b_val = bytearray(val)
    strSize = len(b_code) 
    for i in range(strSize):
        b_val[8-i] = b_code[strSize-1-i]
    s = str(b_val)
    return ("RR" + s + "DE")

fichier = open("result.txt", "w")
#code = "RR610482175DE"

i = 0

for j in range(611460001,611560000):   #(610050000,610110000) (610000000,610050000) (609000000,609090000)
    nmr = str(j)
    id = fct(nmr)
    print fct(id)
    #i= i+1
    #start = timer()
    r = requests.get("https://nolp.dhl.de/nextt-online-public/de/search?piececode=" + id)
    #end = timer()
    #fichier.write( str(i) + "- " + str(end - start) +  "\n")
    #print (r.status_code)
    paste_url = r.text
    key_1 = paste_url.find("Belgien")
    #print key_1
    if key_1 != -1:
        fichier.write(id + "\n")

fichier.close()

#print ("The pastebin URL is:%s" %paste_url)


