# 导入必要的库和模块
from lxml import etree as et

# 设置XML解析器
parser = et.XMLParser()

# 读取并解析XML文件
with open("assets2.xml", "r", encoding='utf-8') as xml_file:
    xml_string = xml_file.read()
    xml_tree = et.fromstring(xml_string, parser)

xml_file = ["assets.xml", "assets2.xml"]

string_to_remove = "Z:\\blocks\\00\\"

# 创建一个空列表，用于储存原始路径
unique_paths_list = []

# 打开（或创建）一个文件，准备将满足条件的路径写入
with open("AssName.txt", "a") as output_file:
    # 便利每个XML文件
    for xml_file_name in xml_file:
        with open(xml_file_name, "r", encoding='utf-8') as xml_file:
            xml_string = xml_file.read()
            xml_tree = et.fromstring(xml_string, parser)
            # 遍历XML树中的所有Asset元素
            for asset in xml_tree.findall(".//Asset"):
                # 寻找每个Asset元素下的Name元素，并获取其文本内容
                asset_name = asset.find(".//Name").text
                # 检查资产名称是否以"Eff_UI_"开头
                if asset_name.startswith("Eff _UI_"):
                    print("素材名称:", asset_name)
                    # 寻找每个Asset元素下的OriginalPath元素，并获取其文本内容
                    asset_original_path = asset.find(".//OriginalPath").text
                    # 使用字符串替换方法去除指定字符串
                    cleaned_path = asset_original_path.replace(string_to_remove, "")
                    # 检查此路径是否已经记录（不在unique_paths_list中）
                    if cleaned_path not in unique_paths_list:
                        # 如果不在列表中，将其添加到列表
                        unique_paths_list.append(cleaned_path)
                        # 将路径写入到输出文件中
                        output_file.write(cleaned_path + '\n')
