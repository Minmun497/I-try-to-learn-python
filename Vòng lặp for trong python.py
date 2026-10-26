#Tính tổng 1! + 2! + ... + 10!
tong=0
for i in range(1,11):
    a=1
    for j in range(1,i+1):
                a =a*j
    tong = tong +a
print (tong)
# Tính tổng của 1 đến n! bất kì
n = int(input("Nhập n: "))
tong = 0
for i in range (1,n+1):
    a=1
    for j in range (1,i+1):
        a =a*j
    tong =tong +a
print(f"Tổng từ 1! đến {n}! là :{tong}")
#Tính n! bất kì
m = int(input("Nhập giá trị n: "))
l=1
for i in range (1,m+1):
      l *= i
print(f"{m}! bằng: {l}")
