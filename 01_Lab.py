
from pymongo import MongoClient

from pprint import pprint

#!  1. Connet to MongoDB

conn = MongoClient("mongodb://localhost:27017/")

#!  2. Create a database called "mydatabase"
db = conn["mydatabase"]

#!  3. Create a database called "mycollection"
collection = db["products"]
#region İnsert(create) operations

#? 4.insert a single record 
# product = {
#     "name":"Macbook Pro",
#     "price":385000,

# }

# result=collection.insert_one(product)
# print(result)

#* insert 2

# product = {
#     "name":"iphone 14 pro max",
#     "price":70000,
#     "GB":256 
# }

# result=collection.insert_one(product)
# print(result)


#endregion



#region Bulk İnsert ( create) operations

# products = [
#     {"name": "Lenova x1 Carbon","price":120000},
#     {"name": "Dell XPS 13","price":150000},
#     {"name": "HP Spectrex360","price":140000},
#     {"name":"Asus zenbook 14","price":130000},
#     {"name": "apple macbook air","price":160000},
#     {"name": "apple ipas pro", "price":80000},


# ]
#! birden fazla veri eklemek için insert_many kullanılır.
# result = collection.insert_many(products)
# print(result)

#endregion

#region Read(Retrieve) Operations

#*veri tabanındaki tüm verileri ekrana yazdırır

# for item in collection.find():
#     pprint(item)

#*fiyatı 100000 ' den büyük olanları listeleyelim

# from pprint import pprint

# filter = {"price": {
#     "$gt": 100000
#         }
#     }
# for item in collection.find(filter):
#     pprint(item)
#*fiyatı 120000'e eşit olan ürünleri listeleyelim


# filter = {"price": {
#     "$eq": 120000
#         }
#     }
# for item in collection.find(filter):
#     pprint(item)

#*Fiyatı 150000 den küçük ve 100000 den büyük olan ürünleri listeleyin

# filter_criteria = {
#     "price": {
#         "$gt": 100000,
#         "$lt": 150000
#     }
# }


# results = collection.find(filter_criteria)

# for item in results:
#     pprint(item)

#*fiyatı 120000 yada 160000 yada 385000 olan ürünleri listeleyin.
#?bu sorguda in operatörü ile hızlı ve kolay bir şekilde çözdük. İn yerine Or operatörüde kullanılabilir fakat kodumuz uzamış olurdu.

# filter = {
#     "price": {
#         "$in": [120000, 160000, 385000]
#     }
# }

# for item in collection.find(filter):
#     pprint(item)

#endregion 

#*adında apple geçen ve fiyatı 100000 den küçük olan ürünleri listeleyin
filter = {
    "$and":[
        {"name":{"$regex" : "apple"}},
        {"price": {"$lt": 100000}}
    ]
}

result = collection.find(filter)

for item in result:
    print(item)


