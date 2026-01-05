def add_empty_line(data_lines):
    delimiter = data_lines[0]
    new_lines = []
    for i, line in enumerate(data_lines):
        if line.strip() == delimiter:
            new_lines.append("")  # 添加一个空行
        new_lines.append(line)  # 添加当前行
        continue
        new_lines.append(line)  # 添加剩余的行
    return new_lines
def get_num(data_lines):
    return (data_lines[0])
if __name__ == '__main__':
    # 原始数据，每个元素占一行
    with open('co0001.xyz', encoding='utf-8') as f:
        data = f.read()

    # 将数据按行分割
    data_lines = data.strip().split('\n')

    # 调用函数处理数据
    processed_lines = add_empty_line(data_lines)

    # 将处理后的数据重新组合成字符串，并打印
    processed_data = '\n'.join(processed_lines)
    print(processed_data)