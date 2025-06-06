
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WC_URL = os.getenv("WC_URL")
WC_CONSUMER_KEY = os.getenv("WC_CONSUMER_KEY")
WC_CONSUMER_SECRET = os.getenv("WC_CONSUMER_SECRET")

if not OPENAI_API_KEY:
    raise Exception("OPENAI_API_KEY non impostata nelle variabili d'ambiente")

openai.api_key = OPENAI_API_KEY

class ProductRequest(BaseModel):
    title: str

@app.get("/")
def read_root():
    return {"message": "AI Agent WooCommerce API online"}

@app.post("/generate-description/")
async def generate_description(product: ProductRequest):
    prompt = f"Genera una descrizione SEO per il prodotto: {product.title}"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        description = response.choices[0].text.strip()
        return {"description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
