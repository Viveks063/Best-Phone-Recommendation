import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Description = []
Reviews = []
Prices = []
Link = []
for i in range(2,18):
    url = "https://www.flipkart.com/search?q=mobiles+under+200000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)
        #print(r)

    soup = BeautifulSoup(r.text, "lxml")

    box = soup.find("div",class_="DOjaWF gdgoEp")

    names = box.find_all("div",class_ = "KzDlHZ")
    for i in names:
        name = i.text
        Product_name.append(name)


    prices = box.find_all("div",class_ = "Nx9bqj _4b5DiR")
    for i in prices:
        name = i.text
        Prices.append(name)

    desc = box.find_all("ul",class_="G4BRas")
    for i in desc:
        name = i.text
        Description.append(name)

    links = box.find_all("a",class_="CGtC98")
    for i in links:
        href = i.get("href")
        if href:
            Link.append("https://www.flipkart.com" + href)
print(len(Link))
min_len = min(len(Product_name), len(Prices), len(Description))
Product_name = Product_name[:min_len]
Prices = Prices[:min_len]
Description = Description[:min_len]
    #rev = box.find_all("div","XQDdHH")
    #for i in rev:
    #    name = i.text
    #    Reviews.append(name)
    #print(len(Reviews))

df = pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Description":Description,"Link":Link})

df.to_csv("C:/Users/Vivek/Mobile Recommendation/flipkart_mobile_dataset1.csv")

















    #print(soup)

    #while True:
#np = soup.find("a",class_ ="_9QVEpD").get("href")
#cnp = "https://www.flipkart.com"+np
#print(cnp)
    
