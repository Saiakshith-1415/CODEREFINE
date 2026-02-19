import urllib.request, json

data = json.dumps({'email': 'testuser@example.com', 'password': 'testpass'}).encode('utf-8')
req = urllib.request.Request('http://localhost:8000/login', data=data, headers={'Content-Type': 'application/json'}, method='POST')
try:
    with urllib.request.urlopen(req) as r:
        print(r.read().decode())
except Exception as e:
    print(f"Error: {e}")
