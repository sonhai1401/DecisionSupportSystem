# DecisionSupportSystem
Ứng dụng Dự đoán và Trực quan hóa Dữ liệu Kho Hàng
Ứng dụng này được xây dựng bằng Streamlit, Pandas, Scikit-learn, và Plotly. Nó hỗ trợ người dùng trực quan hóa, dự đoán và duy trì lịch sử các dự đoán về dữ liệu kho hàng, giúp quản lý kho hiệu quả hơn.

Tính năng
Ứng dụng cung cấp ba chức năng chính:

Trực quan hóa dữ liệu: Cho phép người dùng trực quan hóa dữ liệu kho hàng với nhiều loại biểu đồ khác nhau.
Dự đoán: Dự đoán số lượng nhập kho trong tương lai dựa trên các chỉ số tồn kho hiện có.
Lịch sử dự đoán: Lưu và hiển thị lịch sử tất cả các dự đoán trước đó.
Hướng dẫn sử dụng
1. Tải dữ liệu lên
Ứng dụng yêu cầu người dùng tải lên một file CSV chứa dữ liệu kho hàng. Định dạng file phải có các cột dữ liệu cơ bản như:

ĐVT: Đơn vị tính
Số lượng Đầu kỳ: Số lượng tồn đầu kỳ
Số lượng Xuất kho: Số lượng xuất kho
Số lượng Cuối kỳ: Số lượng tồn cuối kỳ
Giá trị Đầu kỳ: Giá trị tồn đầu kỳ
2. Trực quan hóa dữ liệu
Chọn loại biểu đồ muốn hiển thị từ menu và ứng dụng sẽ tự động tạo biểu đồ tương ứng.
Các tùy chọn biểu đồ bao gồm biểu đồ cột, biểu đồ đường, biểu đồ histogram, và các biểu đồ top 5 hoặc top 10.
3. Dự đoán số lượng nhập kho
Nhập các giá trị như số lượng đầu kỳ, số lượng xuất kho, số lượng cuối kỳ và giá trị đầu kỳ.
Ứng dụng sẽ dựa trên các chỉ số này để dự đoán số lượng nhập kho cho kỳ tới bằng mô hình Gradient Boosting Regressor.
4. Xem và quản lý lịch sử dự đoán
Tính năng này lưu lại tất cả các dự đoán đã thực hiện để người dùng xem lại khi cần.
Người dùng cũng có thể xóa toàn bộ lịch sử dự đoán nếu cần.
