#Tính tổng số chia hết cho 5 từ 10 đến 100
tong=0
i=10
while (i<=100) :
    if i%5==0:
        tong+=i
    i+=1
print(f"Tổng các số chia hết cho 5 từ 10 đến 100 là: {tong}")

#Tìm số đầu tiên chia hết cho n mà lớn hơn 12
n =int(input("Nhập số n: "))
while n == 0:
    n =int(input("Nhập lại số n(n khac 0): "))
i=13
while (i>12):
    if i%n==0 :
        print(f"Số đầu tiên lớn hơn 12 chia hết cho n là: {i}")
        break
    i+=1