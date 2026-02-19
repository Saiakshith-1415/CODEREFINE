import urllib.request, json

java_code = """public class Main {
    public static void main(String[] args) {
        System.out.println("Java works: 555");
    }
}"""

data = json.dumps({'code': java_code, 'language': 'java'}).encode('utf-8')
req = urllib.request.Request('http://localhost:8000/run', data=data, headers={'Content-Type': 'application/json'}, method='POST')
try:
    with urllib.request.urlopen(req) as r:
        response = r.read().decode()
        print("Response:", response)
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(f"Response: {e.read().decode()}")
except Exception as e:
    print(f"Error: {e}")
