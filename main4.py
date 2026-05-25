print("--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN CẤP CỨU ---")

full_name = input("Nhập Mã bệnh nhân (Ví dụ: BN999): ")

temperature = float(input("Nhập Nhiệt độ cơ thể (Ví dụ: 37.5): "))

heart_rate = int(input("Nhập Nhịp tim (Ví dụ: 85): "))

print("\n" + "="*40 + "\n") 

print("--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print(f"Mã bệnh nhân: {full_name}")
print(f"Nhiệt độ cơ thể: {temperature} độ C")
print(f" => Kiểu dữ liệu hệ thống ghi nhận: {type(temperature)}")

print(f"Nhịp tim: {heart_rate} nhịp/phút")
print(f" => Kiểu dữ liệu hệ thống ghi nhận: {type(heart_rate)}")

print("-" * 35)
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")

# Khi dùng hàm input() trong Python để nhập dữ liệu từ bàn phím, 
# tất cả dữ liệu nhận vào mặc định đều là kiểu chuỗi (String). 
# Nhiệm vụ của chúng ta là phải chuyển nó về đúng kiểu số.