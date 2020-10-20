import requests
from bs4 import BeautifulSoup

URL = 'https://www.flipkart.com/apple-iphone-se-red-64-gb/p/itm6e9443811d36a?pid=MOBFRFXHYMPBSB5H&lid=LSTMOBFRFXHYMPBSB5HVHY9KJ&marketplace=FLIPKART&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_na&fm=SEARCH&iid=0006c7b5-06c8-4f7b-b532-80f8554e1e7d.MOBFRFXHYMPBSB5H.SEARCH&ppt=sp&ppn=sp&ssid=vc2ox7pv400000001599161163003&qH=417360a05fc3522d'
#URL = 'https://www.flipkart.com/oppo-a11k-deep-blue-32-gb/p/itm2d16676f7a6e9?pid=MOBFTYWW3YYTFZ6G&lid=LSTMOBFTYWW3YYTFZ6GNZGB7U&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_618fa1cc-dd98-4f22-abec-24d3d7b1708b_1_JQ348E9X4M_MC.MOBFTYWW3YYTFZ6G&ppt=clp&ppn=oppo-mobile-phones-store&ssid=60xj0uv3xs0000001599163221307&otracker=clp_pmu_v2_Oppo%2BMobiles%2Bunder%2B%25E2%2582%25B910K_1_1.productCard.PMU_V2_Oppo%2BMobiles%2Bunder%2B%25E2%2582%25B910K_oppo-mobile-phones-store_MOBFTYWW3YYTFZ6G_neo%2Fmerchandising_0&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Oppo%2BMobiles%2Bunder%2B%25E2%2582%25B910K_LIST_productCard_cc_1_NA_view-all&cid=MOBFTYWW3YYTFZ6G'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
desc = soup.find("span", {'class': '_35KyD6'})
price = soup.find("div", {'class':'_1vC4OE _3qQ9m1'})
converted_price = float(price.get_text()[1:].replace(',',''))
print(converted_price)
print(desc.get_text().strip())