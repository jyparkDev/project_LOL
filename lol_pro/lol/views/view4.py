from django.shortcuts import render
# 여기는 통계 전용 페이지 입니다.
import pandas as pd
import pickle
from tensorflow.keras.models import load_model
import random
import os.path
import numpy as np
import itertools
def QueryFunc(request):
    return render(request, 'multi/query.html')

def RequeryFunc(request):
    blue1 = request.POST.get('blue1')
    blue2 = request.POST.get('blue2')
    blue3 = request.POST.get('blue3')
    blue4 = request.POST.get('blue4')
    blue5 = request.POST.get('blue5')
    
    purple1 = request.POST.get('purple1')
    purple2 = request.POST.get('purple2')
    purple3 = request.POST.get('purple3')
    purple4 = request.POST.get('purple4')
    purple5 = request.POST.get('purple5')
    
    path = os.path.abspath(os.path.dirname(__file__))

        
    # 팀 --------------------------------------
    rf = pickle.load(open(path + '/model/randomforest_team.sav', 'rb'))
    model = load_model(path + '/model/sequential_team.hdf5')
    
    

    summoner_team_mean = pd.read_csv(path + '/model/10summoner_team_mean_data.csv', encoding = 'cp949')
    ten_summoners_df = pd.read_csv(path + '/model/08summoner_final_for_analysis.csv', encoding = 'cp949')
    
    summoners_name = list(ten_summoners_df['summonerName'])
    
    sample_summoners = random.sample(summoners_name, 10)
    """
    blues = random.sample(sample_summoners, 5)
    reds = list(set(sample_summoners) - set(blues))
    
    blue_team_summoners = blues
    red_team_summoners = reds
    print(blue_team_summoners)
    print(red_team_summoners)
    """
    blue_team_summoners = [blue1, blue2, blue3, blue4, blue5]
    red_team_summoners = [purple1, purple2, purple3, purple4, purple5]
    print(blue_team_summoners)
    print(red_team_summoners)
    # blue_team_summoners = ['16xyz', 'HUYATV SPARKLE', '북쪽의 괴물1', '충주갱수', 'daydayup']
    # red_team_summoners = ['Shining fans', 'sofm2', 'Liiv Route', 'FA Natalie', '모찌피치모찌피치']
    
    blue_df = pd.DataFrame()
    red_df = pd.DataFrame()
    for summoners in blue_team_summoners:
        imsi = summoner_team_mean[summoner_team_mean['summonerName'] == summoners]
        blue_df = pd.concat([blue_df, imsi])
    for summoners in red_team_summoners:
        imsi = summoner_team_mean[summoner_team_mean['summonerName'] == summoners]
        red_df = pd.concat([red_df, imsi])
    
    blue_df = blue_df.reset_index(drop=True)
    red_df = red_df.reset_index(drop=True)
    
    # print(blue_df.iloc[:, 2:])
    # print(red_df.iloc[:, 2:])
    # print(blue_df.iloc[:, 2:].mean() - red_df.iloc[:, 2:].mean())
    
    both_team_mean_series = blue_df.iloc[:, 2:].mean() - red_df.iloc[:, 2:].mean()
    both_team_mean_list = both_team_mean_series.to_list()
    print(both_team_mean_series)
    print(both_team_mean_list)
    
    pred = model.predict([both_team_mean_list])
    
#     pred = (model.predict([both_team_mean_list]) > 0.5).astype('int32')
#     pred = rf.predict([both_team_mean_list])
#     pred = (rf.predict([both_team_mean_list]) > 0.5).astype('int32')
    

    
        
    # 개인 --------------------------------------
    rf = pickle.load(open(path + '/model/randomforest_indi.sav', 'rb')) # 랜덤포레스트 모델
    model = load_model(path + '/model/sequential_indi.hdf5') # 시퀀셜 모델
    
    ten_summoners_df = pd.read_csv(path + '/model/08summoner_final_for_analysis.csv', encoding = 'cp949')
    # print(ten_summoners_df)
    summoners_name = list(ten_summoners_df['summonerName'])
    
    sample_summoners = random.sample(summoners_name, 10)
    
    blue_team_summoners = [blue1, blue2, blue3, blue4, blue5]
    red_team_summoners = [purple1, purple2, purple3, purple4, purple5]
#     print(blue_team_summoners)
#     print(red_team_summoners)
    
    blue_df1 = pd.DataFrame()
    red_df1 = pd.DataFrame()
    for summoners in blue_team_summoners:
        imsi = ten_summoners_df[ten_summoners_df['summonerName'] == summoners]
        blue_df1 = pd.concat([blue_df1, imsi])
    for summoners in red_team_summoners:
        imsi = ten_summoners_df[ten_summoners_df['summonerName'] == summoners]
        red_df1 = pd.concat([red_df1, imsi])
    
    blue_df1 = blue_df1.reset_index(drop=True)
    red_df1 = red_df1.reset_index(drop=True)
    blue = round(blue_df1, 2).to_dict(orient='record')
    purple = round(red_df1, 2).to_dict(orient='record')
    
