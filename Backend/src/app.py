from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from src.controllers import Auth, Product, Slide

app = FastAPI()

app.mount("/images", StaticFiles(directory="src/images"), name="images")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],         
    allow_headers=["*"],         
)

# Incluindo os routers
app.include_router(Auth.router, tags=["auth"])
app.include_router(Product.router, tags=["products"])
app.include_router(Slide.router, tags=["slide"])

@app.get("/healtcheck")
def read_root():
    return {'Hello': 'World'}
