#Tohitrov Bobur
#1- savol
import psycopg2

conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='1',
                        host='localhost',
                        port=5432)

cur = conn.cursor()
# new_Product = """create table product(
# id setrial primary key ,
# name varchar (250),
# price int ,
#  color varchar (250),
#  image varchar (250),
# )"""

#2-savol
# def insert_product(name,price,image):
#     a="""insert into product(name,price,image) values (%s,%s,%s)"""
#     data = (name, price, image)
#     cur.execute(a, data)
#     conn.commit()
#     cur.close()
#     conn.close()
#     print("Product inserted successfully")
#
#
# def select_all_products():
#     a="""select * from product"""
#     cur.execute(a)
#     print(cur.fetchall())
#
# def update_product(product_id, new_name, new_price, new_image):
#     a="""update product set name=%s,price=%s,image=%s where id=product_id"""
#     data = (new_name, new_price, new_image)
#     cur.execute(a, data)
#     conn.commit()
#     print("Product updated successfully")
#
# def delete_product(product_id):
#     a="""delete from product where id=product_id"""
#     cur.execute(a)
#     conn.commit()
#     print("Product deleted successfully")
#
#
# insert_product('ali',4343,'q3tfeef')
#3-savol
# class Alphabet:
#     def __init__(self):
#         self.letters = 'abcdefghijklmnopqrstuvwxyz'
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.letters):
#             letter = self.letters[self.index]
#             self.index += 1
#             return letter
#         else:
#             raise StopIteration
#
# alpha = Alphabet()
#
# for letter in alpha:
#     print(letter)
#4-savol
# import threading
# import time
#
# def print_numbers(start, end):
#     for i in range(start, end+1):
#         print(i)
#         time.sleep(1)
#
# def print_letters():
#     for letter in 'ABCDE':
#         print(letter)
#         time.sleep(1)
#
# t1 = threading.Thread(target=print_numbers, args=(1, 5))
# t2 = threading.Thread(target=print_letters)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#5-savol
# class Product:
#     def __init__(self, name, price,color,image):
#         self.name = name
#         self.price = price
#         self.color = color
#         self.image = image
#
#
#     def save(self):
#         a = """insert into product(name,price,color,image) values (%s,%s,%s,%s)"""
#         data = (self.name, self.price,self.color, self.image)
#         cur.execute(a, data)
#         conn.commit()
#         cur.close()
#         conn.close()
#6-savol
# class DbConnect:
#     def __enter__(self):
#         self.conn = psycopg2.connect("dbname=mydatabase user=myuser password=mypassword")
#         self.cur = self.conn.cursor()
#         return self.conn, self.cur
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.cur.close()
#         self.conn.close()
#
# with DbConnect() as (conn, cur):
#     cur.execute("SELECT * FROM mytable")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
#7-savol
# import requests
#
# url = "https://dummyjson.com/products/"
# response = requests.get(url)
# data = response.json()
# print(data)
