#!/usr/bin/env python
#coding:utf-8
import random
import string
import requests
import gettime
import time
success = 0
failed = 0
gyyuser = "hdlagent"
gyypassword = "GNway123456"

def postgyytoken():
    url = "http://yun.gnway.com/gnapi/adminuser/login"
    data ={"username": gyyuser,"password": gyypassword}
    r = requests.post(url=url,data =data)
    x = r.text
    z = x[2:14]
    return x[17:-2]
#获取所有主机列表信息(4.3、获取主机列表)       
def getgyyzj():
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/customs?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/hosts?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "getgyyzj:01"
        global failed
        failed += 1
    return
    
#获取某个主机下的用户列表(4.4、获取某个主机下的客户列表)
def getgyymgzj(hostid):
    
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/custombyhost/"+hostid+"?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/custombyhost/"+hostid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "getgyymgzj:01"
        global failed
        failed += 1
    return
#新建公司(5.1)
def postgyycustomid(hostid, domain, descript , username , password , contact , email , remark):
    token = postgyytoken()
    url = "http://yun.gnway.com/gnapi/customs?access-token="+ token
    data ={"hostid": hostid , "domain":domain ,"descript": descript ,"username":username , "password": password ,"contact": contact ,"email": email ,"remark": remark}
    r = requests.post(url=url,data =data)
    z = r.text
    
    g = z[15:17]
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "postgyycustomid:01"
        global failed
        failed += 1
    return z[-6:-1]

#获取所有客户信息(5.2、获取所有客户信息)
def getgyykh():
    
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/customs?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/customs?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]

    if g =="00":
            
        print g
        global success
        success += 1
    else:
        print "getgyykh:01"
        global failed
        failed += 1
    return

#获取某个用户信息 (5.3、获取单个客户信息) 
def getgyymgyh(customid):
    
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/custombyhost/"+hostid+"?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/customs/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "getgyymgyh:01"
        global failed
        failed += 1
    return



#5.4、修改客户
def gyyEditcustoms(customid ,hostid, domain, descript , username , password , contact , email , remark):

    token = postgyytoken()
    url = "http://yun.gnway.com/gnapi/customs/"+customid+"?access-token="+ token
    data ={"hostid": hostid , "domain":domain ,"descript": descript ,"username":username , "password": password ,"contact": contact ,"email": email ,"remark": remark}
    #headers = {'Content-Type':'application/json; charset=UTF-8',}
    r = requests.put(url=url,data =data)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "gyyEditcustoms:01"
        global failed
        failed += 1
    return        
#获取某个客户允许用户数(5.5、获取当前客户允许用户数)
def getgyymgyhs(customid):
    
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/custombyhost/"+hostid+"?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/maxonlines/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if z[-3:-2]=="1":
        
        if g =="00":
            print g
            global success
            success += 1
        else:
            print "getgyymgyhs:01"
            global failed
            failed += 1
    return
#5.6、修改用户数（增加）
def postgyyaddusers(zjid, gsid , yhs):
    token = postgyytoken()
    url = "http://yun.gnway.com/gnapi/addusers?access-token="+ token
    data ={"hostid": zjid,"customid": gsid ,"maxonlinenum": yhs}
    #headers = {'Content-Type':'application/json; charset=UTF-8',}
    r = requests.post(url=url,data =data)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        
        print g
        global success
        success += 1
    else:
        print "postgyyaddusers:01"
        global failed
        failed += 1
    return
#5.7、修改用户数（减少）
def postgyysubusers(zjid, gsid , yhs):
    token = postgyytoken()
    url = "http://yun.gnway.com/gnapi/subusers?access-token="+ token
    data ={"hostid": zjid,"customid": gsid ,"maxonlinenum": yhs}
    #headers = {'Content-Type':'application/json; charset=UTF-8',}
    r = requests.post(url=url,data =data)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "postgyysubusers:01"
        global failed
        failed += 1
    return

