import os
import shutil

# 从name.txt读取要移动的文件名
with open('AssName.txt', 'r') as file:
    blk_files = [line.strip() for line in file]

# 创建test文件夹（如果它不存在）
os.makedirs('Eff_UI_Ass', exist_ok=True)

# 移动指定的文件到test文件夹
for blk_file in blk_files:
    source_path = os.path.join('00ass', blk_file)
    destination_path = os.path.join('Eff_UI_Ass', blk_file)
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
    else:
        print(f'{blk_file} does not exist in 00ass folder')

