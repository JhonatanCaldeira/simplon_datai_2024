import streamlit as st
from pymongo import MongoClient
import pprint


client = MongoClient()
db = client['scrapping-database']
collection = db['scrapy_quotes']

group_author = collection.aggregate([
    { "$group" : { "_id" : "$Author" } },
    { "$sort": { 'Author': 1 }}
])

author_list = []
for group in group_author:
    author_list.append(group["_id"])

select_author = st.selectbox('Select an Author: ', author_list)


random_document = collection.aggregate([
    {"$sample": {"size": 1}}
])

for document in random_document:
    st.title(document["Quote"])
    st.write(f'By {document["Author"]}')

client.close()