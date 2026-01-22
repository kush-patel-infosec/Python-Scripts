
from msilib.schema import Error
import requests
import re
from bs4 import BeautifulSoup

def extractLinks(url):
   try:
      count = 0
      reqs = requests.get(url)
      soup = BeautifulSoup(reqs.text, 'html.parser')
      
      f = open("links.txt", "w")

      for link in soup.find_all("a"):
         data = link.get('href')

         data = str(data)
         if '#' not in data:
            count+=1
            f.write(data)
            print(data+'\n')
            f.write("\n")

         if url in data:
            reqs1 = requests.get(data)
            soup1 = BeautifulSoup(reqs1.text, 'html.parser')

            for sub_link in soup1.find_all("a"):
               sub_data = sub_link.get('href')
               sub_data = str(sub_data)
               if '#' not in sub_data and data.startswith(url):
                  count+=1
                  f.write(sub_data)
                  print(sub_data+'\n')
                  f.write("\n\n")

         if(count>500):
            break

      f.close()
   except:
      print(Error)

def extractEmails(url):
   try:
      count = 0
      reqs = requests.get(url)
      dom = requests.get(url).text
      soup = BeautifulSoup(reqs.text, 'html.parser')
      
      link_file = open("links.txt", "w")
      email_file = open("emails.txt", "w")

      for email in re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", dom):
         email_file.write(email)
         email_file.write("\n")

      for link in soup.find_all("a"):
         data = link.get('href')

         data = str(data)
         if '#' not in data and data.startswith('http'):
            count+=1
            # put link in file
            link_file.write(data)
            print(data+'\n')
            link_file.write("\n")
            # put email in file
            dom = requests.get(data).text
            for email in re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", dom):
               email_file.write(email)
               email_file.write("\n")


         if url in data and data.startswith('http'):
            reqs1 = requests.get(data)
            soup1 = BeautifulSoup(reqs1.text, 'html.parser')

            for sub_link in soup1.find_all("a"):
               sub_data = sub_link.get('href')
               sub_data = str(sub_data)
               if '#' not in sub_data and sub_data.startswith('http'):
                  count+=1
               # put link in file
                  link_file.write(sub_data)
                  print(sub_data+'\n')
                  link_file.write("\n\n")
               # put email in file
                  dom = requests.get(data).text
                  for email in re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", dom):
                     email_file.write(email)
                     email_file.write("\n")

         if(count>500):
            break

      link_file.close()
      email_file.close()
   except:
      print(Error)

def extractEmails1(url):
   
   dom = requests.get(url).text

   email_file = open("emails.txt", "w")

   emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", dom).text
   emails.append()
   # email_file.write(emails)
   print (emails)
   email_file.close()

  
# url = 'http://sportspanel.pk/'
# url = 'https://www.geeksforgeeks.org/'
# url = 'http://www.brightbrothers.co.in/'
url = 'https://www.ganpatuniversity.ac.in'
# url = 'https://www.ctae.ac.in/'
# url = 'http://una.org.pk/'
# url = 'https://stackoverflow.com/'

# r = requests.get(url).text
# print(r)
# extractLinks(url)
extractEmails(url)
