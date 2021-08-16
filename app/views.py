# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pandas as pd
from django.contrib.staticfiles.storage import staticfiles_storage
from .trend_equipment import predict_equipment
from .trend_place import predict_place
from datetime import date, datetime, timedelta
from .trainning_place import train_place
from .trianing_equipment import train_equi
import threading
from .scrapper import scrap_data

from .filter import get_csv, update_data
scrap_time = datetime(2020, 12, 1, 5, 15, 00)
scrap_h = scrap_time.strftime('%H')
scrap_m = scrap_time.strftime("%M")
raw_path = staticfiles_storage.path('csv/raw_data.csv')
filt_path = staticfiles_storage.path('csv/filt.csv')
filt_equi_path = staticfiles_storage.path('csv/test_equi.csv')
filt_state_path = staticfiles_storage.path('csv/test_place.csv')
path_equi = staticfiles_storage.path('csv/equi.csv')
path_state = staticfiles_storage.path('csv/state.csv')
data_scrap = pd.read_csv(staticfiles_storage.path("csv/test_equi.csv"))
dum = data_scrap.values.tolist()

t_date = int(dum[-1][0].split("-")[2])
t_month = int(dum[-1][0].split("-")[1])
t_year = int(dum[-1][0].split("-")[0])
prev_date = date(t_year, t_month, t_date)
today_date = datetime.now().date()

trained_time = date(2020, 11, 29)
next_train_time = (trained_time + timedelta(7))
def printit():
    global next_train_time
    threading.Timer(5.0, printit).start()
    a = str(datetime.now().strftime('%H:%M:%S'))
    hour = int(a.split(":")[0])
    minute = int(a.split(":")[1])
    second = int(a.split(":")[2])
    if(hour==int(scrap_h) and minute == int(scrap_m) and second>=0 and second<5):
        no_day = int(str(today_date - prev_date).replace("days", "").replace("day", "").split(",")[0])
        print("no of days", no_day)
        print("Scrapping Started")
        scrap_time  = str(datetime.now())
        scrap_data(t_date, t_month, raw_path)
        get_csv(raw_path, filt_path, path_equi, path_state)
        update_data(filt_equi_path, filt_state_path, path_equi, path_state, 5)
    no_day_train = int(str(next_train_time - today_date).replace("days", "").replace("day","").split(",")[0])
    if(no_day_train == 7):
        trained_time = str(datetime.now())
        next_train_time = trained_time + timedelta(days=7)
        train_equi(staticfiles_storage.path('csv/test_equi.csv'))
        train_place(staticfiles_storage.path('csv/test_place.csv'))
printit()


def region_data(csv_path, drop = True):
    df = pd.read_csv(csv_path)
    # drop karili 1st column ta
    if drop:
        df = df.drop(['Unnamed: 0'], axis=1)
    ph_state = df.values.tolist()
    # date column ku convert karili pd ra date time format re
    df['date'] = pd.to_datetime(df['date'])
    # sei date time wala column ku index set karili to make it time series
    df = df.set_index(pd.DatetimeIndex(df['date']))
    # then index column banigala pare date column ku drop kari deli
    df = df.drop(['date'], axis=1)
    # then stackoverflow ru code utheili
    GB = df.groupby([(df.index.year), (df.index.month)]).sum()
    y = GB.index.tolist()
    final = GB.values.tolist()

    month_converter = {1: "January", 2: "February", 3: "March", 4: "April",
                       5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
                       10: "October", 11: "November", 12: "December"}
    for i in range(len(y)):
        final[i].insert(0, month_converter[y[i][1]] + ',' + str(y[i][0]))
    return final, ph_state

