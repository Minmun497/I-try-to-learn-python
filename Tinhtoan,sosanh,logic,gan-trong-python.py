""" 
Vé tàu lượn siêu tốc
Một công viên giải trí quy định điều kiện để một bạn nhỏ được vào chơi tàu lượn siêu tốc như sau:

Bạn nhỏ phải từ 10 tuổi trở lên (tuoi >= 10).

Chiều cao sau khi cộng thêm đế giày phải từ 130 cm trở lên.

Nếu chiều cao chưa đủ 130 cm nhưng đã đạt tối thiểu 120 cm, bạn nhỏ vẫn được chơi nếu có người lớn đi kèm.
"""
tuoi = 14
chieu_cao = 118
de_giay=3
nguoi_lon_di_kem = False

chieu_cao_tong = chieu_cao + de_giay

du_tuoi = tuoi >=11
thoa_man = (chieu_cao_tong>= 130) or (chieu_cao_tong <130 and nguoi_lon_di_kem == True)
duoc_len_tau = du_tuoi and thoa_man

print ("Chiều cao tổng = ",chieu_cao_tong)
print ("Đủ tuổi :",du_tuoi)
print ("Đủ chiều cao hoặc không đủ chiều cao và có người đi cùng :",thoa_man)
print ("Được lên xe :",duoc_len_tau)