#!/usr/bin/env python
#coding:utf-8
import requests

success = 0
failed = 0
gyyuser = "hdlagent"
gyypassword = "GNway123456"

#获取token值
def postgyytoken():
    url = "http://yun.gnway.com/gnapi/adminuser/login"
    data ={"username": gyyuser,"password": gyypassword}
    #headers = {'Content-Type':'application/json; charset=UTF-8',}
    r = requests.post(url=url,data =data)
    x = r.text
    print("x:" + x)
    z = x[2:14]
    
    #if z != "access_token" :
     #    print u'用户名或密码错误'
    #else :
     #   print u'用户名密码正确'
    
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
        print (g)
        global success
        success += 1
    else:
        print ("getgyyzj:01")
        global failed
        failed += 1		
    
    
    
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
        print (g)
        global success
        success += 1
    else:
        print ("getgyymgzj:01")
        global failed
        failed += 1
        
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
            
        print (g)
        global success
        success += 1
    else:
        print ("getgyykh:01")
        global failed
        failed += 1

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
        print (g)
        global success
        success += 1
    else:
        print ("getgyymgyh:01")
        global failed
        failed += 1

#5.4、修改客户
def gyyEditcustoms(hostid, domain, descript , username , password , contact , email , remark):

    token = postgyytoken()
    url = "http://yun.gnway.com/gnapi/customs/12879?access-token="+ token
    data ={"hostid": hostid , "domain":domain ,"descript": descript ,"username":username , "password": password ,"contact": contact ,"email": email ,"remark": remark}
    #headers = {'Content-Type':'application/json; charset=UTF-8',}
    print ({"hostid": hostid , "domain":domain ,"descript": descript ,"username":username , "password": password ,"contact": contact ,"email": email ,"remark": remark})
    r = requests.put(url=url,data =data)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("gyyEditcustoms:01")
        global failed
        failed += 1
        
#获取某个客户允许用户数(5.5、获取当前客户允许用户数)
def getgyymgyhs(customid):
    
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/custombyhost/"+hostid+"?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/maxonlines/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("getgyymgyhs:01")
        global failed
        failed += 1

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
        
        print (g)
        global success
        success += 1
    else:
        print ("postgyyaddusers:01")
        global failed
        failed += 1

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
        print (g)
        global success
        success += 1
    else:
        print ("postgyysubusers:01")
        global failed
        failed += 1

#获取某个客户允许用户到期时间(5.8、获取当前客户到期时间)
def getgyymgyhdqsj(customid):
    
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/custombyhost/"+hostid+"?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/enddate/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("getgyymgyhdqsj:01")
        global failed
        failed += 1
            
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
    
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("postgyyaddtime:01")
        global failed
        failed += 1
            
    
#5.10、用户退订
def postgyyorder(customid):
    token = postgyytoken()
    r=requests.delete("http://yun.gnway.com/gnapi/order/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("postgyyorder:01")
        global failed
        failed += 1
              


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
        print (g)
        global success
        success += 1
    else:
        print ("getgyyyyxx:01")
        global failed
        failed += 1
            
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
    print (d)
    g = z[15:17]
    
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("postgyyaddgroupuser:01")
        global failed
        failed += 1

#7.2、获取本伙伴下所有用户
def getgyyuser():
    
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/custombyhost/"+hostid+"?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/groupuser?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("getgyyuser:01")
        global failed
        failed += 1


#7.3、本伙伴单个用户信息
def getgyyuser_random(id):
    
    token = postgyytoken()
    
    
    r=requests.get("http://yun.gnway.com/gnapi/groupuser/"+id+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("getgyyuser_random:01")
        global failed
        failed += 1


#7.5、删除终端用户
def getgyydeleteuser(id):
    
    token = postgyytoken()
    
    
    r=requests.delete("http://yun.gnway.com/gnapi/groupuser/"+id+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]

    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("getgyydeleteuser:01")
        global failed
        failed += 1

        
#10.1、OEM获取客户详细信息
def getoem(customid):
    
    token = postgyytoken()
    #print token
    #print ("http://yun.gnway.com/gnapi/custombyhost/"+hostid+"?access-token="+ token)
    r=requests.get("http://yun.gnway.com/gnapi/custominfo/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("getoem:01")
        global failed
        failed += 1

#11.1、基于服务器上报的数据，跟网页客户页面保持一致
def getgyyzxrs(customid):
    
    token = postgyytoken()
    
    
    r=requests.get("http://yun.gnway.com/gnapi/customonline/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("getgyyzxrs:01")
        global failed
        failed += 1

 #11.2、基于连接服务器的接口的数据，跟终端用户详情页面保持一致
def getgyyzxrs2(customid):
    
    token = postgyytoken()
    
    
    r=requests.get("http://yun.gnway.com/gnapi/customon/"+customid+"?access-token="+ token)
    s = r.status_code
    z = r.text
    g = z[15:17]
    
    if g =="00":
        print (g)
        global success
        success += 1
    else:
        print ("getgyyzxrs2:01")
        global failed
        failed += 1

if __name__=="__main__":
    
 #   getgyyzj("hdlagent","GNway123451")
  #  getgyymgzj("959")
   # getgyymgyh("12327")
    #(4.3、获取主机列表)获取获取主机列表成功
    postgyytoken()
    print('------------')
    getgyyzj()
    print('------------------')
#(4.4、获取某个主机下的客户列表)获取某个主机下的用户列表成功(hostid)
    getgyymgzj("959")

#(5.2、获取所有客户信息)获取所有客户信息正确
    getgyykh()

#(5.3、获取单个客户信息) 获取某个用户信息成功(customid)
    getgyymgyh("12327")

#(5.5、获取当前客户允许用户数)获取某个客户允许用户数成功(customid)
    getgyymgyhs("12327")

#5.6、修改用户数（增加）(hostid,customid,maxonlinenum)
#jiekou.postgyyaddusers("959","12879","1")

#5.7、修改用户数（减少）(hostid,customid,maxonlinenum)
#jiekou.postgyysubusers("959","12879","1")


#(5.8、获取当前客户到期时间)获取某个客户允许用户到期时间成功(customid)
    getgyymgyhdqsj("12327")

#5.9、添加时长（月）
#jiekou.postgyyaddtime("959","12879","2019-02-28")

#5.10、用户退订(customid)
#jiekou.postgyyorder("12879")

#(6.1、获取应用详细信息)获取发布应用信息成功(customid)
    getgyyyyxx("13431")

#7.2、获取本伙伴下所有用户成功
    getgyyuser()

#7.3、本伙伴单个用户信息成功(id)
    getgyyuser_random("649")

#获取10.1、OEM获取客户详细信息成功(customid)
    getoem("12327")

#7.5、删除终端用户(id)
#jiekou.getgyydeleteuser("35691")

#11.1、基于服务器上报的数据，跟网页客户页面保持一致接口成功(customid)
    getgyyzxrs("12327")

#11.2、基于连接服务器的接口的数据，跟终端用户详情页面保持一致接口成功(customid)
    getgyyzxrs2("12327")
       
    result = str(success) + " successed, " + str(failed) + " failed"
    print(result)
    result.index("0 failed")

     