#     print(blue_df1)
#     print(red_df1)
#     
#     print(list(blue_df1.iloc[:, 4:].columns))
    
    col_sum = list(blue_df1.iloc[:, 4:].columns)
    col_mean = ['firstBloodKill', 'firstInhibitorKill', 'visionScore', 'kda'] # ☆'firstBloodKill', 'firstInhibitorKill'는 평균이 나을까?
    for dele in col_mean:
        col_sum.remove(dele)
    
    blue_total = blue_df1[col_sum].sum().append(blue_df1[col_mean].mean()) # .to_list()
    red_total = red_df1[col_sum].sum().append(red_df1[col_mean].mean()) # .to_list()
    
    # blue_total.extend(red_total)
    
    #-----------------수정 2020.12.22---------------
    both_total = (blue_total - red_total)
    both_total = both_total[:, np.newaxis]
    # print(both_total.shape) # (20, ) → (20, 1)
    
    # 스케일링
    from sklearn.preprocessing import StandardScaler
    
    sc = StandardScaler()
    sc.fit(both_total)    # x값만 대상
    both_total = sc.transform(both_total)  
    # print(both_total.shape)
    
    
    both_newaxis = both_total.reshape(1, -1)
    # print(both_newaxis.shape) # (20, 1) → (1, 20)
    # ----------------------------------------------
    
    
    pred = model.predict([both_newaxis]) # 정확한 분석과 확률을 위해 random forest 대신 sequential 사용
    # pred = (model.predict([blue_total]) > 0.5).astype('int32')
    # pred = rf.predict([blue_total])
    # pred = (rf.predict([blue_total]) > 0.5).astype('int32')
    print('예측값:', pred.flatten()) # blue team (100) 기준
    
    key1 = ""
    key2 = ""
    key3 = ""
    if pred > 0.5:
        key1 = "블루팀 승리"
        key2 = "퍼플팀 패배"
        key3 = "블루팀이 " + str(round(pred[0][0]*100,2)) + "% 확률로 승리예측"
    else:
        key1 = "블루팀 패배"
        key2 = "퍼플팀 승리"
        key3 = "퍼플팀 승리 " + str(round((1 - pred[0][0])*100,2)) + "% 확률로 승리예측"
    print('예측값:', pred.flatten()) # blue team (100) 기준   
    print(key3)
    
    
    # [괜찮은 조합 찾기]
    
    all = blue_team_summoners.copy()
    all.extend(red_team_summoners)
    print(all)
    
    combi = list(itertools.combinations(all, 5))
    print(combi)
    print(len(combi))
    
    best_combi = {}
    
    for com in combi:
        red_team = all.copy()
    
        blue_team = list(com)
        for dele in blue_team:
            red_team.remove(dele)
    
        # print(blue_team)
        # print(red_team)
    
        blue_df = pd.DataFrame()
        red_df = pd.DataFrame()
        for summoners in blue_team:
            imsi = ten_summoners_df[ten_summoners_df['summonerName'] == summoners]
            blue_df = pd.concat([blue_df, imsi])
        for summoners in red_team:
            imsi = ten_summoners_df[ten_summoners_df['summonerName'] == summoners]
            red_df = pd.concat([red_df, imsi])
    
        blue_df = blue_df.reset_index(drop=True)
        red_df = red_df.reset_index(drop=True)
    
        col_sum = list(blue_df.iloc[:, 4:].columns)
        col_mean = ['firstBloodKill', 'firstInhibitorKill', 'visionScore', 'kda'] # ☆'firstBloodKill', 'firstInhibitorKill'는 평균이 나을까?
        for dele in col_mean:
            col_sum.remove(dele)
    
        blue_total = blue_df[col_sum].sum().append(blue_df[col_mean].mean())
        red_total = red_df[col_sum].sum().append(red_df[col_mean].mean())
        
        both_total = (blue_total - red_total).to_numpy()
        both_total = both_total[:, np.newaxis]
        
        # 스케일링
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        sc.fit(both_total)
        both_total = sc.transform(both_total)
          
        both_newaxis = both_total.reshape(1, -1)

        pred3 = model.predict([both_newaxis])

        if pred3.flatten()[0] < 0.55 and pred3.flatten()[0] > 0.45:
            best_combi[str(blue_team)] = pred3.flatten()[0]
            
    print(best_combi)
    best_of_value = min(best_combi.values(), key=lambda x: abs(0.5-x))
    best_of_key = list(best_combi.keys())[list(best_combi.values()).index(best_of_value)]
    
    best_of_best = {}
    best_of_best[best_of_key] = best_of_value
        
    return render(request, 'multi/query.html', {'key1':key1, 'key2':key2, 'key3':key3,
                                                'blue':blue, 'purple':purple, 'pred':pred,
                                                'best':best_combi, 'best_of_best':best_of_best})