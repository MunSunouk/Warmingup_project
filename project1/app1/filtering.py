import pandas as pd

def have_filter(data, have_list):
    data = data # 전처리 된 데이터셋
    have_list = have_list
    
    idx_list=[]
    for i in have_list:
        idx_list.append(data[(data['재료명'].str.startswith(i))|(data['재료명'].str.endswith(i))])

    idx = idx_list[0]

    for i in range(1,len(idx_list)):
        idx_ = idx_list[i]
        idx = pd.concat([idx, idx_])

    data = idx.reset_index()
    data.drop('index',axis=1, inplace=True)
    print(data.head(30))

    return data

def noeat_filter(data, noeat_list):
    data = data # 전처리 된 데이터셋
    noeat_list = noeat_list
    
    idx_list=[]
    for i in noeat_list:
        idx_list.append(data[(data['재료명'].str.startswith(i))|(data['재료명'].str.endswith(i))])

    idx = idx_list[0]

    for i in range(1,len(idx_list)):
        idx_ = idx_list[i]
        idx = pd.concat([idx, idx_])

    print(len(idx))
    print(len(data))

    idx_num = idx['재료명'].index
    data.drop(idx_num, inplace=True)
    print(len(data))
    print(data.head(30))

    return data

data = pd.read_csv('../../data/레시피_김준민/레시피+재료정보_김준민.csv', encoding='cp949')

ingre_str = '-쌀,-금,-새우,-버섯,-멸치,감자,고구마,안심,마늘,계란,콩'
ingre_list = ingre_str.split(',')

noeat_list = []
have_list = []
for i in ingre_list:
    if i.startswith('-'):
        i = i.replace('-','')
        noeat_list.append(i)
    else:
        have_list.append(i)

print(noeat_list)
print(have_list)
noeat_filter(data, noeat_list)
have_filter(data,have_list)
