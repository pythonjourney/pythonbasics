import requests
count = 0
while True:
   response = requests.get('https://notdefined4')
   count = count+1
   print(count)
   print(response.text)




     