import requests

URL = 'http://127.0.0.1:5000/prediction'
X = {
     'x1': 0.002287,
     'x2': -0.02005,
     'x3': 0.04493
     }

r = requests.post(URL, json = X)

if r.status_code == 200:
    print('Local host responded')
    print(f'Prediction result: {r.text}')
else:
    print('Recheck deploy status')
