

from abc import ABC, abstractmethod
from setting import collection
from models import Category
from pprint import pprint
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId


class BaseService(ABC):
    @abstractmethod
    def get_all(self):
        pass

    
    @abstractmethod
    def get_by_id(self,id:str):
        pass
    
    @abstractmethod
    def add(self,entity:dict):
        pass
    @abstractmethod
    def update(self , filter_values:dict, set_values:dict):
        pass 
        


class CategoryService(BaseService) :
    def get_all(self):

        try: 
            query = {
                "_BaseEntity__status":{
                    "$in":["Active", "Modified"]}
            }

            #! select(projection) işlemi veritabanındaki tüm sütunlar içerisinde ki veriyi getirmek yerine sadece belirli sütunlari getirmek için kullanılır
            #! SQL de select MongoDb de projection
            projection = {
                "_id":0,         #bu sütunu hariç tut
                "name":1,       #bu sütunu ver 
                "description":1,
            }     

            results = collection.find(query,projection).sort("name", 1)  # 1 ascending , -1 descending

            for item in results:
                pprint(item)
        except PyMongoError as err:
            print(f"An error occured:{err}") 

    def get_by_id(self,id:str):
        try:
            query = {
                "_id" : ObjectId(id),
                "_BaseEntity__status":{
                    "$in":["Active", "Modified"]}
            }

            projection = {
                "_id":0,         #bu sütunu hariç tut
                "name":1,       #bu sütunu ver 
                "description":1,
            }     

            results = collection.find(query,projection).sort("name", 1)  # 1 ascending , -1 descending

            for item in results:
                pprint(item)
        except PyMongoError as err:
           print(f"An error occured:{err}")


    def add(self,entity:dict):
        try:
            collection.insert_one(entity)
            print("entity added sucessfully")
        except PyMongoError as err:
           print(f"An error occured:{err}")
        
    def update(self , filter_values:dict,set_values:dict):
        try:
            result = collection.update_one(
                filter_values,
                {
                    "$set": set_values
                }
            )
            pprint(f"{result.modified_count} document(s) updated.")

        except PyMongoError as err:
            print(f" an error occured: {err}") 