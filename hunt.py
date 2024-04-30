from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
import subprocess
import json
import os
import requests
import re

app = FastAPI()

@app.get("/api/{email}")
async def email_api(email: str = Path(...)):
    try:
        process = subprocess.Popen(['ghunt', 'email', '--json', f'{email}.json', email], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()  # Wait for the process to complete
        if os.path.exists(f'{email}.json'):
            with open(f'{email}.json', 'r') as file:
                email_data = json.load(file)
                os.remove(f'{email}.json')
            return email_data
        else:
            raise HTTPException(status_code=404, detail="Email data not found")
    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="Failed to execute command")

@app.get("/name/{id}")
async def get_contributor_name(id: str):
    
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

    try:
        response = requests.get(f'https://www.google.com/maps/contrib/{id}', headers=headers, verify=True)
        response.raise_for_status()  
        pattern = r'<meta content="Contributions by (.*?)" itemprop="name">'
        matches = re.findall(pattern, response.text)
        if matches:
            return {"Name": matches[0]}
        else:
            raise HTTPException(status_code=404, detail="Contributor's name not found.")
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Failed to fetch data.") from e

