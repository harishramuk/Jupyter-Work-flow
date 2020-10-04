supermarket={'store1':
                     {'name':'HARRIS STORE',
                      'items':[{'name':'KF','quantity':100},
                               {'name':'RC','quantity':200},
                               {'name':'MC','quantity':300}]
                     },
             'store2':
                     {'name':'MANI BOOKS STORE',
                      'items':[{'name':'python','quantity':500},
                               {'name':'django','quantity':400},
                               {'name':'java','quantity':600}
                               ]
                      }
             }                

print(' Name of store1... ')
print(supermarket['store1']['name'])
print(supermarket.get('store1').get('name'))
print('The name of items present in store1...')
for x in supermarket['store1']['items']:
    print(x['name'])
    print('brand',x['name'],'is quantity',x['quantity'])
print('the no of django books in store2... ')
for x in supermarket['store2']['items']:
    if x['name']== 'django':
        
        print(x['quantity'])  
print('The name of  book and quantity,..')        
for x in supermarket['store2']['items']:
    print('name of book',x.get('name'),'quantity',x.get('quantity'))    
