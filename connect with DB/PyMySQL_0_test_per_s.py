import datetime

data = ("DR0005", "西瓜汁", datetime.date(2024, 9, 22), "TW", 70, "飲品")

da = "INSERT INTO drink VALUES(%s, %s, %s, %s, %s, %s)" % data
print(da)
