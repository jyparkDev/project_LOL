from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64
from pandas import DataFrame

# import matplotlib.pyplot as plt
# import numpy as np
# 여기는 통계 전용 페이지 입니다.

def ChampionFunc(request):
#     import matplotlib.pyplot as plt

    return render(request, 'statistics/champion.html')


def TierFunc(request):
    plt.rc('font', family='malgun gothic') # 한글 깨짐 방지용 폰트
    
    # KDA 값 
    data = {'KDA':[1.92,2.06,2.25,2.35,2.43,2.52,2.64,2.44,2.48], 'kill':[4.69,5.2,5.79,6.03,6.19,6.03,5.67,5.29,5.46],\
            'Death':[6.01,5.99,6,5.95,5.82,5.49,5.04,5.23,5.34], 'Assist':[6.84,7.17,7.73,7.94,7.94,7.81,7.64,7.49,7.77]}
    
    # 칼럼명
    indexs = ['lron', 'bronze', 'Silver', 'Gold', 'Platinum', 'Diamond','Master','Grand Master','Challenger']
    
    # 색상 설정
    my_colors = ('#ffc659','#00CFBC','#00A0D2', '#ff6c81',)
    
    # 저장 객체
    fig = plt.figure()
    width = 0.7 # 막대 너비
    
    df = DataFrame(data, index=indexs)
    df.plot(kind='bar', width=width, color=my_colors)
    plt.ylabel('게임당 KDA')
    plt.xticks(rotation=20)
    plt.legend()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri1 = urllib.parse.quote(string) # 시각화 값 저장
    
    plt.clf() # 시각화 자료 초기화
    
    
    # 티어 분포 파이 차트
    
    # 값
    out_ratio = np.array([[0.0062, 0.01, 0.08, 0.], [0.14, 0.29, 0.58, 1.82], [1.58, 1.59, 2.57, 7.92], [3.07, 5.46, 7.75, 16.4], [5.60, 8.24, 7.90, 11.1], [5.78, 5.04, 2.71, 2.37], [1.13, 0.53, 0.27, 0.11]])
    
    # 칼럼
    labels = ['Challenger', 'Diamond', 'Platinum', 'Gold' , 'Silver', 'Bronze', 'lron']
    
    # 색 설정 값
    colors_in = ['#ff6c81','#00a0d2','#80eee4','#ffc659', '#cacfdb', '#a69679','#cbcdcd']#
    colors_out = ['#f56277','#eb586d','#e14e63' ,'#d74459','#0096c8','#008cbe','#0082b4','#0078aa','#76e4da','#6cdad0','#62d0c6','#58c6bc','#f5bc4f','#ebb245','#e1a83b','#d79e31',\
              '#c0c5d1','#b6bbc7','#acb1bd','#a2a7b3','#9c8c6f','#928265','#88785b','#7e6e51','#c1c3c3', '#b7b9b9','#a3a5a5', '#adafaf']
    
    # 이미지 저장 객체
    fig = plt.figure()
    
    # 내부 파이차트
    plt.pie(out_ratio.sum(axis=1),radius=0.5,labels=labels, rotatelabels=True, startangle=90, shadow=True, colors=colors_in, pctdistance=2.1, labeldistance=2.1)
    wedgeprops={'width': 0.5}
    # 외부 파이차트
    plt.pie(out_ratio.flatten(), radius=1,startangle=90, colors=colors_out, wedgeprops=wedgeprops)
    plt.xticks(rotation=20)
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string) # 시각화 저장    
    plt.clf() # 시각화 자료 초기화
    
    # 티어 분포 누적 막대 그래프
    # 칼럼
    indexs = ['lron', 'bronze', 'Silver', 'Gold', 'Platinum', 'Diamond','Master','Grand Master','Challenger']
    my_colors = ('#ffc659','#91D54C','#00CFBC','#00A0D2')
    width = 0.7   
    # 시각화 저장 객체
    fig = plt.figure() 

    # 티어 설정 값
    datas = {'Ⅰ':[1.13,5.78,5.61,3.07,1.58,0.14,0.08,0.01,0.01], 'Ⅱ':[0.53,5.04,8.24,5.47,1.59,0.29,np.nan,np.nan,np.nan],\
             'Ⅲ':[0.27,2.7,7.9,7.75,2.57,0.58,np.nan,np.nan,np.nan],'Ⅳ':[0.11,2.37,11.09,16.35,7.92,1.82,np.nan,np.nan,np.nan]} 
    df = DataFrame(datas, index=indexs)
    width = 0.5     
    ax = df.plot(kind='bar', width=width, stacked=True, color=my_colors)

    plt.ylabel('점유율')
    plt.title('tier')
    plt.xticks(rotation=20)
    for p in ax.patches:
        print(p.get_bbox())
        left, bottom, width, height = p.get_bbox().bounds
        ax.annotate("%.2f%%"%(height*1), xy=(left+width/2, bottom+height/2), ha='center', va='center')
#     for ii,rect in enumerate(ax):
#        h1 = rect.get_height()
    plt.sca(ax)
    plt.box(False)
    plt.legend()
    
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format = 'png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri2 = urllib.parse.quote(string)
    
    return render(request, 'statistics/tier.html', {"graph": uri, 'bers':uri1, 'ber':uri2})
