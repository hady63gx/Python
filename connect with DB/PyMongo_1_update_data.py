from pymongo import MongoClient
import pymongo

# 要確定 mongodb 是啟動的，才能連得上。
connection = MongoClient(host='localhost', port=27017)
db = connection.Drink_dbname  # use database as name as :Drink_dbname
collection = db['Drink_collection_name']   # create collection Drink_collection_name
print("collection: ", collection)

# 輸入
data = {"_id": 12345,
        "drink": [{"hot": {"coffee": 100, "tea": 90}},
                  {"juice": {"apple": 95, "banana": 85}}],
        "table": ["", "A01", "A02", "A03", "A04", "A05"]
        }
try:
    result = collection.insert_one(data)
    print("已新增", data)
except pymongo.errors.DuplicateKeyError as err_name:
    print(err_name)
    print("已經存在 _id: ", data['_id'], "(因此不寫入)")
