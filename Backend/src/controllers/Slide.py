from fastapi import UploadFile, File, APIRouter
from fastapi.responses import FileResponse

import os
import uuid

router = APIRouter()

IMAGEDIR = 'image/'

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    content = await file.read()

    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(content)

    return {'filename': file.filename}


@router.post("/get")
async def get_image():
      
    files = os.listdir(IMAGEDIR)

    for file in files:
        path = f"{IMAGEDIR}{file}"

    return FileResponse(path)