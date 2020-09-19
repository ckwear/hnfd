
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .forms import *
from django.http import HttpResponse, JsonResponse
# from selenium import webdriver
from django.db import connection
import json
from selenium.webdriver.support.ui import WebDriverWait
###셀레니엄모듈
# from threading import Thread
from os import system
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotVisibleException
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



import pandas as pd
import pymysql
from sqlalchemy import create_engine
from operator import itemgetter as itg
import itertools as it
import time
import os





def login(request):
    loginform = LoginForm()
    if request.method == "POST":
         loginform = LoginForm(request.POST)
         return HttpResponse('wefwef')
         if loginform.is_valid():
             post = loginform.save(commit=False)
             post.author = 'markcha'
             post.published_date = timezone.now()
             post.save()
             return redirect('showtext', pk=post.pk)
    else:
         posting = MakePost()
    return render(request, 'login.html', {'loginform' : loginform})

def Register(request):

    if request.method == "POST":
         registerform = RegisterForm(request.POST)
         #return HttpResponse('aaa %s' % request.POST['name'])
         if registerform.is_valid():
             user = User()
             get_name = request.POST['name']
             get_id = request.POST['id']
             get_email = request.POST['email']
             #cf_user = User.objects.filter(name=get_name, user_id=get_id, email=get_email)

             if request.POST['pw'] != request.POST['pw2']:
                 return HttpResponse('비밀번호가 다릅니다.')
             else:
                 user.id = get_id
                 user.name = get_name
                 user.email = get_email
                 user.password = request.POST['pw']
                 user.save()
                 return redirect('start')
    else:
         registerform = RegisterForm()
    return render(request, 'register.html', {'registerform': registerform})








def ChoiceOrderPaper(request):
    if request.method == "POST":
         date = request.POST['openDate']
         date2 = date
         date += ' 00:00:00'
         fcty_nu = request.POST['fcty_nu']
         subdivision2 = request.POST['subdivision']
         print(fcty_nu)
         # choice_odr_ppr = OrderPaper.objects.filter(due_date=date, factory_num=fcty_nu, subdivision=subdivision2)
         choice_odr_ppr = OrderPaper.objects.filter(due_date=date, factory_num=fcty_nu, subdivision=subdivision2)
         
         #if date:
         #print(choice_odr_ppr)
         return render(request, 'choice_order_paper.html', {'rst' : choice_odr_ppr})

    else:
         choice_order_form = ChoiceOrderForm()

    return render(request, 'choice_order_paper.html', {})

def CatchItemAjax(request):
    cursor = connection.cursor()
    cnt = cursor.execute('''
    SELECT op.item_code AS "item_code",  MAX(op.item_name) AS "item_name" 
    FROM order_paper AS op 
    WHERE op.item_code NOT IN(SELECT it.item_code FROM item AS it) 
    GROUP BY op.item_code;''')
    
    rsget_dont_have_itemst = cursor.fetchall()
    make_json = []
    for item in rsget_dont_have_itemst:
        make_json.append({'row' : [{'item_code' : item[0]},{'item_name' : item[1]}]})
    # print(make_json)
    return JsonResponse({'query':make_json, 'cnt' : cnt})

def CatchOrderPaperAjax(request):
    if request.method == "POST":
        date = request.POST['send_date']
        date += ' 00:00:00'
        factory_num = request.POST['send_factoy_num']
        sub = request.POST['send_sub']
        # print(date, factory_num, sub)
        cursor = connection.cursor()
        cnt = cursor.execute("SELECT * FROM order_paper where due_date='{0}' and factory_num='{1}' and subdivision='{2}';".format(date, factory_num, sub))
        rsget_dont_have_itemst = cursor.fetchall()
        print(rsget_dont_have_itemst)
        make_json = []
        for item in rsget_dont_have_itemst:
            make_json.append({'No' : item[2],'item_code' : item[3],'item_name' : item[4], 'due_date' : item[5],'con' : item[6],'item_kind' : item[7],'soter' : item[8],'input' : item[9],'zone' : item[10],'bus_num' : item[11],'order_part' : item[12],'cmpy_code' : item[13],'cmpy_name' : item[14],'order_value' : item[15],'unit' : item[16],'unit_price' : item[17],'order_price' : item[18],'delivery_part' : item[19],'ett' : item[20],'ordered_num' : item[21],'ordered_ITEM_num' : item[22],'order_num' : item[23],'order_ITEM_num' : item[24],'delivery_cmpy' : item[25],'delivery_num' : item[26],'factory_num' : item[27], 'subdivision' : item[28]})
        # print(make_json)
        return JsonResponse({'query':make_json, 'cnt' : cnt})

