from requests import get
from json import loads
from say import *

def temp(citi):
        url = 'https://danepubliczne.imgw.pl/api/data/synop'
        response = get(url)

        for row in loads(response.text):
            #print(row)
            if row['stacja'] in citi:
                t = row['temperatura']
                say(t.replace(".", ",") + '°C')

def pogo(citi2):
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)

    for row in loads(response.text):
        #print(row)
        if row['stacja'] in citi2:
            s = row["suma_opadu"]
            a0 = ["0"]

            if s in a0:
                say("Jest tam słonecznie")
