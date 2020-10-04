def factorial(num):
    result=0
    while num>=1:
        result = result+num
        num = num-1
    return result
print(factorial(5))
