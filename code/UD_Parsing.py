
# coding: utf-8

# In[2]:


from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://localhost:27017')
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)


# In[12]:


import stanfordnlp

nlp = stanfordnlp.Pipeline(lang ='es')


# In[51]:


db=client.bigdata_project
nws = db.raw_news.find()
#print(db.bigdata_project.count_documents({}))
for i in nws:
    processed ={}
    processed["title"]=i["title"]
    doc = nlp(i["text"])
    sentence_lst=[]
    for sent in doc.sentences:
        sentence_lst.append(sent.dependencies_string())
        #print(list(sent.dependencies))
    processed["UDP"]=sentence_lst        
    
    #print (processed)
    result = db.processed_news.insert_one(processed)

