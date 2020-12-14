from django.shortcuts import render
# 여기는 통계 전용 페이지 입니다.

def ChampionFunc(request):
    return render(request, 'statistics/champion.html')


def TierFunc(request):
    return render(request, 'statistics/tier.html')