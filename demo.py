import requests
url='http://www.hypercityindia.com/toys.html'
headers = {'x-api-key': '53401fd5-1dd3-479c-9826-e949598451ab'}
response = requests.post('https://api.geekflare.com/dnsrecord', json = {
            "url": url
            },headers=headers)
res=response.json()
print(res)
print(res['data'][0]['country'])
print(res['data'][0]['data']['A'][0])
# print(response.json)

# http://guruincsite.com/2.php