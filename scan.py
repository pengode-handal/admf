#recode?  Sangaddddd cupuuuuuuuuuuu, recode cupu kli,  ga menghargai _-
#mengimportan bahan
from __future__ import print_function
import sys
import time
import os
import time
import socket
import argparse 
import requests
import asyncio
import aiohttp
from aiohttp import ClientSession

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--domain", help="masukan domainya")
  parser.add_argument("-v", "--version", action="version", version="Tools Admin Finder Ver 1.2.1")
  parser.add_argument("-i", "--install", help="untuk install")
  args = parser.parse_args()
  
  if args.install:
    from os import system as sistem
    from sys import exit as keluar
    sistem("pip3 install requests")
    sistem("pip3 install -r bahan.txt")
    print("Udah ke Install")
    keluar("")
  if args.domain:
    print(""" \033[92m \n
           _              __ _           _
  __ _  __| |_ __ ___    / _(_)_ __   __| | ___ _ __
 / _` |/ _` | '_ ` _ \  | |_| | '_ \ / _` |/ _ \ '__|
| (_| | (_| | | | | | | |  _| | | | | (_| |  __/ |
 \__,_|\__,_|_| |_| |_| |_| |_|_| |_|\__,_|\___|_|
 """);
    print(""" \33[94m \n
########################################################
* author by : BabwaXgura     team:Muslim Cyber Anonymous
* coded by : BabwaXgura      thanks to: Allah,member MCA
########################################################\n\n
""")
  #memulai masukan target  
  target = args.domain
  #mengecek prokotol
  target = target.replace('https://', '')
  target = target.replace('http://', '')
  tar_list = target.split('/')
  for tar in tar_list:
      if tar == '':
          tar_list.remove(tar)
  target = '/'.join(tar_list)
  target = 'http://' + target
  
  
  
  #define variables, functions, etc.
  mulai = time.time()
  
  adaa = []
  
  conn = aiohttp.TCPConnector(
          family=socket.AF_INET,
          verify_ssl=False,
      ) 
  #men scanning
  async def fetch(url, session):
      async with session.get(url) as response: 
          status = response.status #mengecek responding website
          if status == 200:
              print("\33[97;1mketemu   \33[1;0m{}\33[97;1m   {}".format(response.url, status))
              adaa.append(response.url)
          elif status == 404:
              print("\33[91;1mga ketemu \33[94;1m{}\33[91;1m 404 {}".format(response.url, status))
          elif status == 403:
              print("\33[91;1mforbidden \33[94;1m{}\33[91;1m 403 \33[95;1m{}".format(response.url, status))
          else:
            print("\33[95;1m??? {} ??? {}".format(response.url, status))
          return await response.read()
  #membuka list direktori
  async def run():
      url = target + "{}"
      tasks = []
      lisnya = open('list_dir.txt', 'r')
      paths = []
      for path in lisnya:
          path = path.replace('\n','')
          paths.append(path)
  
      async with ClientSession(connector=conn) as session: #creates the tasks
          for ano in paths:
              task = asyncio.ensure_future(fetch(url.format(ano), session))
              tasks.append(task)
  
          responses = asyncio.gather(*tasks)
          await responses
          
  #start loop        
  loop = asyncio.get_event_loop()
  
  future = asyncio.ensure_future(run())
  loop.run_until_complete(future)
  
  #mengeluarkan hasil
  berakhir = time.time()
  lamanya = berakhir - mulai
  print("\33[93;1mWaktu scanning butuh {} detik untuk selesai\n".format(lamanya))
  print("\33[91;1m### \33[93;1mnih hasilnya \33[91;1m###\33[1;0m")
  if len(adaa) == 0:
      print("\33[94;1m!!! NO RESULTS !!!")
  else:
      for ada in adaa:
          print(ada)    
  print("\33[91;1m#####################")
  
if __name__ == '__main__':
  main()
