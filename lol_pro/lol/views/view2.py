from django.shortcuts import render
from lol.models import Champion
import ast
import MySQLdb
from django.http.response import HttpResponse
import json
import os.path

# 여기는 챔피언 분석 및 상세 페이지 입니다.
try:
    path = os.path.abspath(os.path.dirname(__file__))
    with open(path+'/loldb.txt', 'r') as f:
        config = f.read()
        config = ast.literal_eval(config) 
except Exception as e:
    print("DB config read err : " + str(e))
  
def PositFunc(request):
    pos = request.GET['pos']
    #print(pos) 
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = """
        select cname, cimg, pname from champion inner join pos on cname = cirum where pname = '{}'
        """.format(pos)
        cursor.execute(sql)
        data = cursor.fetchall()
        #print(data[0])
        datas = []
        for i in data:
            dic ={'cname':i[0],'cimg':i[1],'pname':i[2]}
            datas.append(dic)
        #print(datas)
        
    except Exception as e2:
        print("postion ajax err : " + str(e2))    
    
    finally:
        cursor.close()
        conn.close()
        
    return HttpResponse(json.dumps(datas), content_type="application/json")    
def StatisticsFunc(request):
        champ = Champion.objects.all()
        #print(champ)
        return render(request, 'champion/statistics.html', {'cham':champ})


    
def StatisticsChaFunc(request):
    cname = request.GET['cname']
    print(cname)
    
    try:
        """
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = '''
        select cname, cimg, pname from champion inner join pos on cname = cirum where pname = '{}'
        '''.format()
        cursor.execute(sql)
        data = cursor.fetchall()
        #print(data[0])
        datas = []
        for i in data:
            dic ={'cname':i[0],'cimg':i[1],'pname':i[2]}
            datas.append(dic)
        #print(datas)
      """  
        pass
    except Exception as e2:
        print("postion ajax err : " + str(e2))    
    finally:
#         cursor.close()
#         conn.close()    
        pass
    return render(request, 'champion/champion_detail.html')