from src.models.order_item import (
    create_order_item,
    get_order_item_by_email_user,
    delete_order_item)

from bson.objectid import ObjectId

from src.server.database import connect_db, db, disconnect_db


async def order_items_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_items_collection = db.order_items_collection

    order_item =  {
        "order": 
            {
            "_id" : ObjectId("00000000000"),
            "user" : {"_id" : ObjectId("00000000000"),
                "name": "Luiza",
                "email": "lu_domagalu@gmail.com",
                "password" : "213sd312re3",
                "is_active" : True,
                "is_admin" : False
            },
            "create" : "luiza",
            "address" : ObjectId("00000000000"),
            "authority" : "Ok"
            },
        "product": [
            {
                "_id" : ObjectId("COLOCAR ID"), #TODO
                "name": "boina",
                "description": "boina de tricô com forro algodão",
                "price": "30.00",
                "image" : "<image>",
                "code" : 1234,
            }
        ],
        "price": 25.00,
        "paid": True
    }

    if option == '1':
        new_order_item = await create_order_item(order_items_collection, order_item)
        print(new_order_item)
         
    elif option == '2':
        order_item = await get_order_item_by_email_user(order_items_collection, order_item["order"]["user"]["email"])

        result = await delete_order_item(
            order_items_collection,
            order_item["_id"]
        )

        print(result)
        
    await disconnect_db()