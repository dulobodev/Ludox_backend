from typing import Union

from fastapi import FastAPI, File, UploadFile

import os
import sys
import uuid


IMAGEDIR = r'C:\Users\eduardo.clobo\Desktop\Ludox_backend\Backend\src\images'

app = FastAPI()

for route in app.routes:
    print(f"🔗 {route.path} - {route.methods}")

@app.get("/")
def read_root():
    return {'Hello': 'World'}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    content = await file.read()

    file_path = os.path.join(IMAGEDIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(content)

    return {'filename': file.filename}


@app.post("/get")
async def get_image():
      
    files = os.listdir(IMAGEDIR)

    print(files)