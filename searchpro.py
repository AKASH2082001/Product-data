import sqlite3

connection = sqlite3.connect("product.db")

getproductprice = input("enter the price to be searched :")

result = connection.execute("select * from productdata where productprice="+getproductprice)

for i in result:
    print("productcode =>", i[0])
    print("productname =>", i[1])
    print("productprice =>", i[2])
    print("distributername =>", i[3])
    print("manufacturename =>", i[4])
