from django.shortcuts import render
from lol.models import Champion
import ast
import MySQLdb
from django.http.response import HttpResponse
import json
import os.path
import collections
from lol.views.char_info import skill, spell, lun, startitem, itembuild, shoes,\
    char_poss
import threading, time 
# 여기는 챔피언 분석 및 상세 페이지 입니다.
try:
    path = os.path.abspath(os.path.dirname(__file__))
    with open(path+'/loldb.txt', 'r') as f:
        config = f.read()
        config = ast.literal_eval(config) 
except Exception as e:
    print("DB config read err : " + str(e))
  
def PositFunc(request):
    if request.GET['switch'] == "pos":
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
         
    elif request.GET['switch'] == "search":  
        cham = request.GET['cham']
        print(cham)
        #print(pos) 
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select cname, cimg from champion inner join pos on cname = cirum where cirum like '%"+"{}".format(cham)+"%' group by cname"
            cursor.execute(sql)
           
            data = cursor.fetchall()
            print(data)
            datas = []
            for i in data:
                dic ={'cname':i[0],'cimg':i[1]}
                datas.append(dic)
            print(datas)
            
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
    #print(cname)
    
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = '''
        select * from champion inner join pos on cname = cirum where cname = '{}'
        '''.format(cname)
        cursor.execute(sql)
        data = cursor.fetchall()
        char_pos = []
        for d in data:
            cp = list(collections.OrderedDict.fromkeys(d).keys())
            char_pos.append(cp)        
        pno = char_pos[0][3]
        
        # 캐릭터 정보 받아오는 곳
        #print(char_pos)           # 챔프/포지션
        skills = skill(pno) # 스킬
        spells = spell(pno) # 스펙
        luns = lun(pno)     # 룬
        startitems = startitem(pno)
        itembuilds = itembuild(pno)
        shoess = shoes(pno)
#         print(char_pos)
#        print(skills)
#         print(spells)
#         print(luns)
#         print(startitems)
#         print(itembuilds)
#         print(shoess)
        datas = {'char_pos':char_pos,'skill':skills,'spell':spells,'lun':luns,'sitem':startitems,'build':itembuilds,'shoes':shoess}
        return render(request, 'champion/champion_detail.html' , {'cdata':datas})
        
        
    except Exception as e2:
        print("postion ajax err : " + str(e2))    
    finally:
        #cursor.close()
        conn.close()    
        
def StatisticsChaFunc2(request):
    
    cname = request.GET['cname']
    pos = request.GET['pos']
#     print(cname)
#     print(pos)

    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = '''
        select * from champion inner join pos on cname = cirum where cname = '{}' and pname='{}'
        '''.format(cname,pos)
        cursor.execute(sql)
        data = cursor.fetchall()
        pos = []
        for d in data:
            cp = list(collections.OrderedDict.fromkeys(d).keys())
            pos.append(cp)        
        print(pos)
        pno = pos[0][3]
        
        # 캐릭터 정보 받아오는 곳
        #print(char_pos)           # 챔프/포지션
        char_pos = char_poss(cname)
        skills = skill(pno) # 스킬
        spells = spell(pno) # 스펙
        luns = lun(pno)     # 룬
        startitems = startitem(pno)
        itembuilds = itembuild(pno)
        shoess = shoes(pno)
#         print(char_pos)
#        print(skills)
#         print(spells)
#         print(luns)
#         print(startitems)
#         print(itembuilds)
#         print(shoess)
        datas = {'char_pos':char_pos,'skill':skills,'spell':spells,'lun':luns,'sitem':startitems,'build':itembuilds,'shoes':shoess}
        return render(request, 'champion/champion_detail.html' , {'cdata':datas})
        
        
    except Exception as e2:
        print("postion ajax err : " + str(e2))    
    finally:
        cursor.close()
        conn.close()    
        