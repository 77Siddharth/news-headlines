import requests 
from bs4 import BeautifulSoup
from csv import writer

#PUT THE URL INSIDE GET
response  = requests.get('https://www.thehindu.com/todays-paper/')

bs = BeautifulSoup(response.text ,'html.parser')
headlines = bs.findChild(class_ = 'archive-list')

with open('news.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["headlines"])

    heads = headlines.get_text().split("\n")
    i=0
    for head in heads:
        if head != "":
            i=i+1
            hea = head

            # number the headlines
            print(str(i)+"."+ hea + "\n")

            csv_writer.writerow([hea])