def ResultTwo(request):
    # return HttpResponse('wejfiowef')
    print(request.GET.get('send_date'))
    # choice_odr_ppr = OrderPaper.objects.filter(due_date=request.GET.get('send_date'), factory_num=request.GET.get('send_factoy_num'), subdivision=request.GET.get('send_sub'))
    # for item in choice_odr_ppr:
    #     print(item)
    # cursor_one = connection.cursor()
    # cnt1 = cursor_one.execute("SELECT * FROM order_paper where due_date='{0}' and factory_num='{1}' and subdivision='{2}';".format(request.GET.get('send_date'), request.GET.get('send_factoy_num'), '1차'))
    # first_ordpp_qry = cursor_one.fetchall()

    # cursor_two = connection.cursor()
    # cnt2 = cursor_two.execute("SELECT * FROM order_paper where due_date='{0}' and factory_num='{1}' and subdivision='{2}';".format(request.GET.get('send_date'), request.GET.get('send_factoy_num'), '2차'))
    # second_ordpp_qry = cursor_two.fetchall()
    # zz = list(map(itg(24), first_ordpp_qry))
    # zzz = list(map(itg(24), second_ordpp_qry))
    # # print(zz)
    # # print(zzz)
    # rst_list = []
    # for pp_one_item in first_ordpp_qry:
    #     pp_one_item = list(pp_one_item)
    #     for pp_two_item in second_ordpp_qry:
    #         pp_two_item = list(pp_two_item)
    #         if pp_one_item[24]==pp_two_item[24]:
    #             if pp_one_item[15] == pp_two_item[16]:
    #                 pp_two_item.append(0)
                    
    #             elif pp_one_item[15] > pp_two_item[16]:
    #                 pp_two_item.append(-1)
    #             elif pp_one_item[15] < pp_two_item[16]:
    #                 pp_two_item.append(1)
    #             print(pp_two_item)
    #             break

    date = request.GET.get('send_date')
    date += ' 00:00:00'
    factory_num = request.GET.get('send_factoy_num')
    sub = request.GET.get('send_sub')
    culoms = ['order_num', 'input', 'cmpy_name', 'delivery_part', 'unit', 'item_name', 'zone', 'order_value', 'box_num', 'box', 'pac', 'due_date', 'factory_num', 'sub']
    sql = '''
        SELECT op.order_num, max(op.input), max(op.cmpy_name), max(op.delivery_part), max(op.unit), max(op.item_name), max(op.zone), max(op.order_value), max(it.pac_num),

        sum(CASE
        	WHEN it.unit = 'BOX' AND op.delivery_part='배송' THEN op.order_value
        	WHEN it.unit = 'PAC' AND op.delivery_part='배송' THEN op.order_value DIV it.pac_num
        	WHEN it.unit = 'EA'  AND op.delivery_part='배송' THEN (op.order_value DIV it.ea_num) DIV it.pac_num
        	WHEN it.unit = 'KG'  AND op.delivery_part='배송' THEN (op.order_value DIV it.kg_num) DIV it.pac_num
        	WHEN op.delivery_part='직송' THEN 0
        	ELSE 0
        END)
        box, sum(
        	CASE WHEN op.delivery_part='배송' THEN
        		(CASE
        			WHEN it.unit = 'BOX' THEN 0
        			WHEN it.unit = 'PAC' THEN op.order_value MOD it.pac_num
        			WHEN it.unit = 'EA'  THEN (op.order_value DIV it.ea_num) MOD it.pac_num
        			WHEN it.unit = 'KG'  THEN (op.order_value DIV it.kg_num) MOD it.pac_num
        			ELSE 0
        		end)
        	ELSE 0
        end
        ) pac, max(op.due_date), max(op.factory_num), max(op.subdivision), max(op.inh_code), max(op.item_code)
        FROM order_paper AS op, item AS it
        WHERE op.due_date='{0}' AND  op.factory_num='{1}' AND op.subdivision='{2}' AND op.item_code=it.item_code
        GROUP BY op.item_code,  op.order_num WITH rollup
        
    '''.format(date, factory_num, '1차')
    cursor = connection.cursor()
    cnt = cursor.execute(sql)
    result_one_paper = cursor.fetchall()
    sql = '''
        SELECT op.order_num, max(op.input), max(op.cmpy_name), max(op.delivery_part), max(op.unit), max(op.item_name), max(op.zone), max(op.order_value), max(it.pac_num),

        sum(CASE
        	WHEN it.unit = 'BOX' AND op.delivery_part='배송' THEN op.order_value
        	WHEN it.unit = 'PAC' AND op.delivery_part='배송' THEN op.order_value DIV it.pac_num
        	WHEN it.unit = 'EA'  AND op.delivery_part='배송' THEN (op.order_value DIV it.ea_num) DIV it.pac_num
        	WHEN it.unit = 'KG'  AND op.delivery_part='배송' THEN (op.order_value DIV it.kg_num) DIV it.pac_num
        	WHEN op.delivery_part='직송' THEN 0
        	ELSE 0
        END)
        box, sum(
        	CASE WHEN op.delivery_part='배송' THEN
        		(CASE
        			WHEN it.unit = 'BOX' THEN 0
        			WHEN it.unit = 'PAC' THEN op.order_value MOD it.pac_num
        			WHEN it.unit = 'EA'  THEN (op.order_value DIV it.ea_num) MOD it.pac_num
        			WHEN it.unit = 'KG'  THEN (op.order_value DIV it.kg_num) MOD it.pac_num
        			ELSE 0
        		end)
        	ELSE 0
        end
        ) pac, max(op.due_date), max(op.factory_num), max(op.subdivision),max(op.inh_code), max(op.item_code)
        FROM order_paper AS op, item AS it
        WHERE op.due_date='{0}' AND  op.factory_num='{1}' AND op.subdivision='{2}' AND op.item_code=it.item_code
        GROUP BY op.item_code,  op.order_num WITH rollup
    '''.format(date, factory_num, '2차')
    cursor = connection.cursor()
    cnt = cursor.execute(sql)
    result_two_paper = cursor.fetchall()
    # pd.set_option('display.max_row', 500)
    # print(pd.DataFrame(result_one_paper))
    # print(result_two_paper)
    #2019-12-23 y1-2
    result_one_paper = list(result_one_paper)
    result_two_paper = list(result_two_paper)
    rst_list = []
    rst_it = []
    print(result_one_paper[0][14])
    while result_one_paper:
        if result_one_paper[0][0] == None:
            it = result_one_paper.pop(0)
            rst_it.append(it)
            # print(it)


        if result_two_paper[0][0] == None:
            it = result_two_paper.pop(0)
            rst_it.append(it)
            # print(it)

        # if result_one_paper[0][0] == None:
        #     it = result_one_paper.pop(0)
        #     rst_it.append(it)


        # if result_two_paper[0][0] == None:
        #     it = result_two_paper.pop(0)
        #     rst_it.append(it)
        
        if result_one_paper[0][14] == result_two_paper[0][14]:
            it = result_one_paper.pop(0)
            result_two_paper.pop(0)
            lst_it = list(it)
            lst_it.append(0)
            rst_list.append(lst_it)           

        else:
            chk_loop = 0
            for two_it_loop in range(1, len(result_two_paper)):
                if result_one_paper[0][14] == result_two_paper[two_it_loop][14] and result_two_paper[two_it_loop][0] != None:
                    chk_loop = 1
                    it = result_one_paper.pop(0)
                    result_two_paper.pop(0)

                    lst_it = list(it)
                    lst_it.append(0)
                    rst_list.append(lst_it)
                    break

            if chk_loop == 0:
                it = result_one_paper.pop(0)
                lst_it = list(it) 
                lst_it.append(-2)
                rst_list.append(lst_it)


    # rst_list = []

    # while result_one_paper:


    #     if result_one_paper[0][14] == result_two_paper[0][14] and result_one_paper[0][0] == result_two_paper[0][0] and result_one_paper[0][12] == result_two_paper[0][12]:
    #         if result_one_paper[0][0] != None and result_two_paper[0][0] != None:
    #             it = result_one_paper.pop(0)
    #             result_two_paper.pop(0)
    #             lst_it = list(it)
    #             lst_it.append(0)
    #             rst_list.append(lst_it)
    #         else:
    #             it1 = result_one_paper.pop(0)
    #             it2 = result_two_paper.pop(0)
    #             lst_it1 = list(it1)
    #             lst_it1.append(10)
    #             rst_list.append(lst_it1)
    #             lst_it2 = list(it2)
    #             lst_it2.append(0)
    #             rst_list.append(lst_it2)                  

    #     else:
    #         chk_loop = 0
    #         # for two_it_loop in range(len(result_two_paper)):
    #         #     if result_one_paper[0][14] == result_two_paper[two_it_loop][14]:
    #         #         chk_loop = 1
    #         #         new_it = [result_two_paper.pop(0) for i in range(two_it_loop)]
    #         #         new_it = [list(it) for it in new_it]
    #         #         [it.append(20) if it[0] == None else it.append(2) for it in new_it]
    #         #         # print(new_it)
    #         #         [rst_list.append(it) for it in new_it]
    #         #         it = result_one_paper.pop(0)
    #         #         if it[0] != None:
    #         #             result_two_paper.pop(0)
    #         #             lst_it = list(it)
    #         #             lst_it.append(0)
    #         #             rst_list.append(lst_it)
    #         #         else:
    #         #             result_two_paper.pop(0)
    #         #             lst_it = list(it)
    #         #             lst_it.append(20)
    #         #             rst_list.append(lst_it)  
    #         #         break
    #         for two_it_loop in range(1, len(result_two_paper)):
    #             if result_one_paper[0][14] == result_two_paper[two_it_loop][14]:
    #                 chk_loop = 1
    #                 it = result_one_paper.pop(0)
    #                 result_two_paper.pop(0)
    #                 if it[0] != None:
    #                     lst_it = list(it)
    #                     lst_it.append(0)
    #                     rst_list.append(lst_it)
    #                 else:
    #                     lst_it = list(it)
    #                     lst_it.append(10)
    #                     rst_list.append(lst_it)  
    #                 break

    #         if chk_loop == 0:
    #             it = result_one_paper.pop(0)
    #             if it[0] != None:
    #                 lst_it = list(it) 
    #                 lst_it.append(-2)
    #                 rst_list.append(lst_it)
    #             else:
    #                 lst_it = list(it)
    #                 lst_it.append(10)
    #                 rst_list.append(lst_it) 


    while result_two_paper:
        it = result_two_paper.pop(0)
        lst_it = list(it)
        lst_it.append(2)
        rst_list.append(lst_it)



    # while result_two_paper:
    #     it = result_two_paper.pop(0)
    #     if it[0] != None:
    #         lst_it = list(it)
    #         lst_it.append(2)
    #         rst_list.append(lst_it)
    #     else:
    #         lst_it = list(it)
    #         lst_it.append(20)
    #         rst_list.append(lst_it)  

    # print(rst_list)
    getter_item_code = set(map(itg(15), rst_list))
    getter_item_code = list(getter_item_code)
    new_rst_list = []
    # print(getter_item_code)
    while getter_item_code:
        it_code = getter_item_code.pop(0)
        item_group = []
        for it in rst_list:
            if it[15] == it_code:
                item_group.append(it)
        
        for i, it in enumerate(item_group):
            if it[16] == 10:
                temp = item_group[i]
                item_group[i] = item_group[len(item_group)-3]
                item_group[len(item_group)-3] = temp 
            if it[16] == 20:
                temp = item_group[i]
                item_group[i] = item_group[len(item_group)-2]
                item_group[len(item_group)-2] = temp

        new_rst_list += item_group
                


    # one_pp_loop = 0
    # two_pp_loop = 0
    # save_two_pp_loop = 0
    # for one_pp_loop in range(len(result_one_paper)):
    #     for two_pp_loop in range(save_two_pp_loop, len(result_two_paper)):
    #         if result_one_paper[one_pp_loop][0] != None and result_two_paper[two_pp_loop][0] != None:
    #             if result_one_paper[one_pp_loop][14] == result_two_paper[two_pp_loop][14]:
    #                 temp = list(result_two_paper[one_pp_loop])
    #                 temp.append(0)
    #                 rst_list.append(temp)
    #                 save_two_pp_loop +=1 

    #                 break
    #         if result_two_paper[two_pp_loop][0] == None:
    #             temp = list(result_one_paper[one_pp_loop])
    #             temp.append(-2)
    #             rst_list.append(temp)
    #             break
    #         if result_two_paper[two_pp_loop][0] == None:
    
    # print(rst_list)
    pd.set_option('display.max_row', 500)
    rst = pd.DataFrame(new_rst_list)
    # rst = pd.DataFrame(rst_list)

    # print(rst)
    # rst.to_excel('rst.xlsx')
    return JsonResponse({'cnt' : 'wefwef'})

