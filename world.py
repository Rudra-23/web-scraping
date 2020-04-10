import requests
from bs4 import BeautifulSoup
import string

def gethtml(url):
    r = requests.get(url).text
    return r

if __name__ == "__main__":
    getdata = gethtml("https://www.worldometers.info/coronavirus/country/india/")
    soup=BeautifulSoup(getdata,"html.parser")
    
    ele= soup.find("div",class_="col-md-12",id="news_block")
    ele=ele.get_text().strip()
    

    l=ele.split("\n")
    arr=[]
    for item in l:
        x=[]
        x=item.split(" ")
        for i in x:
            if i[0:5]=="India":
                x.remove(i)
                x.append("India")
        arr.append(x)
        # print(*x)
    arr=arr[:-1]
    for i in arr:
        if len(i)==1:
            arr.remove(i)
    arr=arr[:-1]
    count =0
    print(*arr[0],"\n\n")
    for ele in arr[1:]:
        print(*ele,end=" ")
        count=count+1
        if count == 1:
            print(" : ",end=" ")
        if count==2:
            count=0
            print("\n\n")
    x=input("\n\n\nPress Enter To Exit")
