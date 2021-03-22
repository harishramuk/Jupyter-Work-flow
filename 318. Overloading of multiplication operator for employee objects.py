class book:
    def __init__(self,page):
        self.page = page
    def __add__(self,other):
        total_page =self.page + other.page
        return total_page
b1 = book(100)
b2 = book(200)
b3 = book(300)
print(b1+b2)
print(b2+b3)


class student:
    def __init__ (self,name,mark):
        self.name = name
        self.mark = mark
    def __gt__ (self,other):
        gt_mark = self.mark > other.mark
        return gt_mark
    def __le__ (self,other):
        return self.mark <= other.mark
s1 = student('harrish',200)
s2 = student('vinoth',300)
print(s1 > s2)
print(s1 < s2)
print(s1<=s2)
print(s1 >= s2)