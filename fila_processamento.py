import json
import requests

url = "http://localhost:8080/shipping/process"

with open('result.txt', 'r') as result:
    data = json.load(result)

carrier = data['carrier']
package_id = data['id']

for shipping in data['shippings']:
    id = shipping['id']
    tracking_code = shipping['tracking_code']
    complain = shipping['complain']
    request = {}
    request['msg'] = { 'carrier': carrier, 'complain': complain, 'id': id, 'package_id': package_id, 'tracking_code' : tracking_code}

    response = requests.post(url = url, json = request, headers= {"Content-Type": "application/json"})
    
    print(response.status_code, response.reason)
    print(response.text[:300])