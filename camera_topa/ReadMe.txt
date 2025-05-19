 
2. Machine Learning / Deep Learning
Dữ liệu cần có: Hình ảnh mặt hồ có và không có cám, được gán nhãn (label).
Mô hình có thể dùng:
Classification: Có cám hay không.
Object Detection: Xác định vị trí cám (YOLO, SSD, Faster R-CNN).
Segmentation: Phân vùng chính xác vùng cám (U-Net, DeepLab).

 Quy trình triển khai:
Thu thập dữ liệu: Ảnh hoặc video mặt hồ từ camera.
Tiền xử lý: Cắt ảnh, cân bằng sáng, tăng cường dữ liệu.
Huấn luyện mô hình: Dùng TensorFlow, PyTorch, hoặc các công cụ AutoML.
Triển khai mô hình: Nhúng vào hệ thống giám sát hoặc phân tích video theo thời gian thực.

 Công cụ gợi ý:
OpenCV: Xử lý ảnh cơ bản.
YOLOv5/YOLOv8: Phát hiện vật thể nhanh, chính xác.
LabelImg: Gán nhãn dữ liệu.
Roboflow: Tạo và huấn luyện mô hình dễ dàng.
