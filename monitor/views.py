#coding=utf-8
from django.http import HttpRequest,request
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from monitor import models
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session

# Create your views here.
def tick():
    print('Tick! The time is: %s' % datetime.now())
tick()
#scheduler = BlockingScheduler()
#scheduler.add_job(tick,'cron', second='44,45,46,47,48,49,50,51,52', hour='*')




'''
def index(request):
    return render(request, "index.html")
'''

@login_required
def index(request):
 if request.method == 'GET':
    ip_time = []
    alipay = []
    wxpay = []
    ccb =  []
    succee =  []
    fail =  []
    for i in models.mpay.objects.raw('''select id,to_char(ip_time,'mm-dd hh24:mi') as ip_time,alipay,wxpay,ccb,succee,fail from monitor_mpay where rownum<=6 order by ip_time asc'''):
        ip_time.append(str(i.ip_time))
#        ip_time.append((i.ip_time).strftime('%Y-%m-%d %H:%M'))
        alipay.append(i.alipay)
        wxpay.append(i.wxpay)
        ccb.append(i.ccb)
        succee.append(i.succee)
        fail.append(i.fail)
        print ip_time,fail
    return render_to_response("index.html", RequestContext(request, {'ip_time': ip_time, 'alipay': alipay, 'wxpay':wxpay , 'ccb':ccb ,
                                                                     'succee':succee,'fail': fail }))