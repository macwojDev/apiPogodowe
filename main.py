# import request get to upload data from url
from requests import get
from json import loads # loads convert string to list or dict
from terminaltables import AsciiTable

# variable to choose polish cities u want to get weather from
# for me it's białystok and wwa - my and my gf cities
CITIES = ['Białystok', 'Warszawa']

# mainloop
def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url) # server's answer
    # print as string --->  print(response.text)
    # print as dict ---> print(loads(response.text))
    
    # list important for creating table
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura', 'Ciśnienie']
    ]
    
    # find out chosen data in json
    for row in loads(response.text):
        if row['stacja'] in CITIES:
        # appending chosen data to our table
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie']
            ])
    # creating table to print out the result
    table = AsciiTable(rows)
    print(table.table)
if __name__=='__main__':
    main()

# status control panel for me to learn how it works
        # print(response)
        # if status==[2xx] ---> ok
        # if status==[3xx] ---> przekierowanie
        # if status==[4xx] ---> error(user fail)
        # if status==[5xx] ---> error(server fail)