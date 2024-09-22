# 打开配置文件并读取内容
f = open("jvavkeys.cfg", "r")
mapping = {}
# 读取文件内容，并按逗号分隔（注意逗号后可能有空格，所以使用strip()）
a = [item.strip() for item in f.read().split(",")]
f.close()

# 创建键值对映射
for i in range(0, len(a), 2):  # 步长为2，因为每两个元素是一个键值对
    key = a[i]
    value = a[i + 1] if i + 1 < len(a) else ""  # 确保不会越界
    mapping[value] = key
    print("Mapped Key - Java:", key, " Jvav:", value)