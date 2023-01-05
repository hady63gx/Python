from pymongo import MongoClient

# 要確定 mongodb 是啟動的，才能連得上。
connection = MongoClient(host='localhost', port=27017)
db = connection.Drink_dbname  # use database as name as :Drink_dbname
collection = db['Drink_collection_name']   # create collection Drink_collection_name
print("collection: ", collection)

# 搜尋
id_name = 12345
my_query = {'_id': id_name}
# my_query = {}
data = list(collection.find(my_query))
print("data =", data)
print("type(data): ", type(data))

# 如果想刪除 collection 可以用 drop()
# db.Drink_collection_name.drop()

# 如果想刪除資料庫，要先確認現在使用哪個資料庫，
# 因為語法中沒有需要加資料庫名稱!