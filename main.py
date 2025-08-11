

from services import CategoryService
from models import Category
from pprint import pprint
from bson.objectid import ObjectId


service = CategoryService()

#region get all
# service.get_all()

#endregion

#region get_by_id
# service.get_by_id(id="685fb9db5a2c42bf4993588e")

#endregion


#region get all
# service.get_all()

#endregion

#region add
# new_category = Category(name=" new category", description="this is a new category")

# service.add(new_category.__dict__)

#endregion

#region update

# service.update(
#     filter_values={
#         "_id":ObjectId("685fb9db5a2c42bf4993588e")
#     },
#     set_values={
#         "name" : " New Electronics Category",
#         "description": "Electronics devices",
#         "_BaseEntity__status":"Modified"

#     }
# )
#endregion

#region delete
# service.update(
#     filter_values={
#         "_id":ObjectId("685fb9db5a2c42bf4993588e")
#     },
#     set_values={
#         "_BaseEntity__status": "passive"
#     }
# )
#endregion