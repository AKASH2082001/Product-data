import sqlite3

connection = sqlite3.connect("product.db")


# connection.execute(''' Create Table Productdata(
#                   productcode integer primary key autoincrement,
#                   productname text,
#                   productprice integer,
#                   distributername text,
#                   manufacturename text
#
# )''')
#
# print("table created successfully")

getproductname = input ("enter the product name:")
getproductprice = input ("enter the product price")
getdistributername = input ("enter the distributer name:")
getmanufacturename = input ("enter the manufacture name:")

connection.execute("insert into productdata(productname,productprice,distributername,manufacturename) values('"+getproductname+"',"+getproductprice+",'"+getdistributername+"','"+getmanufacturename+"')")

connection.commit()
connection.close()

print("inserted successfully")