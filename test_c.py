import urllib.request, json

c_code = """#include <stdio.h>
int main() {
    printf("C works: %d\\n", 789);
    return 0;
}"""

data = json.dumps({'code': c_code, 'language': 'c'}).encode('utf-8')
req = urllib.request.Request('http://localhost:8000/run', data=data, headers={'Content-Type': 'application/json'}, method='POST')
try:
    with urllib.request.urlopen(req) as r:
        print(r.read().decode())
except Exception as e:
    print(f"Error: {e}")
