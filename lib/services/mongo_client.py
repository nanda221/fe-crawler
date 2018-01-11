import pymongo


def connect(host='localhost', port=27017):
    return pymongo.MongoClient(host, port)
