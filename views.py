import pymongo
import json
ipaddress = ''

'''Mongo connection'''
mongo = pymongo.MongoClient(maxPoolSize=50, connect=False)
'''------------'''

'''MongoDb Database and collections'''
db = pymongo.database.Database(mongo, 'KIRANA')
col = pymongo.collection.Collection(db, 'product_data')

def ini_ip(ipx):
    global  ipaddress
    ipaddress = ipx
    return ipx


def database(shortcode):
    m = list(col.find({"shortcode":shortcode}))
    data = { "name" : "ayur",
             "price": "20"}

    data = json.dumps(data)

    return data


