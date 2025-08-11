
from pymongo import MongoClient
from models import Category

conn = MongoClient("mongodb://localhost:27017/")

db=conn["app_db"]

collection=db["categories"]

#region seed database
#! WARNİNG: aşağıdaki kodu bir kez çalıştırdıktan sonra yoruma alınız yokda her seferinde eklenmeye devam eder.

# categories=[
#     Category(name="elektronics",description="devices and gadgets etc.").__dict__ ,
#     Category(name="Boxing Eqiupment",description="gloves and handswraps etc.").__dict__ ,
#     Category(name="board game",description="board game such as stragy and monopoly ").__dict__ ,

#            ]
# collection.insert_many(categories)
# #endregion