from src.models.product import (
    create_product,
    delete_product,
    get_products,
    get_product
)
from src.server.database import connect_db, db, disconnect_db


async def products_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    product_collection = db.product_collection

    product =  {
        "name": "boina",
        "description": "boina de tricô com forro algodão",
        "price": "30.00",
        "image": "inserir imagem_boina",
        "code": 1234
    }

    if option == '1':
        product = await create_product(
            product_collection,
            product
        )
        print(product)
    elif option == '2': 
        product = await get_product(
            product_collection,
            product["code"]
        )
        print(product)
    elif option == '3': 
        product = await get_product(
            product_collection,
            product["code"]
        )

        result = await delete_product(
            product_collection,
            product["_id"]
        )
        print(result)
    elif option == '4':
        products = await get_products(
            product_collection,
            skip=0,
            limit=5
        )
        print(products)

    await disconnect_db()