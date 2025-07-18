#DICTIONARY

thedict={"brand":"Ford","model":"mustang","year":1964}
print(thedict["brand"])#prints Ford
thedict={"brand":"Ford","model":"mustang","year":1964,"year":2024,"electric":"False"}
print(thedict)#dict.can't have 2 items with the same key
len(thedict)
my_dict={'key1':'value1','key2':'value2'}
my_dict['key2']#call values by their keys
my_dict={'key1':[123],'key2':[22,25,29],'key3':['type0','type1','type2']}
my_dict['key3']
my_dict['key1'][0]#CALL BY INDEX VALUE of list<dict-not index
my_dict['key3'][0].upper()

d={}
d['animal']='goat'
d['birds']='parrot','peacock'
d

f={'key1':25,'key2':89,'key3':45}
f.keys()
f.values()
f.items()


thedict={"brand":"Ford","model":"mustang","year":1964}
for k,v in thedict.items() :
    print(k,":",v)

    A={'name':'jasna','place':'kattuppara','center':'beat',}
    for key, value in A.items():
        print(key,":",value)

d={}
d["cat"]=["a small animal"]
d["table"]=["a piece of furniture","list of facts&figures"]     
d

sub={"python","java","c++","python","javascript","java","python","java","c++","c"}
sub