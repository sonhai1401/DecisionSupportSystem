
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Load data
data = pd.read_csv('quy2.csv')

# Làm sạch và tiền xử lý dữ liệu
data_cleaned = data.dropna(subset=['ĐVT', 'Số lượng Nhập kho'])
data_encoded = pd.get_dummies(data_cleaned, columns=['ĐVT'], drop_first=True)

# Thêm các đặc trưng bổ sung để dự đoán tốt hơn
data_encoded['Tỷ lệ Xuất/Đầu kỳ'] = data_encoded['Số lượng Xuất kho'] / (data_encoded['Số lượng Đầu kỳ'] + 1e-5)
data_encoded['Tỷ lệ Cuối/Đầu kỳ'] = data_encoded['Số lượng Cuối kỳ'] / (data_encoded['Số lượng Đầu kỳ'] + 1e-5)
data_encoded['Số lượng Nhập khẩu'] = data_encoded['Số lượng Nhập kho'] - data_encoded['Số lượng Xuất kho']
data_encoded['Giá trị Đầu kỳ'] = data_cleaned['Giá trị Đầu kỳ']

# Xác định các đặc trưng (features) và đích (target)
X = data_encoded[['Số lượng Đầu kỳ', 'Số lượng Xuất kho', 'Số lượng Cuối kỳ', 'Tỷ lệ Xuất/Đầu kỳ', 'Tỷ lệ Cuối/Đầu kỳ', 'Số lượng Nhập khẩu', 'Giá trị Đầu kỳ'] + 
                 [col for col in data_encoded.columns if 'ĐVT' in col]]
y = data_encoded['Số lượng Nhập kho']

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Chuẩn hóa các đặc trưng
# Công thức StandardScaler (xi-mean(x))/(stdev(x))
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Huấn luyện mô hình Gradient Boosting
gb_model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=5, random_state=42)
gb_model.fit(X_train_scaled, y_train)

# Dự đoán với mô hình đã huấn luyện
y_pred = gb_model.predict(X_test_scaled)

# Chuyển đổi dự đoán liên tục thành các danh mục để đánh giá
def categorize_values(values):
    return pd.cut(values, bins=[-np.inf, 300, 700, np.inf], labels=['Thấp', 'Trung bình', 'Cao'])

y_test_class = categorize_values(y_test)
y_pred_class = categorize_values(y_pred)

# Tạo ma trận nhầm lẫn
conf_matrix = confusion_matrix(y_test_class, y_pred_class)

# Vẽ ma trận nhầm lẫn
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt='g', 
            xticklabels=['Thấp', 'Trung bình', 'Cao'], yticklabels=['Thấp', 'Trung bình', 'Cao'])
plt.xlabel("Danh mục dự đoán")
plt.ylabel("Danh mục thực tế")
plt.title("Ma trận Nhầm lẫn")
plt.show()

# Tạo báo cáo phân loại
class_report = classification_report(y_test_class, y_pred_class, output_dict=True)
class_report_df = pd.DataFrame(class_report).transpose()

# Hiển thị báo cáo phân loại
print("# Báo cáo Phân loại")
print(class_report_df)


# Tính toán và hiển thị các chỉ số đánh giá
accuracy = accuracy_score(y_test_class, y_pred_class)
precision = precision_score(y_test_class, y_pred_class, average='weighted')
recall = recall_score(y_test_class, y_pred_class, average='weighted')
f1 = f1_score(y_test_class, y_pred_class, average='weighted')
specificity = (conf_matrix[0, 0] + conf_matrix[1, 1] + conf_matrix[2, 2]) / np.sum(conf_matrix)

# Công thức ma trận nhầm lẫn:
# Accuracy = (TP+TN)/(TP+TN+FP+FN)
# Precision = TP/(TP+FP)
# Recall = TP/(TP+FN)
# Specificity = TN/(TN+FN)
# F1 = 2*(Precision*Recall)/(Precision+Recall)

print("Các chỉ số đánh giá mô hình")
print(f"- Độ chính xác (Accuracy): {accuracy:.2f}")
print(f"- Độ chính xác (Precision): {precision:.2f}")
print(f"- Độ nhạy (Recall - Sensitivity or True Positive Rate): {recall:.2f}")
print(f"- Độ đặc hiệu (Specificity - True Negative Rate): {specificity:.2f}")
print(f"- F1-Score: {f1:.2f}")
