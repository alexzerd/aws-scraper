import requests
import time
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def get_aws_ip_ranges():
    url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
    response = requests.get(url)
    if response.status_code == 200:
        ip_ranges = response.json()['prefixes']
        prefix_ids = [ip_range['ip_prefix'] for ip_range in ip_ranges if ip_range['service'] in ['S3', 'ROUTE53_HEALTHCHECKS']]
        return prefix_ids
    else:
        return 'Unable to fetch data'

def index():
    aws_ip_ranges = get_aws_ip_ranges()
    return render_template('index.html', ip_ranges=aws_ip_ranges)

if __name__ == '__main__':
    while True:
        app.run(host='0.0.0.0')
        time.sleep(3600)