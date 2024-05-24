# import re

# # 读取boundary文件中的内容
# boundary_path = 'constant/polyMesh/boundary'
# with open(boundary_path, "r") as file:
#     boundary_content = file.read()

# # 使用正则表达式匹配wing段落中的信息
# pattern = r'wing\s*{\s*type\s*([^\n]+);\s*inGroups\s*([^\n]+);\s*nFaces\s*([^\n]+);\s*startFace\s*([^\n]+);\s*}'
# match = re.search(pattern, boundary_content)

# if match:
#     wing_type = match.group(1).strip()
#     in_groups = match.group(2).strip()
#     n_faces = int(match.group(3).strip())
#     start_face = int(match.group(4).strip())

#     print("Wing Type:", wing_type)
#     print("In Groups:", in_groups)
#     print("Number of Faces:", n_faces)
#     print("Start Face:", start_face)
# else:
#     print("No match found.")

# # 讀取 faces 文件中的內容
# faces_path = 'constant/polyMesh/faces'
# with open(faces_path, "r") as file:
#     faces_content = file.read()

# # 使用正则表达式匹配所有括号对 () 之间的数据
# pattern = r'\(\s*([^()]+)\s*\)'
# faces_matches = re.findall(pattern, faces_content)

# if faces_matches:
#     # 将数据存储到列表中
#     all_faces = []
#     for match in faces_matches:
#         values = list(map(int, match.split()))
#         all_faces.append(values)
# else:
#     print("No matches found.")
# surface_faces = all_faces[start_face:start_face+n_faces]

# lst = []
# for sublist in surface_faces:
#     for item in sublist:
#         if item not in lst:
#             lst.append(item)

# points_path = 'constant/polyMesh/points'
# with open(points_path, 'r') as file:
#     points_content = file.read()
# points_matches = re.findall(pattern, points_content)
# if points_matches:
#     all_points = []
#     for match in points_matches:
#         values = list(map(float, match.split()))
#         all_points.append(values)
# else:
#     print('No matches found.')

# surface_points = []
# for item in lst:
#     value = all_points[item] # 在 lst1 中查找第二个元素的索引
#     surface_points.append(value)

# # 将列表内容写入文件
# write_path = 'system/include/surface_pts'
# with open(write_path, 'w') as file:
#     file.write("pts\n(\n")  # 写入前兩行
#     for sublist in surface_points:
#         file.write('(' + ' '.join(map(str, sublist)) + ')\n')  # 写入每个子列表，并在末尾添加换行符
#     file.write(');') #寫入最後一行
# print(f'Write the surface points in {write_path} file.')

# boundaryProbes to Validate
import numpy as np
x_min, x_max = -0.05, 1.25
z_min, z_max = -0.075, 0.075
y_min, y_max = 0, 1
res = 128

x_values = np.linspace(x_min, x_max, res)
z_values = np.linspace(z_min, z_max, res)
y_values = np.linspace(y_min, y_max, res)

write_path_AIP = 'system/include/AIP'
with open(write_path_AIP, 'w') as file:
    file.write("pts\n(\n")
    for z in z_values:
        for y in y_values:
            y *= 1.1963
            for x in x_values:
                file.write(f"({x} {y} {z})\n")
    file.write(");")
print(f'Write the surface points in {write_path_AIP} file.')