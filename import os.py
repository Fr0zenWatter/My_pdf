import requests
import os
from os import system

def get_pdf(pdf_url,path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }

    response = requests.get(pdf_url, headers=headers)
    with open(path,'wb+') as f:
        f.write(response.content)

def git_push(commit):
    od_arr = ["git add .",'git commit -m "'+commit+'"',"git push"]
    for od in od_arr:
        system(od)

def get_pdf_name(pdf_url,name):
    get_pdf(pdf_url,"Matrix_Computition//" + str(name)+".pdf")
    #上传git
    git_push(name)


get_pdf_name("https://arxiv.org/pdf/2211.05807.pdf","5")



