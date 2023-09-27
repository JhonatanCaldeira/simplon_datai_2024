from sqlalchemy import create_engine
import mysql.connector as mysql
from sqlalchemy import URL
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url_object = URL.create(
    "mysql+mysqlconnector",
    username="jcaldeira",
    password="Brii#020408",  # plain (unescaped) text
    host="localhost",
    database="simplon",
)

sqlEngine = create_engine(url_object, pool_recycle=3600)
dbConnection = sqlEngine.connect()

sql = ("select p.product_name, tpt.packing_name, pt.product_name_type "
       "from tb_product p "
       "inner join tb_packing_type tpt on p.id_packing_type = tpt.id_packing_type "
       "inner join tb_product_type pt on p.id_packing_type = pt.id_product_type"
       )

df = pd.read_sql(sql, dbConnection)
arr_order = df['packing_name'].value_counts().index
my_plt = sns.countplot(data=df, y='packing_name', order=arr_order)
my_plt.set_xticklabels(my_plt.get_xticklabels(), rotation=90)
plt.show()


arr_order = df['product_name_type'].value_counts().index
my_plt = sns.countplot(data=df, y='product_name_type', order=arr_order)
my_plt.set_xticklabels(my_plt.get_xticklabels(), rotation=90)
plt.show()
