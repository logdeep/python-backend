from pydantic import BaseModel, Field, ConfigDict


class OEMProduct(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    product_id: str = Field(min_length=1, max_length=64)
    product_name: str = Field(min_length=1, max_length=200)
    quantity: int = Field(ge=0)
    price: float = Field(ge=0, allow_inf_nan=False)


class ProcessedProduct(BaseModel):
    product_id: str
    product_name: str
    quantity: int
    unit_price: float
    total_value: float
    status: str = "processed"
