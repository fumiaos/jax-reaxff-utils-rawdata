def add_empty_line(data_lines):
    delimiter = data_lines[0]
    new_lines = []
    for i, line in enumerate(data_lines):
        if line.strip() == delimiter:
            new_lines.append("")
        new_lines.append(line)
        continue
        new_lines.append(line)
    return new_lines
def get_num(data_lines):
    return (data_lines[0])
if __name__ == '__main__':
    with open('co0001.xyz', encoding='utf-8') as f:
        data = f.read()
    data_lines = data.strip().split('\n')
    processed_lines = add_empty_line(data_lines)
    processed_data = '\n'.join(processed_lines)
    print(processed_data)
