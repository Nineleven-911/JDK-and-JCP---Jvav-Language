def add_to_jvavkeys(key_value_pair):
    # 格式化输入，确保逗号两边有空格
    formatted_pair = f"{key_value_pair.split(',')[0].strip()} , {key_value_pair.split(',')[1].strip()}"

    file_path = 'jvavkeys.cfg'
    try:
        with open(file_path, 'r') as file:
            # 读取文件内容，并去除每行末尾的换行符
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # 如果文件不存在，则视为空列表
        lines = []

    # 检查格式化后的键值对是否已经存在
    if formatted_pair in lines:
        print(f"Key-value pair '{formatted_pair}' already exists in {file_path}.")
        return False  # 表示没有添加新内容

    # 追加新内容到文件末尾
    with open(file_path, 'a') as file:
        # 如果文件不是空的，我们先添加一个逗号和一个空格（为了保持格式一致）
        if lines:
            file.write(' , ')
        # 写入新的格式化后的键值对（不带换行符，因为下次追加时我们会自动添加）
        file.write(formatted_pair)

    return True  # 表示添加了新内容


while True:
    user_input = input("Enter key-value pair (e.g., 'a , b'): ").strip()
    # 检查输入是否包含逗号
    if ',' in user_input:
        if add_to_jvavkeys(user_input):
            print(f"Added formatted key-value pair to jvavkeys.cfg.")
    else:
        print("Invalid input. Please enter a key-value pair separated by a comma.")
