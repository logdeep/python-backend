from fastapi import FastAPI

from app.schemas import OEMProduct, ProcessedProduct
from app.service import process_product

app = FastAPI(
    title="OEM Product Processor",
    description="Validate and process OEM product records.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/products", response_model=ProcessedProduct, status_code=200)
def create_product(product: OEMProduct) -> ProcessedProduct:
    return process_product(product)
