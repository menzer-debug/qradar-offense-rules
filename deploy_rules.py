import requests
import os
import json

# GitHub Secrets-dən məlumatları alırıq
QRADAR_IP = os.getenv('QRADAR_IP')
TOKEN = os.getenv('QRADAR_TOKEN')

headers = {
    'SEC': TOKEN,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

def upload_rule(rule_file):
    with open(rule_file, 'r') as f:
        rule_data = json.load(f)
    
    url = f"https://{QRADAR_IP}/api/analytics/rules"
    response = requests.post(url, headers=headers, json=rule_data, verify=False)
    
    if response.status_code == 201:
        print(f"Success: {rule_file} yükləndi.")
    else:
        print(f"Error: {response.text}")

# Rules qovluğundakı bütün json-ları yüklə
for file in os.listdir('rules'):
    if file.endswith('.json'):
        upload_rule(f'rules/{file}')
