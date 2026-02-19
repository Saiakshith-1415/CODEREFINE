import urllib.request, json

cpp_code = """#include <iostream>
int main() {
    std::cout << "C++ works: 999" << std::endl;
    std::cout.flush();
    return 0;
}"""

data = json.dumps({'code': cpp_code, 'language': 'cpp'}).encode('utf-8')
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