def ResultOne(request):
    if request.method == "POST":
        date = request.POST['send_date']
        return JsonResponse({'query': 'wef'})
    else:
        date = request.GET.get('send_date')
        date += ' 00:00:00'
        factory_num = request.GET.get('send_factoy_num')
        sub = request.GET.get('send_sub')
        culoms = ['order_num', 'input', 'cmpy_name', 'delivery_part', 'unit', 'item_name', 'zone', 'order_value', 'box_num', 'box', 'pac', 'due_date', 'factory_num', 'sub']
        sql = '''
        SELECT op.order_num, max(op.input), max(op.cmpy_name), max(op.delivery_part), max(op.unit), max(op.item_name), max(op.zone), max(op.order_value), max(it.pac_num),

        sum(CASE
        	WHEN it.unit = 'BOX' AND op.delivery_part='배송' THEN op.order_value
        	WHEN it.unit = 'PAC' AND op.delivery_part='배송' THEN op.order_value DIV it.pac_num
        	WHEN it.unit = 'EA'  AND op.delivery_part='배송' THEN (op.order_value DIV it.ea_num) DIV it.pac_num
        	WHEN it.unit = 'KG'  AND op.delivery_part='배송' THEN (op.order_value DIV it.kg_num) DIV it.pac_num
        	WHEN op.delivery_part='직송' THEN 0
        	ELSE 0
        END)
        box, sum(
        	CASE WHEN op.delivery_part='배송' THEN
        		(CASE
        			WHEN it.unit = 'BOX' THEN 0
        			WHEN it.unit = 'PAC' THEN op.order_value MOD it.pac_num
        			WHEN it.unit = 'EA'  THEN (op.order_value DIV it.ea_num) MOD it.pac_num
        			WHEN it.unit = 'KG'  THEN (op.order_value DIV it.kg_num) MOD it.pac_num
        			ELSE 0
        		end)
        	ELSE 0
        end
        ) pac, max(op.due_date), max(op.factory_num), max(op.subdivision)
        FROM order_paper AS op, item AS it
        WHERE op.due_date='{0}' AND  op.factory_num='{1}' AND op.subdivision='{2}' AND op.item_code=it.item_code
        GROUP BY op.item_code,  op.order_num WITH rollup
        
        '''.format(date, factory_num, '1차')
        cursor = connection.cursor()
        cnt = cursor.execute(sql)
        result_one_paper = cursor.fetchall()
        make_json = []
        dic = {}
        for i, item in enumerate(result_one_paper):
            for j, it in enumerate(item):
               dic[culoms[j]] = it
            make_json.append(dic)
            dic = {}
        # print(make_json)
        return JsonResponse({'query': make_json, 'cnt': cnt})

