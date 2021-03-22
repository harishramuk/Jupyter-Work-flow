class book:
    def __init__(self,page):
        self.page = page
    def __add__(self,other):
        return book(self.page + other.page)
    def __str__(self):
        return 'total no of pages:{}'.format(self.page)
    def __mul__(self,other):
        return book(self.page * other.page)
    def __sub__(self,other):
        return book(self.page - other.page)
b1=book(100)
b2=book(200)
b3=book(500)
print(b1+b2+b3)
print(b1*b2+b3)
print(b1-b2+b3)