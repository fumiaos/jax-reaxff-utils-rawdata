from format_bracket import *
from format_th import convert_text
from togeo import convert_to_pdb
from totrain import to_train
# 将数据按行分割
with open('co0001.xyz', encoding='utf-8') as f:
    data = f.read()
data_lines = data.strip().split('\n')

# 调用函数处理数据
processed_lines = add_empty_line(data_lines)
print(get_num(data_lines))
num = int(get_num(data_lines))
# 将处理后的数据重新组合成字符串，并打印
processed_data = '\n'.join(processed_lines)
#print(type(processed_data))

# 调用函数并打印结果
output_text = convert_text(processed_data)
#print(output_text)

pdb_output = convert_to_pdb(output_text)
#print(pdb_output)
with open('geo', 'w', encoding='utf-8') as f:
    f.write(pdb_output)

train_output = to_train(output_text,num)
print(train_output)
with open('trainset.in', 'w', encoding='utf-8') as f:
    f.write(train_output)
