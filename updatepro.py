import sqlite3

connection = sqlite3.connect("product.db")

getproductcode = input("enter the product code:")
getproductname = input ("enter the product name:")
getproductprice = input ("enter the product price")
getdistributername = input ("enter the distributer name:")
getmanufacturename = input ("enter the manufacture name:")

result = connection.execute("update productdata set productname='"+getproductname+"',productprice="+getproductprice+",distributername='"+getdistributername+"',manufacturename='"+getmanufacturename+"' where productcode="+getproductcode+"")
connection.commit()

print("data updated successfully")
result = connection.execute("select * from productdata where productcode="+getproductcode+"")

print("data updated")

for i in result:
    print("productcode =>", i[0])
    print("productname =>", i[1])
    print("productprice =>", i[2])
    print("distributername =>", i[3])
    print("manufacturename =>", i[4])

