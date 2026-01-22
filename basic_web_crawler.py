from msilib.schema import Error
import requests
import re
from bs4 import BeautifulSoup

def crawler(url):
    try:
        count = 0
        reqs = requests.get(url)
        dom = requests.get(url).text
        soup = BeautifulSoup(reqs.text, 'html.parser')
        link_file = open("urls.txt", "w")
        
        for link in soup.find_all("a"):
            data = link.get('href')
            data = str(data)
            if '#' not in data and data.startswith('http'):
                count+=1
                link_file.write(data)
                print(data+'\n')
                link_file.write("\n")
                dom = requests.get(data).text

            if url in data and data.startswith('http'):
                reqs1 = requests.get(data)
                soup1 = BeautifulSoup(reqs1.text, 'html.parser')
                for sub_link in soup1.find_all("a"):
                    sub_data = sub_link.get('href')
                    sub_data = str(sub_data)
                    
                    if '#' not in sub_data and sub_data.startswith('http'):
                        count+=1
                        link_file.write(sub_data)
                        print(sub_data+'\n')
                        link_file.write("\n\n")
                        dom = requests.get(data).text
            
            if(count>500):
                break

        link_file.close()

    except:
        print(Error)

url = input("Enter URL :: ")
extractLinks(url)
