from fastapi import UploadFile, File, Depends, APIRouter, HTTPException
from fastapi.responses import FileResponse
from src.core.db import client
from src.models.Product import ProductCreate, ProductResponse

import os
import uuid

router = APIRouter()

IMAGEDIR = "src/images/"

db = client["data"]
products_collection = db["products"]

@router.post("/product", response_model=ProductResponse)
async def create_product(
    product: ProductCreate = Depends(ProductCreate.as_form),
    file: UploadFile = File(...),
):
    
    file.filename = f"{uuid.uuid4()}.jpg"
    content = await file.read()

    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(content)

    new_product = product.dict()
    new_product["image_uuid"] = file.filename
    new_product["value"] = float(product.value) 

    result = products_collection.insert_one(new_product)

    return ProductResponse(
        id=str(result.inserted_id),
        image_uuid=file.filename,
        **product.dict()
    )

@router.get("/products")
async def list_products():
    products = []
    for product in products_collection.find():
        products.append({
            "id": str(product["_id"]),
            "title": product["title"],
            "description": product["description"],
            "feedback": product["feedback"],
            "value": product["value"],
            "parcela": product["parcela"],
            "image_url": f"/images/{product['image_uuid']}" 
        })
    return products