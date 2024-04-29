from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
import subprocess
import json
import os

app = FastAPI()

@app.get("/api/{email}")
async def email_api(email: str = Path(...)):
    try:
        process = subprocess.Popen(['ghunt', 'email', '--json', f'{email}.json', email], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()  # Wait for the process to complete
        if os.path.exists(f'{email}.json'):
            with open(f'{email}.json', 'r') as file:
                email_data = json.load(file)
            return email_data
        else:
            raise HTTPException(status_code=404, detail="Email data not found")
    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="Failed to execute command")
