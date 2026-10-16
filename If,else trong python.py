# Dạng 1 if đơn
n = float(input("Nhap chieu cao: "))

if (n<=160):
    print ("May lun vl")

# Dạng 2 if...else
tuoi = int(input("Nhập tuổi người dùng : "))
if tuoi >= 18:
   print("Đủ tuổi lái xe")
else :
    print("Chưa đủ tuổi lái xe")

# Dạng 3 if elif else 
a = int(input("Nhập kích thước sản phẩm (mm): "))
if a>=100:
    print("Loại A-Lớn")
elif a>=50:
    print("Loại B-Vừa")
elif a>=20:
    print("Loại C-Nhỏ")
else:
    print("NG-Quá nhỏ")

weight = float(input("Nhập cân nặng (kg) : "))
height = float(input("Nhập chiều cao (m) : "))
BMI = weight / height**2 
if BMI >= 35:
    print("Quá béo")
elif BMI>=30:
    print("Béo")
elif BMI>=25:
    print("Hơi béo")
elif BMI>=18.5:
    print("Bình thường")
elif BMI>=16:
    print("Hơi gầy")
elif BMI>=15:
    print("Gầy")
else:
    print("Quá gầy")

print(f"Chỉ số BMI của bạn :{BMI}")