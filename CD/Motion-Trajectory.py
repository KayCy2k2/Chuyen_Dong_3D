import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Tạo dữ liệu cho mô hình khối lập phương
side_length = 1.0
vertices = np.array([
    [0, 0, 0],
    [side_length, 0, 0],
    [side_length, side_length, 0],
    [0, side_length, 0],
    [0, 0, side_length],
    [side_length, 0, side_length],
    [side_length, side_length, side_length],
    [0, side_length, side_length]
])

# Tạo danh sách các điểm trong quỹ đạo chuyển động
num_frames = 3  # Số lượng hình ảnh trong quá trình chuyển động
trajectory = np.linspace(0, 2 * np.pi, num_frames)  # Đường đi theo quỹ đạo (ví dụ: đường tròn)

# Tạo plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vẽ khối lập phương ban đầu
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2])

# Vẽ quỹ đạo chuyển động của khối lập phương
for t in trajectory:
    # Tính toán ma trận xoay cho mỗi bước thời gian
    rotation_matrix = np.array([
        [np.cos(t), -np.sin(t), 0],
        [np.sin(t), np.cos(t), 0],
        [0, 0, 1]
    ])
    
    # Tính toán vị trí mới của các điểm dựa trên ma trận xoay
    transformed_vertices = np.dot(vertices, rotation_matrix)
    
    # Vẽ khối lập phương mới sau khi di chuyển
    ax.scatter(transformed_vertices[:, 0], transformed_vertices[:, 1], transformed_vertices[:, 2])
    plt.pause(1)  # Dừng 0.1 giây để hiển thị frame

plt.show()
