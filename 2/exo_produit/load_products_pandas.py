import mysql.connector as mysql
import pandas as pd
import os
from sqlalchemy import create_engine


BASE_PATH = os.path.dirname(__file__)
CSV_FILE = os.path.join(BASE_PATH, 'Produits.csv')

df_products = pd.read_csv(CSV_FILE)

add_packing_type = ("INSERT INTO tb_packing_type "
                    "(packing_name) VALUES (%s)")

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


def get_dict(list, key):
    dict_produit = dict()
    for item in list:
        dict_produit = {key: {item[1]: item[0]}}
    print(dict_produit)
    return dict_produit


def load_packing(df, cnx):
    df_packing = pd.DataFrame(
        df['CONDITION'].unique(), columns=['packing_name'])
    df_packing.to_sql('tb_packing_type', con=cnx,
                      if_exists='append', index=None)


def load_product_type(df, cnx):
    df_product_type = pd.DataFrame(
        df['FAMILLE ARTICLE'].unique(), columns=['product_name_type'])
    df_product_type.to_sql('tb_product_type', con=cnx,
                           if_exists='append', index=None)


def load_product(df, cnx):
    df.to_sql('tb_product', con=cnx, if_exists='append', index=None)


try:

    from sqlalchemy import URL

    url_object = URL.create(
        "mysql+mysqlconnector",
        username="jcaldeira",
        password="jcaldeira#020408@",  # plain (unescaped) text
        host="192.168.56.101",
        database="simplon",
    )

    sqlEngine = create_engine(url_object, pool_recycle=3600)
    dbConnection = sqlEngine.connect()

    # load_packing(df_products, dbConnection)
    # load_product_type(df_products, dbConnection)

    query_pack = ("SELECT id_packing_type, packing_name FROM tb_packing_type")
    df_pack = pd.read_sql(query_pack, dbConnection)

    query_product_type = (
        "SELECT id_product_type, product_name_type FROM tb_product_type")
    df_prod_type = pd.read_sql(query_product_type, dbConnection)

    df_products['FAMILLE ARTICLE'] = df_products['FAMILLE ARTICLE'].apply(
        lambda x: int(df_prod_type.loc[df_prod_type['product_name_type']
                                       == x]['id_product_type'].values))

    df_products['CONDITION'] = df_products['CONDITION'].apply(
        lambda x: int(df_pack.loc[df_pack['packing_name']
                                  == x]['id_packing_type'].values))

    df_products['PU HT'] = df_products['PU HT'].str.replace(",", ".")

    df_products.rename(columns={'Code article': 'code_article',
                                'LIBELLE ARTICLE': 'product_name',
                                'FAMILLE ARTICLE': 'id_product_type',
                                'CONDITION': 'id_packing_type',
                                'PU HT': 'price'}, inplace=True)

    load_product(df_products, dbConnection)

    dbConnection.commit()

except Exception as e:
    dbConnection.rollback()
    print(e)
    # print(code, name,
    #       get_index_from_list(
    #           result_prod_type, product_type),
    #       get_index_from_list(
    #           result_pack, product_pack),
    #       price.replace(",", "."))
finally:
    dbConnection.close()
