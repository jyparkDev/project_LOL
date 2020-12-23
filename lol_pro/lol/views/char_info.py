from lol.models import Champion
import ast
import MySQLdb
import os.path
import collections

try:
    path = os.path.abspath(os.path.dirname(__file__))
    with open(path+'/loldb.txt', 'r') as f:
        config = f.read()
        config = ast.literal_eval(config)         
except Exception as e:
    print("DB config read err : " + str(e))
    
def char_poss(name):    
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = '''
        select * from champion inner join pos on cname = cirum where cname = '{}'
        '''.format(name)
        cursor.execute(sql)
        data = cursor.fetchall()
        char_pos = []
        for d in data:
            cp = list(collections.OrderedDict.fromkeys(d).keys())
            char_pos.append(cp)   
        print(char_pos)
        
        return char_pos
             
    except Exception as e2:
        print("charter err : " + str(e2))  
          
    finally:
        cursor.close()
        conn.close()    
         
def skill(pno):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = '''
        select * from pos inner join skill on pno = pnum where pno = '{}'
        '''.format(pno)
        cursor.execute(sql)
        data = cursor.fetchall()
        skills = []
        cham = data[0][:9]
        skill = list(data[0][9:])
        cp = list(collections.OrderedDict.fromkeys(cham).keys())
        skills = cp + skill
        #print(skills)
        return skills
    except Exception as e2:
        print("skill err : " + str(e2))    
    finally:
        cursor.close()
        conn.close()
    

def spell(pno):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = '''
        select * from pos inner join spell on pno = pnum where pno = '{}'
        '''.format(pno)
        cursor.execute(sql)
        data = cursor.fetchall()
        spell = []
        for d in data:
            cp = list(collections.OrderedDict.fromkeys(d).keys())
            spell.append(cp)
        return spell  
    except Exception as e2:
        print("spell err : " + str(e2))    
    finally:
        cursor.close()
        conn.close()
     

def lun(pno):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = '''
        select * from pos inner join lun on pno = pnum where pno = '{}'
        '''.format(pno)
        cursor.execute(sql)
        data = cursor.fetchall()
        trans_lun = []
        for i in data:
            trans_lun.append(list(i))   
        luns = []   
           
        for lun in range(len(trans_lun)):
            
            lun1 = trans_lun[lun][:12]
            lun2 = trans_lun[lun][12:]
            cp = list(collections.OrderedDict.fromkeys(lun1).keys())
            luns.append(cp+lun2)
        return luns   
    except Exception as e2:
        print("lun err : " + str(e2))    
    finally:
        cursor.close()
        conn.close()
   

def startitem(pno):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = '''
        select * from pos inner join startitems on pno = pnum where pno = '{}'
        '''.format(pno)
        cursor.execute(sql)
        data = cursor.fetchall()
        
        items = []
        for item in data:
            item1 = list(collections.OrderedDict.fromkeys(item[:4]).keys())
            item2 = list(item[4:])
            items.append(item1+item2)
        return items    
    except Exception as e2:
        print("startitem err : " + str(e2))    
    finally:
        cursor.close()
        conn.close()
    

def itembuild(pno):
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = '''
        select * from pos inner join itembuild on pno = pnum where pno = '{}'
        '''.format(pno)
        cursor.execute(sql)
        data = cursor.fetchall()
       
      
        build = []
        for buil in data:
            buil = list(collections.OrderedDict.fromkeys(buil).keys())
            build.append(buil)
        return build    
    except Exception as e2:
        print("itembuild err : " + str(e2))    
    finally:
        cursor.close()
        conn.close()
        
def shoes(pno):  
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = '''
        select * from pos inner join shoes on pno = pnum where pno = '{}'
        '''.format(pno)
        cursor.execute(sql)
        data = cursor.fetchall()
        #print(data)
      
        shoess = []
        for shoe in data:
            s = list(collections.OrderedDict.fromkeys(shoe).keys())
            shoess.append(s)
        return shoess    
    except Exception as e2:
        print("shoes err : " + str(e2))    
    finally:
        cursor.close()
        conn.close()      
    