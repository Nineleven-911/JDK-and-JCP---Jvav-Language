import os
import subprocess
import sys
import uuid


def generate_unique_filename(prefix='generated_', suffix='.class'):
    """生成一个唯一的文件名"""
    unique_id = uuid.uuid4()
    return f"{prefix}{unique_id}{suffix}"


def main():
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("Usage:jvav <input_file_path>")
        sys.exit(1)

    # 获取用户传入的文件路径
    input_file_path = sys.argv[1]

    # 确保文件路径存在
    if not os.path.isfile(input_file_path):
        print(f"Error: File not found at {input_file_path}")
        sys.exit(1)

    # 生成一个唯一的文件名
    output_filename = generate_unique_filename()
    output_file_path = os.getcwd()+"\\filegen\\"+output_filename

    # 获取jvavc.exe的路径
    jvavc_exe_path = os.path.join(os.getcwd(), 'jvavc.exe')

    # 确保jvavc.exe存在
    if not os.path.isfile(jvavc_exe_path):
        print(f"Error: jvavc.exe not found at {jvavc_exe_path}")
        sys.exit(1)

    # 调用jvavc.exe并传递参数
    try:
        subprocess.run([jvavc_exe_path, input_file_path, output_filename], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: jvavc.exe failed with error {e}")
        sys.exit(1)

    # 调用java命令执行生成的文件，并捕获输出
    try:
        # 注意：这里假设您的Java类不需要额外的类路径参数，
        # 如果需要，请使用-cp选项指定类路径
        result = subprocess.run(['java', output_filename.replace('.class', '')], capture_output=True, text=True,
                                check=True)
        print(result.stdout, end='')  # 打印Java程序的输出
    except subprocess.CalledProcessError as e:
        print(f"Error: java failed with error {e}")
    finally:
        # 无论Java程序是否成功执行，都删除生成的文件
        os.remove(output_file_path+".java")
        print(f"Deleted generated file: {output_file_path}")


main()
