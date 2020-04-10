import requests
from bs4 import BeautifulSoup
import string


def gethtml(url):
    r = requests.get(url).text
    return r


if __name__ == "__main__":

    getdata = gethtml("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(getdata, "html.parser")
    l = []
    for ele in soup.find(class_="table table-striped").find("tbody").find_all("td"):
        l.append(ele.string)
    n = len(l)-5
    l = l[:n]
    data = []
    x = []
    for i in l:
        x.append(i)
        if len(x) == 5:
            data.append(x)
            x = []

    state = input("Enter the state :")
    state = string.capwords(state)
    flag = False
    cured, death, cases = 0, 0, 0
    if state == "All":
        for a, b, c, d, e in data:
            print("Serial number :"+str(a))
            print("State : "+str(b))
            print("Confirmed cases : "+str(c))
            print("Cured cases : "+str(d))
            print("Deaths :"+str(e))
            print(" ")
            cured += int(d)
            death += int(e)
            cases += int(c)
        print("Total cases in India : "+str(cases))
        print("Total cured cases in India : "+str(cured))
        print("Total deaths in India : "+str(death))
        flag = True

    for a, b, c, d, e in data:
        if state == b:
            print("State : "+str(b))
            print("Confirmed cases : "+str(c))
            print("Cured cases : "+str(d))
            print("Deaths :"+str(e))
            flag = True

    if flag == False:
        print("Enter a Valid state !")

    a = input("")
