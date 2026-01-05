# 定义原始数据
data = """

"""
def to_train(data,num):
    # 将数据按行分割
    lines = data.strip().split('\n')
    output = ""
    # 初始化一个空列表来存储能量值
    energies = []

    # 遍历每一行，提取能量值
    for line in lines:
        if "E =" in line:
            # 提取能量值并转换为浮点数
            energy = line.split('E =')[1].strip()
            energies.append(energy)

    print(energies)
    # 输出结果
    for i, energy in enumerate(energies, start=1):
        #print(f"CoO_{i} E={energy}")
        #print(i)
        #print(2**i)
        rel_E = 1+(float(energies[i-1])/(num)-float(energies[0])/num)*627.509474
        if i ==1:
            pass
        else:
            output+=(f" 1.00  +   co0001_{i}/{num}   -   co0001_1/{num}                                      {rel_E}\n")
    return output
    # 1.00  +   hsh-SH1.15/1   -   hshBase/1                                      15.98476


