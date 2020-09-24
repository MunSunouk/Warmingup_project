import pandas as pd
import numpy as np

# data : 재료 데이터, noeat_list : 안먹는 리스트
def noeat_filter(data, noeat_list):
    noeat_data = data.copy() # 전처리 된 데이터셋
    noeat_list = noeat_list
    
    idx_list=[]
    for i in noeat_list:
        idx_list.append(noeat_data[(noeat_data['재료명'].str.startswith(i))|(noeat_data['재료명'].str.endswith(i))])

    # print(idx_list)

    idx = np.sort(pd.concat(idx_list)['레시피 코드'].unique().tolist())
    # print(idx)

    # data_noteat = []
    noeat_data = noeat_data[~noeat_data['레시피 코드'].isin(idx)]

    return noeat_data

# 안먹는 재료 걸러넨 데이터와 먹는 재료
def have_filter(data, have_list):
    have_data = data.copy() # 전처리 된 데이터셋
    have_list = have_list
    
    idx_list=[]
    for i in have_list:
        idx_list.append(have_data[(have_data['재료명'].str.startswith(i))|(have_data['재료명'].str.endswith(i))])

    # 필터링 된 레시피 코드들
    idx = np.sort(pd.concat(idx_list)['레시피 코드'].unique().tolist())
    idx = idx.tolist()
    # print(idx)


    return idx

def get_filtering_df(data_info, data_igd, data_process, idx):
    # data_info : 기본정보 데이터
    # data_igd : 재료정보 데이터
    # data_process : 과정정보 데이터

    have_info_list = []
    have_igd_list = []
    have_process_list = []

    for i in idx:
        have_info_list.append(data_info[data_info['레시피 코드']==i])
        have_igd_list.append(data_igd[data_igd['레시피 코드']==i])
        have_process_list.append(data_process[data_process['레시피 코드']==i])

    have_info = pd.concat(have_info_list)
    have_igd = pd.concat(have_igd_list)
    have_process = pd.concat(have_process_list)

    return have_info, have_igd, have_process




data = pd.read_csv('./레시피_재료정보.csv', encoding='cp949')

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

# print(noeat_list)
# print(have_list)
# print(noeat_filter(have_filter(data,have_list), noeat_list))

# noeat_filter(data, noeat_list)
idx = have_filter(noeat_filter(data, noeat_list), have_list)
df_info = pd.read_csv('./레시피_기본정보.csv', encoding='cp949')
df_igd = pd.read_csv('./레시피_재료정보.csv', encoding='cp949')
df_process = pd.read_csv('./레시피_과정정보.csv', encoding='cp949')

a, b, c = get_filtering_df(df_info, df_igd, df_process, idx)
print(a)
print(b)
print(c)