s = 'B4A1D3'
alpha=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alpha.append(ch)
    else:
        digits.append(ch)
output = ''.join(sorted(alpha)+sorted(digits))
print(output)
        