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
    x = {"shortcode": shortcode}
    m = list(col.find(x))
    data = {'shortcode': m[0]['shortcode'], 'name': m[0]['prod_name'], 'price': m[0]['price']}

    return json.dumps(data)

