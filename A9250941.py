input('按Enter後輸入數字(a)'); a = int(input())
input('按Enter後輸入數字(b)'); b = int(input())

r = 0
r = a - b * int(float(a) / b)
while not r == 0:
    a = b
    b = r
    r = a - b * int(float(a) / b)
    
print("GCD=", end='', flush=True)
print(b)
