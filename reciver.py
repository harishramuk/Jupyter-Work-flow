import pickle
with open('emp.det','rb') as f:
    print('De-serialization emp objects are printed....')
    
    while True:
        try:
            obj = pickle.load(f)
            obj.display1()
        except EOFError:
            print('all employee read complete...')
            break