#获取某个客户允许用户到期时间(5.8、获取当前客户到期时间)
def getgyymgyhdqsj(customid):
    
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/custombyhost/"+hostid+"?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/enddate/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    sj = z[-12:-2]
    dqsj = gettime.get_lastday_month(1)
    
    if sj == dqsj :
        
        if g =="00":
            print g
            global success
            success += 1
        else:
            print "postgyyaddtime:01"
            global failed
            failed += 1
    return
#5.9、添加时长（月）
def postgyyaddtime(zjid, gsid , jssj):
    token = postgyytoken()
    url = "http://yun.gnway.com/gnapi/addtime?access-token="+ token
    data ={"hostid": zjid,"customid": gsid ,"enddate": jssj}
    #headers = {'Content-Type':'application/json; charset=UTF-8',}
    r = requests.post(url=url,data =data)
    s = r.status_code
    z = r.text
    #print z
    g = z[15:17]
    y = z[-13:-3]
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "postgyyaddtime:01"
        global failed
        failed += 1
    return
#5.10、用户退订
def postgyyorder(customid):
    token = postgyytoken()
    r=requests.delete("http://yun.gnway.com/gnapi/order/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "postgyyorder:01"
        global failed
        failed += 1
    return


#获取发布应用信息(6.1、获取应用详细信息)
def getgyyyyxx(customid):
    
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/custombyhost/"+hostid+"?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/apps/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "getgyyyyxx:01"
        global failed
        failed += 1
    return 
#7.1、新建用户
def postgyyaddgroupuser(customid, username, descript , password , repassword , contact , email , maxloginnum , remark , repeatlogin , is_modify_passwd):
    token = postgyytoken()
    url = "http://yun.gnway.com/gnapi/groupuser?access-token="+ token
    data ={"customid": customid ,"username": username , "descript": descript ,"password": password ,"repassword": repassword,"contact": contact ,"email": email ,"maxloginnum": maxloginnum,"remark": remark ,"repeatlogin": repeatlogin ,"is_modify_passwd":is_modify_passwd}
    #headers = {'Content-Type':'application/json; charset=UTF-8',}
    r = requests.post(url=url,data =data)
    s = r.status_code
    z = r.text
    d = z[-7:-2]
    g = z[15:17]
    
    if g =="00":
        global success
        success += 1
    else:
        print "postgyyaddgroupuser:01"
        global failed
        failed += 1
        
    return d

#7.2、获取本伙伴下所有用户
def GetGyyAllusers():
    
    token = postgyytoken()
    r=requests.get("http://yun.gnway.com/gnapi/groupuser?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "getgyyuser:01"
        global failed
        failed += 1
    return


#7.3、本伙伴单个用户信息
def getgyyuser_random(id):
    
    token = postgyytoken()
    r=requests.get("http://yun.gnway.com/gnapi/groupuser/"+id+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    #if z[-40:-38] == "53":
     #   print z[-40:-38]
    
    if g =="00":
        
        global success
        success += 1
    else:
        print "getgyyuser_random:01"
        global failed
        failed += 1
    return z
#7.4、编辑用户

def gyyEdituser(id, customid, username, descript , password , repassword , contact , email , maxloginnum , remark , repeatlogin , is_modify_passwd):
    maxloginnum1 = ord(maxloginnum)+1
    
    token = postgyytoken()
    url = "http://yun.gnway.com/gnapi/groupuser/"+id+"?access-token="+ token
    data ={"customid": customid ,"username": username , "descript": descript ,"password": password ,"repassword": repassword,"contact": contact ,"email": email ,"maxloginnum": maxloginnum1,"remark": remark ,"repeatlogin": repeatlogin ,"is_modify_passwd":is_modify_passwd}
    #headers = {'Content-Type':'application/json; charset=UTF-8',}
    
    r = requests.put(url=url,data =data)
    
    s = r.status_code
    z = r.text
    d = z[-7:-2]
    g = z[15:17]
    time.sleep(2)
    
    getgyyuser_random(id)
    
    
    if g =="00":
        global success
        success += 1
    else:
        print "gyyEdituser:01"
        global failed
        failed += 1
        
    return d
#7.5、删除终端用户    
def deleuser(id):
    token = postgyytoken()
    r=requests.delete("http://yun.gnway.com/gnapi/groupuser/"+id+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        
        global success
        success += 1
    else:
        print "getgyydeleteuser:01"
        global failed
        failed += 1

#7.6、获取终端用户程序名称和url的接口
def GetGyyUsersName(id):
    token = postgyytoken()
    r=requests.get("http://yun.gnway.com/gnapi/groupuserapps/"+id+"?access-token="+ token)
    
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "getgyyuser:01"
        global failed
        failed += 1
    
    return z
#7.7、根据用户名获取发布的应用信息
def postgyyUserApplication(descript, username):
    token = postgyytoken()
    url = "http://yun.gnway.com/gnapi/guserapps?access-token="+ token
    
    data ={"cname": descript, "gname": username}
    
    #headers = {'Content-Type':'application/json; charset=UTF-8',}
    r = requests.post(url=url,data =data)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "getgyyuser:01"
        global failed
        failed += 1
        
    return z

#11.1、基于服务器上报的数据，跟网页客户页面保持一致
def getgyyzxrs(customid):
    
    token = postgyytoken()
    
    
    r=requests.get("http://yun.gnway.com/gnapi/customonline/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "getgyyzxrs:01"
        global failed
        failed += 1
    return
 #11.2、基于连接服务器的接口的数据，跟终端用户详情页面保持一致
def getgyyzxrs2(customid):
    
    token = postgyytoken()
    
    
    r=requests.get("http://yun.gnway.com/gnapi/customon/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print g
        global success
        success += 1
    else:
        print "getgyyzxrs2:01"
        global failed
        failed += 1
    return        
#新建、查询、删除用户
def GyyUserOperation(customid, username, descript , password , repassword , contact , email , maxloginnum , remark , repeatlogin , is_modify_passwd):
    token = postgyytoken()
    id = postgyyaddgroupuser(customid, username, descript , password , repassword , contact , email , maxloginnum , remark , repeatlogin , is_modify_passwd)
    time.sleep(2)
    #本伙伴单个用户信息
    getgyyuser_random(id)
    time.sleep(3)
    #编辑用户
    gyyEdituser(id +"", customid +"", "8ng11", "", "mi", "mi", "", "", "4", "", "true", "1")
    
    time.sleep(2)
    #删除用户
    deleuser(id)
#创建公司、修改公司、加时间、减时间、退订
def caozou(hostid, domain, descript , username , password , contact , email , remark):
    dqsj = gettime.get_lastday_month(1)
    gsid = postgyycustomid(hostid, domain, descript , username , password , contact , email , remark)
#获取新建用户
    getgyymgyh(gsid+"")
    #给公司加时间
    postgyyaddtime("959",gsid+"",dqsj+"")
    #公司到期时间
    getgyymgyhdqsj(gsid+"")
    #修改公司用户数（添加）
    postgyyaddusers("959",gsid+"","1")
#减少用户数
    postgyysubusers("959",gsid+"","1")
    #获取用户数
    getgyymgyhs(gsid+"")
    ##新建、查询、删除用户
    GyyUserOperation(gsid+"", "8ng11", "", "mi", "mi", "", "", "", "", "true", "1")
    time.sleep(5)

    #获取主机列表
    getgyyzj()
    #获取某个主机下的客户列表
    getgyymgzj("959")
    #获取应用详细信息
    getgyyyyxx(gsid+"")
    #获取所有客户信息)
    getgyykh()
    
    getgyyzxrs2(gsid+"")
    getgyyzxrs(gsid+"")
    time.sleep(300)
    #用户退订
    postgyyorder(gsid+"")
    return
if __name__=="__main__":
    # 多个字符中生成指定数量的随机字符：
    ran_str = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',8))

    caozou("959",ran_str +".yun.gnway.com",ran_str+"",ran_str+"",ran_str+"","","","ceshi")

           
    result = str(success) + " successed, " + str(failed) + " failed"
    print(result)
    result.index("0 failed")
