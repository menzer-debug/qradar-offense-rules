import requests
import os
import json
QRADAR_IP = os.getenv('QRADAR_CONSOLE_IP')
TOKEN = os.getenv('QRADAR_SEC_TOKEN')

headers = {
    'SEC': TOKEN,
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Version': '12.0'
}

def upload_rule(rule_file):
    try:
        with open(rule_file, 'r') as f:
            rule_data = json.load(f)


url = f"https://{QRADAR_IP}/api/analytics/custom_rules"

        response = requests.post(
            url,
            headers=headers,
            json=rule_data,
            verify=False  # Lab mühiti üçün
        )

        if response.status_code in [200, 201, 202]:
            print(f"[SUCCESS] {rule_file} yükləndi")
        else:
            print(f"[ERROR] {rule_file} → {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"[EXCEPTION] {rule_file} → {str(e)}")

# bütün rule-ları upload et
for file in os.listdir('rules'):
    if file.endswith('.json'):
        upload_rule(f'rules/{file}')