def equip_data(csv_path, drop = True):
    data_collected = 0
    df = pd.read_csv(csv_path)
    # drop karili 1st column ta
    if(drop):
        df = df.drop(['Unnamed: 0'], axis=1)
    ph_equip = df.values.tolist()
    # date column ku convert karili pd ra date time format re
    df['date'] = pd.to_datetime(df['date'])
    # sei date time wala column ku index set karili to make it time series
    df = df.set_index(pd.DatetimeIndex(df['date']))
    # then index column banigala pare date column ku drop kari deli
    df = df.drop(['date'], axis=1)
    # then stackoverflow ru code utheili
    GB = df.groupby([(df.index.year), (df.index.month)]).sum()
    y = GB.index.tolist()
    final = GB.values.tolist()
    month_converter = {1: "January", 2: "February", 3: "March", 4: "April",
                       5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
                       10: "October", 11: "November", 12: "December"}
    for i in range(len(y)):
        final[i].insert(0, month_converter[y[i][1]] + ',' + str(y[i][0]))
        final[i].append(final[i][1] + final[i][2] + final[i][3] + final[i][4])
        data_collected += final[i][5]
    return final, data_collected, ph_equip


@login_required(login_url="/login/")
@csrf_exempt
def index(request):
    final, data_collected, ph_equip = equip_data(staticfiles_storage.path('csv/equip_hist.csv'))
    _final , processed_data, latest_equi = equip_data(staticfiles_storage.path('csv/test_equi.csv'), False)
    reg, ph_state = region_data(staticfiles_storage.path('csv/state_hist.csv'))
    _, latest_place = region_data(staticfiles_storage.path('csv/test_place.csv'), False)
    p_state = latest_place
    p_equip = latest_equi
    context = {"data_received": len(pd.read_csv(staticfiles_storage.path("csv/scrapped_backup.csv"), encoding= "latin").index)+1,'processed_data': processed_data}
    context['prev_month'] = final[-2][0].split(",")[0]
    context['prev_month_data'] = final[-2][5]
    context['current_month'] = _final[-1][0].split(",")[0]
    context['current_month_data'] = _final[-1][5]
    context['both_month'] = _final[-1][5] + final[-2][5]
    context['difference'] = ((abs(final[-1][5] - final[-2][5]))/final[-2][5])*100
    context['tom_equip'] = predict_equipment(2)
    context['tom_state'] = predict_place(2).tolist()
    context['eh_month'] = [item[0] for item in _final][-12:]
    context['eh_surgery'] = [item[1] for item in _final][-12:]
    context['eh_scanner'] = [item[2] for item in _final][-12:]
    context['eh_ventilator'] = [item[3] for item in _final][-12:]
    context['eh_microscope'] = [item[4] for item in _final][-12:]
    context['eh_total'] = [item[5] for item in _final][-12:]
    context['ph_equip_date'] = [item[0] for item in latest_equi][-7:]
    context['ph_surgery'] = [item[1] for item in latest_equi][-7:]
    context["ph_scanner"] = [item[2] for item in latest_equi][-7:]
    context["ph_ventilator"] = [item[3] for item in latest_equi][-7:]
    context['ph_microscope'] = [item[4] for item in latest_equi][-7:]
    context['sh_month'] = [item[0] for item in reg][-6:]
    context['sh_delhi'] = [item[1] for item in reg][-6:]
    context['sh_up'] = [item[2] for item in reg][-6:]
    context['sh_maharastra'] = [item[3] for item in reg][-6:]
    context['sh_rajasthan'] = [item[4] for item in reg][-6:]
    context['sh_bengal'] = [item[5] for item in reg][-6:]
    context['ph_state_date'] = [item[0] for item in latest_place][-7:]
    context['ph_delhi'] = [item[1] for item in latest_place][-7:]
    context['ph_up'] = [item[2] for item in latest_place][-7:]
    context['ph_maharastra'] = [item[3] for item in latest_place][-7:]
    context['ph_rajasthan'] = [item[4] for item in latest_place][-7:]
    context['ph_bengal'] = [item[5] for item in latest_place][-7:]
    context['p_state_date'] = [item[0] for item in latest_place][-3:]
    context['p_delhi'] = [item[1] for item in latest_place][-3:]
    context['p_up'] = [item[2] for item in latest_place][-3:]
    context['p_maharastra'] = [item[3] for item in latest_place][-3:]
    context['p_rajasthan'] = [item[4] for item in latest_place][-3:]
    context['p_bengal'] = [item[5] for item in latest_place][-3:]
    context['p_equip_date'] = [item[0] for item in latest_equi][-3:]
    print(latest_equi[-3:])
    context['p_surgery'] = [item[1] for item in latest_equi][-3:]
    context["p_scanner"] = [item[2] for item in latest_equi][-3:]
    context["p_ventilator"] = [item[3] for item in latest_equi][-3:]
    context['p_microscope'] = [item[4] for item in latest_equi][-3:]
    context['trained_time'] = trained_time
    context['next_train'] = next_train_time
    context["before_equipment"] = latest_equi[-7][1:]
    context['after_equipment'] = predict_equipment(7)
    context['before_place'] = latest_place[-7][1:]
    context['after_place'] = predict_place(7).tolist()
    context['equi_csv'] = [item for item in latest_equi][-100:]
    context['place_csv'] = [item for item in latest_place][-100:]
    if (scrap_time):
        context['last_scrap_date'] = scrap_time
    if (request.POST.get('option') and request.POST['name']=="state_day_option"):
        print("Requested")
        option = int(request.POST['option'])
        print("THe option from selector", option)
        last_date, last_month, last_year = int(latest_place[-1][0].split("-")[2]), int(latest_place[-1][0].split("-")[1]), int(latest_place[-1][0].split("-")[0])
        latest_date = datetime(last_year, last_month, last_date)
        for i in range(option):
            a = predict_place(i+1)
            a = a.tolist()
            next_date = (latest_date + timedelta(i + 1)).date()
            a.insert(0, next_date)
            # a.insert(0, last_year+"-"+last_month+"-"+str(last_date+i+1))
            p_state.append(a)
        json_data = {'status': 'success'}
        json_data["p_state_date"] =[item[0] for item in p_state][-1*(option+3):]
        json_data["p_delhi"] = [item[1] for item in p_state][-1*(option+3):]
        print(json_data["p_delhi"])
        json_data["p_up"] = [item[2] for item in p_state][-1*(option+3):]
        json_data["p_maharastra"] = [item[3] for item in p_state][-1*(option+3):]
        json_data['p_rajasthan'] = [item[4] for item in p_state][-1*(option+3):]
        json_data["p_bengal"] = [item[5] for item in p_state][-1*(option+3):]
        return JsonResponse(json_data)
    if (request.POST.get('option') and request.POST['name']=="equip_day_option"):
        print("Requested")
        option = int(request.POST['option'])
        print("THe option from selector", option)
        last_date, last_month, last_year = int(latest_equi[-1][0].split("-")[2]), int(latest_equi[-1][0].split("-")[1]), int(latest_equi[-1][0].split("-")[0])
        latest_date = datetime(last_year, last_month, last_date)
        for i in range(option):
            a = predict_equipment(i+1)
            next_date = (latest_date + timedelta(i+1)).date()
            # a.insert(0, last_year+"-"+last_month+"-"+str(last_date+i+1))
            a.insert(0, next_date)
            p_equip.append(a)
        json_data = {'status': 'success'}
        json_data["p_equip_date"] = [item[0] for item in p_equip][-1*(option+3):]
        json_data["p_surgery"] =[item[1] for item in p_equip][-1*(option+3):]
        json_data["p_scanner"] = [item[2] for item in p_equip][-1*(option+3):]
        json_data["p_ventilator"] = [item[3] for item in p_equip][-1*(option+3):]
        json_data['p_microscope'] = [item[4] for item in p_equip][-1*(option+3):]
        return JsonResponse(json_data)

    context['segment'] = 'index'
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")

def pages(request):
    context = {}

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template   = request.path.split('/')[-1]
        context['segment'] = load_template
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
