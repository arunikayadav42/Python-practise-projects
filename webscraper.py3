import requests,string,bs4
url="https://www.humblebundle.com/books/network-security-certification-books"
r=requests.get(url)
#print(r.text)
tier_dict={}
soup = bs4.BeautifulSoup(r.text,'html.parser')
tiers = soup.select(".dd-game-row")

for tier in tiers:
	#only for sections that have a headline
	if tier.select(".dd-header-headline"):
		#grab tier name (and price)
		tier1=tier.select(".dd-header-headline")
		tiername=tier1[0].text.strip()

		#grab product names
		product_names=tier.select(".dd-image-box-caption")
		product_names=[prodname.text.strip() for prodname in product_names]
		#build dictionary
		tier_dict[tiername]={"products":product_names}

tier_headlines = soup.select(".dd-header-headline")
#print (tier_headlines)
# for tier in tier_headlines:
# 	print (tier.text.strip())
stripped_tier=[tier.text.strip() for tier in tier_headlines]
#print(stripped_tier)
# tiers={
# 	'tier1':{
# 	'price':500,
# 	'products':['name1','name2']
# 	},
# 	'tier2':{
# 	'price':500,
# 	'products':['name1','name2']
# 	}
# }
for tiername,tierinfo in tier_dict.items():
	print(tiername)
	print("products:")
	print("\n".join(tierinfo['products']))
	print("\n\n")
# print (stripped_productnames[4])
# print ([name.split()[1][1] for name in stripped_tier if name.startswith('Pay')])