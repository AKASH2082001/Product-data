import sqlite3

connection = sqlite3.connect("product.db")

getcode = input("enter the product code: ")

connection.execute("delete from productdata where productcode="+getcode)
connection.commit()

print("Data deleted successfully")

result = connection.execute("select * from productdata")

print("data updated")

for i in result:
    print("productcode =>",i[0])
    print("productname =>",i[1])
    print("productprice =>",i[2])
    print("distributername =>",i[3])
    print("manufacturename =>",i[3])
