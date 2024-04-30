import requests
import re
id = 117512536359598436616
headers = {
    'Host': 'www.google.com',
    'Sec-Ch-Ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Full-Version': '""',
    'Sec-Ch-Ua-Arch': '""',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '""',
    'Sec-Ch-Ua-Model': '""',
    'Sec-Ch-Ua-Bitness': '""',
    'Sec-Ch-Ua-Wow64': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.60 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Service-Worker-Navigation-Preload': 'true',
    'X-Client-Data': 'CKP4ygE=',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=0, i',
}
response = requests.get(f'https://www.google.com/maps/contrib/{id}', headers=headers, verify=True)
pattern = r'<meta content="Contributions by (.*?)" itemprop="name">'
matches = re.findall(pattern, response.text)
if matches:
    for match in matches:
        print("Name:", match)
else:
    print("Contributor's name not found.")
