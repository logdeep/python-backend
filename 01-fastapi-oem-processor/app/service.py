from app.schemas import OEMProduct, ProcessedProduct


def process_product(product: OEMProduct) -> ProcessedProduct:
    """Apply the core product calculation independently of HTTP concerns."""
    total_value = round(product.quantity * product.price, 2)
    return ProcessedProduct(
        product_id=product.product_id,
        product_name=product.product_name,
        quantity=product.quantity,
        unit_price=product.price,
        total_value=total_value,
    )
