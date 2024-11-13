# DecisionSupportSystem
Ứng dụng dự đoán và trực quan hóa nhu cầu sản phẩm
hệ thống dự báo nhu cầu sản phẩm được xây dựng bằng thư viện Streamlit của Python. Hệ thống sử dụng mô hình hồi quy Random Forest để dự đoán số lượng sản phẩm sẽ được bán trong tương lai dựa trên dữ liệu bán hàng lịch sử.

Chuẩn bị dữ liệu:

Lưu trữ file dữ liệu bán hàng lịch sử của bạn trong định dạng CSV với tên online_sales_dataset.csv.
Đặt file CSV cùng thư mục với script Python của bạn.
Cấu trúc dữ liệu trong file CSV cần tuân theo định dạng được mô tả trong code (các cột như InvoiceDate, Quantity, UnitPrice, Discount, ShippingCost, InvoiceNo, Category).
Chạy ứng dụng

Chạy script Python bằng lệnh:

Bash
python script_name.py
Hãy thận trọng khi sử dụng các đoạn mã.

Truy cập ứng dụng web bằng cách mở trình duyệt web và gõ địa chỉ: http://localhost:8501/

Chức năng

Ứng dụng cung cấp hai chức năng chính:

Dự báo và trực quan hóa:
Chọn năm, quý và danh mục sản phẩm để thực hiện dự báo.
Xem hệ số R-squared và RMSE của mô hình để đánh giá độ chính xác.
Dự báo nhu cầu cho quý đã chọn.
Xem biểu đồ so sánh giữa dữ liệu lịch sử và dự báo cho danh mục đã chọn.
Xem lịch sử dự báo:
Xem lại các dự báo đã thực hiện trước đó.
Xóa lịch sử dự báo nếu cần.
Mô tả chi tiết về code

Script thực hiện các bước tiền xử lý dữ liệu như:
Chuyển đổi định dạng ngày tháng.
Tạo các đặc trưng mới (Revenue, DayOfWeek, Month, Year, Quarter).
Thực hiện tổng hợp dữ liệu theo danh mục, năm và quý.
Thêm các đặc trưng bổ sung (QuarterIndex, QuarterLabel).
Tạo biến giả cho các danh mục sản phẩm.
Chuẩn hóa dữ liệu.
Script chia tập dữ liệu thành tập huấn luyện và tập test.
Script sử dụng GridSearchCV để tìm kiếm tham số tối ưu cho mô hình Random Forest.
Script huấn luyện mô hình Random Forest với tham số tối ưu.
Script dự đoán nhu cầu trên tập test và tính toán các chỉ số đánh giá mô hình (R-squared, RMSE).
Script sử dụng Streamlit để tạo giao diện người dùng web.
Người dùng có thể lựa chọn chức năng mong muốn.
Người dùng có thể nhập thông tin để dự báo nhu cầu cho một danh mục sản phẩm cụ thể trong một quý cụ thể.
Ứng dụng hiển thị kết quả dự báo và biểu đồ so sánh với dữ liệu lịch sử.
Người dùng có thể xem lại lịch sử dự báo và xóa lịch sử nếu cần.
Lưu ý

Đây là một ví dụ cơ bản và có thể cần điều chỉnh để phù hợp với dữ liệu và nhu cầu cụ thể của bạn.
Mô hình Random Forest được sử dụng trong ví dụ này. Bạn có thể thử nghiệm với các mô hình khác để tìm ra mô hình phù hợp nhất cho dữ liệu của mình.
Những cải tiến tiềm năng

Cho phép người dùng tải lên file dữ liệu của riêng họ.
Thêm các tùy chọn cấu hình cho mô hình.
Tích hợp với các công cụ trực quan hóa khác.
Cải thiện giao diện người dùng.
Thử nghiệm với các kỹ thuật tiền xử lý dữ liệu, chọn lọc đặc trưng và điều chỉnh siêu tham số của mô hình để nâng cao độ chính xác dự báo.
Triển khai ứng dụng lên nền tảng cloud.