def AddItem(request):
    #print(request.POST['nickname'])
    #if request.method == "POST":
    #    print(request.POST['nickname'])
    # else:
    items_ob = Item()
    get_code = request.GET.get('code')
    get_nickname = request.GET.get('nickname')
    get_unit = request.GET.get('unit')
    get_bnum = request.GET.get('bnum')
    get_enum = request.GET.get('enum')
    get_knum = request.GET.get('knum')
    get_name = request.GET.get('name')
    # print(get_code)
    # print(get_name)
    items_ob.item_name = get_name
    items_ob.item_code = get_code
    items_ob.item_nick_name = get_nickname
    items_ob.unit = get_unit
    items_ob.box_num = get_bnum
    items_ob.ea_num = get_enum
    items_ob.kg_num = get_knum
    items_ob.save()
    return JsonResponse({'respone': 'success'})

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

class AllowJSONPCallback(object):
    """This decorator function wraps a normal view function                                                                                      
    so that it can be read through a jsonp callback.                                                                                             
                                                                                                                                                 
    Usage:                                                                                                                                       
                                                                                                                                                 
    @AllowJSONPCallback                                                                                                                          
    def my_view_function(request):                                                                                                               
        return HttpResponse('this should be viewable through jsonp')                                                                             
                                                                                                                                                 
    It looks for a GET parameter called "callback", and if one exists,                                                                           
    wraps the payload in a javascript function named per the value of callback.                                                                  
                                                                                                                                                 
    Using AllowJSONPCallback implies that the user must be logged in                                                                             
    (and applies automatically the login_required decorator).                                                                                    
    If callback is passed and the user is logged out, "notLoggedIn" is                                                                           
    returned instead of a normal redirect, which would be hard to interpret                                                                      
    through jsonp.                                                                                                                               
                                                                                                                                                 
    If the input does not appear to be json, wrap the input in quotes                                                                            
    so as not to throw a javascript error upon receipt of the response."""
    def __init__(self, f):
        self.f = login_required(f)

    def __call__(self, *args, **kwargs):
        request = args[0]
        callback = request.GET.get('callback')
        # if callback parameter is present,                                                                                                      
        # this is going to be a jsonp callback.                                                                                                  
        if callback:
            if request.user.is_authenticated():
                try:
                    response = self.f(*args, **kwargs)
                except:
                    response = HttpResponse('error', status=500)
                if response.status_code / 100 != 2:
                    response.content = 'error'
            else:
                response = HttpResponse('notLoggedIn')
            if response.content[0] not in ['"', '[', '{'] \
                    or response.content[-1] not in ['"', ']', '}']:
                response.content = '"%s"' % response.content
            response.content = "%s(%s)" % (callback, response.content)
            response['Content-Type'] = 'application/javascript'
        else:
            response = self.f(*args, **kwargs)
        return response

@AllowJSONPCallback
def MarryData(APIView):
    #print(request.POST['nickname'])
    #if request.method == "POST":
    #    print(request.POST['nickname'])
    # else:
    # q = pd.read_csv('./myy.csv')
    # print(q)
    # get_name = request.GET.get('name')
    return HttpResponse('this should be viewable through jsonp')