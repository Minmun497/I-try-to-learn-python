#Tính tổng 1! + 2! + ... + 10!
tong=0
for i in range(1,11):
    a=1
    for j in range(1,i+1):
                a =a*j
    tong = tong +a
print (tong)

