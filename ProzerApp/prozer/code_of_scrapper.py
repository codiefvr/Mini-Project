from bs4 import BeautifulSoup
import requests

l = []
t,m,o,n,z=[],[],[],[],[]
headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51  Safari/537.36"}
def amazon(x):
    try:
        #for amazon
        print("From Amazon")
        html_text = requests.get(x, headers=headers).text
        code = BeautifulSoup(html_text, 'html.parser')
        a = code.find(id="productTitle")
        b = a.get_text()
        c = code.find('span', class_='a-offscreen')
        l.append(c.text)
       # rev = code.find('span',class_="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold")
       # review = rev.get_text()
       # print(review)
        return b, c.text
    except:
        return 1

def flipkart(x):
    try:
        # for flipkart
        print("From Flipkart")
        html_text = requests.get(x, headers=headers).text
        code = BeautifulSoup(html_text, 'html.parser')
        a = code.find('span', class_='B_NuCI')
        b = a.get_text()
        c = code.find('div', class_='_30jeq3 _16Jk6d')
        l.append(c.text)
        return b, c.text

    except:
        return 1

def reliance(x):
    try:
        print("From reliance_digital")
        html_text = requests.get(x, headers=headers).text
        code = BeautifulSoup(html_text, 'html.parser')
        a = code.find('h1', class_='pdp__title mb__20')
        b = a.get_text()
        d = []
        for item in code.find_all('span', class_="pdp__offerPrice"):
            d.append(item.get_text())   
        l.extend(d)
        return b, [i for i in d]
    except:
        return 1

def mini():
    for item in l:
        if item is None:
            continue
        else:
            t.append(item.replace("₹",""))
    for j in t:
        m.append(j.replace(",",""))

    for i in m:
        z.append(float(i))
    for k in z:
        n.append(int(k))
    
    o.append(min(n))
    
    for i in range(0,5):
        if(o[0] == n[i]):

            return i


            