#!/usr/bin/env python
# coding: utf-8

# In[2]:


#COMPOSITION -- HAS - A Relationship Demo program

class Sportsnews:
    def sportsinfo(self):
        print('sports info -1')
        print('sports info -2')
        print('sports info -3')
class Movienews:
    def movieinfo(self):
        print('movie info -1')
        print('movie info -2')
        print('movie info -3')
class Politicnews:
    def politicinfo(self):
        print('politic info -1')
        print('politic info -2')
        print('politic info -3')

class Htv:
    def __init__(self):
        self.sports= Sportsnews()
        self.movie= Movienews()
        self.politic= Politicnews()
    def getnews(self):
        print('Htv news')
        self.sports.sportsinfo()
        print()
        self.movie.movieinfo()
        print()
        self.politic.politicinfo()
h = Htv()
h.getnews()

# or another option 
print()
class H2tv:
    def __init__(self,sportsnews,movienews,politicnews):
        self.spn=sportsnews
        self.mon = movienews
        self.pon = politicnews
    def geth2tvnews(self):
        print('H2tv news...')
        print()
        self.spn.sportsinfo()
        print()
        self.mon.movieinfo()
        print()
        self.pon.politicinfo()
spn = Sportsnews()
mon = Movienews()
pon = Politicnews()
        
h2 = H2tv(spn,mon,pon)
h2.geth2tvnews()        


# In[ ]:





# In[ ]:




