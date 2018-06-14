import requests
title = "spiderman"
payload = {'Title': 'spiderman'}
url = 'https://jsonmock.hackerrank.com/api/movies/search/'
a = requests.get(url, params=payload).json()
return_data = []
print(a)
for i in range(a['total_pages']):
    payload2 = {'Title': 'spiderman', 'page': i}
    res = requests.get(url, params=payload2).json()
    for j in res['data']:
        if a['page'] == i:
            return_data.append(j['Title'])
        else:
            return_data.append(j['Title'])

return_data.sort()

print(len(return_data))


