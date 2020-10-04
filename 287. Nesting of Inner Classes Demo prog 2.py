class Human:
    class Head:
        def talk (self):
            print('talking..')
            
        class Brain:
            def think (self):
                print('thinking.....')
Human().Head().talk()
Human().Head().Brain().think()