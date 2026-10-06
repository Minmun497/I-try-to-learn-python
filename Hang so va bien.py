
#Tim a,b khi biet tong va hieu
S = int (input("Nhap tổng S : "))
D = int (input("Nhap hiệu D : "))

a=int( (S + D)/2 )
b=int( (S - D)/2 )

print("a = ",a ,", b = " ,b)

#Tim c,d khi biet tong va ti so 
TONG =float(input ("Nhập tổng : "))
TI_SO =float(input ("Nhập tỉ số : "))

d= TONG/(TI_SO +1)
c= d*TI_SO

print("c = ",c ,", d = " ,d)

