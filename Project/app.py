
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
data = None
uploaded_file = st.file_uploader("Upload file CSV", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    st.warning("Vui lòng upload file CSV dữ liệu!")

if data is not None:
    # Làm sạch và mã hóa dữ liệu
    data_cleaned = data.dropna(subset=['ĐVT', 'Số lượng Nhập kho'])
    data_encoded = pd.get_dummies(data_cleaned, columns=['ĐVT'], drop_first=True)

    # Thêm các đặc trưng bổ sung để cải thiện dự đoán
    data_encoded['Tỷ lệ Xuất/Đầu kỳ'] = data_encoded['Số lượng Xuất kho'] / (data_encoded['Số lượng Đầu kỳ'] + 1e-5)
    data_encoded['Tỷ lệ Cuối/Đầu kỳ'] = data_encoded['Số lượng Cuối kỳ'] / (data_encoded['Số lượng Đầu kỳ'] + 1e-5)
    data_encoded['Số lượng Nhập khẩu'] = data_encoded['Số lượng Nhập kho'] - data_encoded['Số lượng Xuất kho']

    # Thêm đặc trưng liên quan đến giá trị
    data_encoded['Giá trị Đầu kỳ'] = data_cleaned['Giá trị Đầu kỳ']

    X = data_encoded[['Số lượng Đầu kỳ', 'Số lượng Xuất kho', 'Số lượng Cuối kỳ', 'Tỷ lệ Xuất/Đầu kỳ', 'Tỷ lệ Cuối/Đầu kỳ', 'Số lượng Nhập khẩu', 'Giá trị Đầu kỳ'] + 
                 [col for col in data_encoded.columns if 'ĐVT' in col]]

    y = data_encoded['Số lượng Nhập kho']

    # Chia tập dữ liệu
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Chuẩn hóa các đặc trưng
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Huấn luyện mô hình
    gb_model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=5, random_state=42)
    gb_model.fit(X_train_scaled, y_train)

    # Load lịch sử dự đoán nếu có
    history_file = 'prediction_history.csv'
    try:
        prediction_history = pd.read_csv(history_file)
        if prediction_history.empty:
            prediction_history = pd.DataFrame(columns=['ĐVT', 'Số lượng Đầu kỳ', 'Số lượng Xuất kho', 'Số lượng Cuối kỳ', 'Giá trị Đầu kỳ', 'Dự đoán'])
    except pd.errors.EmptyDataError:
        prediction_history = pd.DataFrame(columns=['ĐVT', 'Số lượng Đầu kỳ', 'Số lượng Xuất kho', 'Số lượng Cuối kỳ', 'Giá trị Đầu kỳ', 'Dự đoán'])

    st.sidebar.title("Trực quan hóa hoặc Dự đoán")
    choice = st.sidebar.selectbox("Chọn tính năng", ["Trực quan hóa", "Dự đoán", "Lịch sử"])

    # Trực quan hóa dữ liệu
    if choice == "Trực quan hóa":
        st.title("Trực quan hóa dữ liệu")

        # Chọn loại biểu đồ
        plot_type = st.selectbox("Chọn loại biểu đồ", [
            "Biểu đồ số lượng đầu kỳ và cuối kỳ", 
            "Biểu đồ cột về số lượng nhập kho",
            "Biểu đồ đường số lượng xuất kho", 
            "Biểu đồ Histogram số lượng cuối kỳ",
            "Top 5 đơn vị tính có giá trị xuất kho lớn nhất",
            "Top 10 đơn vị tính có số lượng xuất kho nhiều nhất",
        ])

        # Tạo biểu đồ
        if plot_type == "Biểu đồ số lượng đầu kỳ và cuối kỳ":
            fig = px.bar(data, x='ĐVT', y=['Số lượng Đầu kỳ', 'Số lượng Cuối kỳ'],  title="So sánh số lượng đầu và cuối kỳ theo đơn vị tính",)
            st.plotly_chart(fig)
        
        elif plot_type == "Biểu đồ cột về số lượng nhập kho":
            fig = px.bar(data, x='ĐVT', y='Số lượng Nhập kho', title='Biểu đồ cột về số lượng nhập kho')
            st.plotly_chart(fig)
        
        elif plot_type == "Biểu đồ đường số lượng xuất kho":
            fig = px.line(data, x='ĐVT', y='Số lượng Xuất kho', title="Biểu đồ Đường về số lượng xuất kho")
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig)

        elif plot_type == "Biểu đồ Histogram số lượng cuối kỳ":
            fig = px.histogram(data, x='Số lượng Cuối kỳ', title="Biểu đồ Histogram số lượng cuối kỳ")
            st.plotly_chart(fig)

        elif plot_type == "Top 5 đơn vị tính có giá trị xuất kho lớn nhất":
            top_5_items = data.nlargest(5, 'Giá trị Đầu kỳ')
            fig = px.bar(top_5_items, x='ĐVT', y='Giá trị Đầu kỳ', title="Top 5 đơn vị tính có giá trị xuất kho lớn nhất")
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig)

        elif plot_type == "Top 10 đơn vị tính có số lượng xuất kho nhiều nhất":
            top_items = data.nlargest(10, 'Số lượng Xuất kho')
            fig = px.bar(top_items, x='ĐVT', y='Số lượng Xuất kho', title="Top 10 đơn vị tính có số lượng xuất kho nhiều nhất")
            st.plotly_chart(fig)

    elif choice == "Dự đoán":
        st.title("Dự đoán số lượng nhập kho")

        # Dropdown để chọn ĐVT
        dv_list = data['ĐVT'].dropna().unique()
        selected_dvt = st.selectbox('Chọn đơn vị tính (ĐVT)', dv_list)

        # Các ô nhập liệu cho các đặc trưng
        dau_ky_so_luong = st.number_input('Số lượng Đầu kỳ', min_value=0, value=0)
        xuat_kho_so_luong = st.number_input('Số lượng Xuất kho', min_value=0, value=0)
        cuoi_ky_so_luong = st.number_input('Số lượng Cuối kỳ', min_value=0, value=0)
        gia_tri_dau_ky = st.number_input('Giá trị Đầu kỳ', min_value=0, value=0)

        # Tính các đặc trưng bổ sung
        ty_le_xuat_dau_ky = xuat_kho_so_luong / (dau_ky_so_luong + 1e-5)
        ty_le_cuoi_dau_ky = cuoi_ky_so_luong / (dau_ky_so_luong + 1e-5)
        so_luong_nhap_khau = dau_ky_so_luong - cuoi_ky_so_luong

        # Nút dự đoán
        if st.button('Dự đoán'):
            # Tạo DataFrame với dữ liệu đầu vào
            input_data = pd.DataFrame([[dau_ky_so_luong, xuat_kho_so_luong, cuoi_ky_so_luong, ty_le_xuat_dau_ky, ty_le_cuoi_dau_ky, so_luong_nhap_khau, gia_tri_dau_ky]], 
                                      columns=['Số lượng Đầu kỳ', 'Số lượng Xuất kho', 'Số lượng Cuối kỳ', 'Tỷ lệ Xuất/Đầu kỳ', 'Tỷ lệ Cuối/Đầu kỳ', 'Số lượng Nhập khẩu', 'Giá trị Đầu kỳ'])
            
            # Mã hóa one-hot cho ĐVT
            input_data['ĐVT'] = selected_dvt
            input_data_encoded = pd.get_dummies(input_data, columns=['ĐVT'], drop_first=True)
            
            # Định hình lại để phù hợp với các cột đã sử dụng khi huấn luyện
            input_data_encoded = input_data_encoded.reindex(columns=X_train.columns, fill_value=0)
            
            # Chuẩn hóa dữ liệu đầu vào
            input_data_scaled = scaler.transform(input_data_encoded)
            
            # Dự đoán với mô hình đã huấn luyện
            prediction = gb_model.predict(input_data_scaled)
            prediction = max(prediction[0], 0) # Đảm bảo dự đoán không âm
            prediction = round(prediction, 0)
            # Hiển thị kết quả dự đoán
            st.success(f"Dự đoán số lượng nhập kho cho quý tiếp theo của {selected_dvt} là: {prediction}")
            
            # Lưu kết quả dự đoán vào lịch sử
            new_entry = pd.DataFrame([[selected_dvt, dau_ky_so_luong, xuat_kho_so_luong, cuoi_ky_so_luong, gia_tri_dau_ky, prediction]],
                                     columns=['ĐVT', 'Số lượng Đầu kỳ', 'Số lượng Xuất kho', 'Số lượng Cuối kỳ', 'Giá trị Đầu kỳ', 'Dự đoán'])
            prediction_history = pd.concat([prediction_history, new_entry], ignore_index=True)

            prediction_history.index += 1
            prediction_history.to_csv(history_file, index=False)

    elif choice == "Lịch sử":
        st.title("Lịch sử dự đoán")
        if st.button('Xóa lịch sử dự đoán'):
            prediction_history = pd.DataFrame(columns=['ĐVT', 'Số lượng Đầu kỳ', 'Số lượng Xuất kho', 'Số lượng Cuối kỳ', 'Giá trị Đầu kỳ', 'Dự đoán'])
            prediction_history.to_csv(history_file, index=False)
            st.success('Đã xóa lịch sử dự đoán thành công!')
            st.write(prediction_history.reset_index(drop=True))
        elif not prediction_history.empty:
            st.write(prediction_history.reset_index(drop=True))
        else:
            st.write("Chưa có lịch sử dự đoán nào.")
