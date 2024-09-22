import os
import sys

print("Jvav Compiler is Running.")

# 打开配置文件并读取内容
with open("jvavkeys.cfg", "r") as f:
    # 读取文件内容，并按逗号分隔（注意逗号后可能有空格，所以使用strip()）
    a = [item.strip() for item in f.read().split(",")]

# 创建键值对映射，从Java关键词到Jvav关键词
mapping = {}
for i in range(0, len(a), 2):  # 步长为2，因为每两个元素是一个键值对
    java_key = a[i]
    jvav_value = a[i + 1] if i + 1 < len(a) else ""  # 确保不会越界
    mapping[jvav_value] = java_key

# 获取.java文件的位置
java_file = sys.argv[1]
# 获取输出文件名（不包含扩展名），如果提供了的话；如果没有提供，则使用默认名称
output_file_name = sys.argv[2] if len(sys.argv) > 2 else "output"
# 自动添加.jvav扩展名（如果尚未添加）
if not output_file_name.endswith(".java"):
    output_file_name += ".java"

# 初始化一个空字符串来存储替换后的结果
decompiled_content = ""

# 打开指定的.java文件并读取内容
with open(java_file, "r") as f:
    java_content = f.read()
    # 拆分文本为行列表
    lines = java_content.split('\n')
    # 初始化一个空列表来存储替换后的每一行
    decompiled_lines = []
    # 遍历每一行进行替换，并打印替换信息
    for line in lines:
        # 拆分行为单词列表
        words = line.split()
        # 替换单词并收集替换信息
        replaced_words = []
        for word in words:
            java_word = mapping.get(word, word)
            if java_word != word:
                print(f"Replaced '{word}' with '{java_word}'")  # 打印替换信息
            replaced_words.append(java_word)
        # 重新组合行
        replaced_line = ' '.join(replaced_words)
        # 添加替换后的行到列表中
        decompiled_lines.append(replaced_line)
    # 将替换后的行列表重新组合为一个多行字符串
    decompiled_content = '\n'.join(decompiled_lines)

# 输出替换后的结果到指定的.java文件
output_dir = os.getcwd() + "\\filegen\\"
os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在
with open(output_dir + output_file_name, "w+") as f:
    f.write(decompiled_content)

print("Compile Complete.")