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