# 本代码目的在于从train.txt文件中的4w条训练语句中按照3：1比例分为新的训练集和验证集

def make_train_dev():
    num = 10000
    train = open('train.txt','w',encoding='utf-8')
    dev = open('dev.txt','w',encoding='utf-8')
    with open('train_source.txt','r',encoding='utf-8') as file:
        i = 0
        data = file.readline()
        while data:
            if data == '\n':
                i += 1

            if i >= 9999:
                train.write(data)
            else:
                dev.write(data)
            data = file.readline()
        train.close()
        dev.close()
        file.close()

make_train_dev()