import mysql.connector as mysql
import pandas as pd
import os

BASE_PATH = os.path.dirname(__file__)
CSV_FILE = os.path.join(BASE_PATH, 'Produits.csv')

df_products = pd.read_csv(CSV_FILE)


add_product_type = ("INSERT INTO tb_product_type "
                    "(product_name_type) VALUES (%s)")

add_product = ("INSERT INTO tb_product"
               "(id_product, product_name, price, id_product_type,id_packing_type) "
               "VALUES (%s,%s,%s,%s,%s)")


def execute_query(cursor, exec_query, param=None):
    cursor.execute(exec_query, param)
    return cursor.fetchall()


def get_index_from_list(list, value):
    for item in list:
        if (item[1] == value):
            return item[0]


def load_packing():
    for p_type in df_products['CONDITION'].unique().tolist():
        add_packing_type = ("INSERT INTO tb_packing_type "
                            "(packing_name) VALUES (%s)")

        cursor.execute(add_packing_type, (p_type,))


def load_product_type():
    for p_type in df_products['FAMILLE ARTICLE'].unique().tolist():
        cursor.execute(add_product_type, (p_type,))


try:
    cnx = mysql.connect(user='jcaldeira', password='Brii#020408',
                        host='127.0.0.1',
                        database='simplon')
    cursor = cnx.cursor()

    query_pack = ("SELECT id_packing_type, packing_name FROM tb_packing_type")
    result_pack = execute_query(cursor, query_pack)

    query_product_type = (
        "SELECT id_product_type, product_name_type FROM tb_product_type")
    result_prod_type = execute_query(cursor, query_product_type)

    for code, name, product_type, product_pack, price in df_products.values.tolist():
        try:
            cursor.execute(add_product, (code, name, price.replace(",", "."),
                                         get_index_from_list(
                result_prod_type, product_type),
                get_index_from_list(
                result_pack, product_pack),
            ))
        except Exception as e:
            print(e)

    cnx.commit()

except Exception as e:
    cnx.rollback()
    print(e)
    print(code, name,
          get_index_from_list(
              result_prod_type, product_type),
          get_index_from_list(
              result_pack, product_pack),
          price.replace(",", "."))
finally:
    cursor.close()
    cnx.close()
