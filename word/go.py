#coding: utf-8
import pymongo
import string,re

import sys
reload(sys)
sys.setdefaultencoding('utf8')

client = pymongo.MongoClient("172.16.2.11", 27017)
dbOrg = client.get_database('job')
collection_dborg = dbOrg.get_collection('FiveJob')

clientL = pymongo.MongoClient("localhost", 27017)
dbStd = clientL.get_database('resumes')
collection_dbstd = dbStd.get_collection('Job58')

def addApplicantId(collection, objOrg):
    pattern = re.compile(u'(?<=/).+?(?=/)')
    _list = pattern.findall(objOrg["url"])
    if not _list:
        raise Exception(objOrg)
    insertObj = {}
    insertObj["ApplicantId"] = _list.pop()
    collection.update({"_id":objOrg["_id"]}, {"$set":insertObj})

def more():
    collection_dborg = dbOrg.get_collection('ResumeUrl')
    index = 0
    try:
        cursor = collection_dborg.find().skip(index)
        dbobj = cursor.next()
        while dbobj:
            addApplicantId(collection_dbstd, dbobj)

            index += 1
            dbobj = cursor.next()
    except Exception,e:
        print dbobj
        print e

    print index

more()

