import os

def count_python_lines(directory):
    """
    Recursively count the total number of lines in all Python files in the directory
    
    :param directory: Directory path to count
    :return: Total number of lines, total number of characters
    """
    total_lines = 0
    total_lens = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        total_lines += len(lines)
                        total_lens += sum(len(line) for line in lines)
                        print(f"{file_path}: {len(lines)} lines, {sum(len(line) for line in lines)} chars")
                except Exception as e:
                    print(f"Cannot read file {file_path}: {e}")
    return total_lines, total_lens

if __name__ == "__main__":
    target_dir = input("请输入要统计的目录路径: ")
    if os.path.isdir(target_dir):
        total = count_python_lines(target_dir)
        print(f"\n总计: {total[0]} 行 Python 代码， {total[1]} Python 字符")
        
    else:
        print("错误: 指定的路径不是一个有效目录")