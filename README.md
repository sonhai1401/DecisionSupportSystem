# DecisionSupportSystem
📈 Hệ Thống Dự Báo Nhu Cầu Sản Phẩm Theo Quý
Dự án này xây dựng một hệ thống sử dụng mô hình Random Forest để dự báo nhu cầu sản phẩm (số lượng bán ra) theo quý, dựa trên dữ liệu bán hàng quá khứ. Hệ thống sử dụng giao diện Streamlit để người dùng nhập thông tin và trực quan hóa kết quả dự báo.

🚀 Tính năng chính
Dự báo số lượng bán ra cho từng danh mục sản phẩm, năm, và quý cụ thể.

Trực quan hóa nhu cầu trong quá khứ và đường dự báo.

Tự động lưu lịch sử các lần dự báo.

Cho phép xem và xóa lịch sử dự báo.

📁 Cấu trúc thư mục
├── app.py                      # Ứng dụng chính chạy bằng Streamlit
├── online_sales_dataset.csv   # Dataset đầu vào
├── forecast_history.csv       # File lưu lịch sử dự báo
├── requirements.txt           # Danh sách thư viện cần cài đặt
├── README.md                  # Tài liệu mô tả dự án
📊 Dữ liệu
File dữ liệu đầu vào: online_sales_dataset.csv gồm các cột chính:

InvoiceNo, InvoiceDate, Quantity, UnitPrice, Discount, ShippingCost, Category

Các trường này sẽ được xử lý và tổng hợp theo Quarter, Year, Category để tạo ra đặc trưng cho mô hình.
🧠 Mô hình học máy
Mô hình: RandomForestRegressor

Các đặc trưng đầu vào:

QuarterIndex, TotalRevenue, AvgDiscount, AvgShippingCost, TotalTransactions, Category (dưới dạng one-hot)

Được tối ưu bằng GridSearchCV trên tập huấn luyện.

🛠️ Cài đặt
1. Clone dự án
```bash
https://github.com/sonhai1401/DecisionSupportSystem.git
```
2. Tạo môi trường ảo (tuỳ chọn)
```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
```
3. Cài đặt thư viện
```bash
pip install -r requirements.txt
```
▶️ Chạy ứng dụng
```bash
streamlit run app.py
```
