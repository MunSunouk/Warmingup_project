import pandas as pd
import numpy as np

# ingre_str 는 필터할 단어들
# ingre_str = '-쌀,-금,-새우,-버섯,-멸치,감자,고구마,안심,마늘,계란,콩'
def filtering_data(ingre_str):
    ingre_list = ingre_str.split(',')

    # 못먹는 재료, 먹는 재료 리스트
    noeat_list = []
    have_list = []
    for i in ingre_list:
        if i.startswith('-'):
            i = i.replace('-','')
            noeat_list.append(i)
        else:
            have_list.append(i)


    noeat_data = pd.read_csv('./레시피_재료정보.csv', encoding='cp949')

    
    idx_list=[]
    for i in noeat_list:
        idx_list.append(noeat_data[(noeat_data['재료명'].str.startswith(i))|(noeat_data['재료명'].str.endswith(i))])

    idx = np.sort(pd.concat(idx_list)['레시피 코드'].unique().tolist())

    # 안먹는 것을 제거한 데이터리스트
    noeat_data = noeat_data[~noeat_data['레시피 코드'].isin(idx)]
    
    idx_list=[]
    for i in have_list:
        idx_list.append(noeat_data[(noeat_data['재료명'].str.startswith(i))|(noeat_data['재료명'].str.endswith(i))])

    # 필터링 된 레시피 코드들
    idx = np.sort(pd.concat(idx_list)['레시피 코드'].unique().tolist())
    idx = idx.tolist()

    # 경로 설정을 해줘야 한다. 중요.....

    df_info = pd.read_csv('./레시피_기본정보.csv', encoding='cp949')
    df_igd = pd.read_csv('./레시피_재료정보.csv', encoding='cp949')
    df_process = pd.read_csv('./레시피_과정정보.csv', encoding='cp949')


    have_info_list = []
    have_igd_list = []
    have_process_list = []

    for i in idx:
        have_info_list.append(df_info[df_info['레시피 코드']==i])
        have_igd_list.append(df_igd[df_igd['레시피 코드']==i])
        have_process_list.append(df_process[df_process['레시피 코드']==i])

    have_info = pd.concat(have_info_list)
    have_igd = pd.concat(have_igd_list)
    have_process = pd.concat(have_process_list)

    return have_info, have_igd, have_process

