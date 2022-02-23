from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from mlearn.apps.mlr.models import Dataset
from django.db.models import Sum
import json
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def loginView(request):
    if request.method == "POST":

        username_login = request.POST['username']
        password_login = request.POST['password']
        
        user = authenticate(request, username=username_login, password=password_login)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username Atau Password tidak sesuai!')
        return redirect('login')


    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'accounts/login.html')

@login_required
def logoutView(request):
    if request.method == "POST":
        logout(request)

        return redirect('index')

    return render(request, 'accounts/logout.html')


def lineChart(request):
    data =[]
    # p = 0
    # for i in range(11):
    #     p = p + 1
    #     produksi = Dataset.objects.filter(bulan=p).aggregate(produksi=Sum('hasil_produksi'))
   
    #produksi = Dataset.objects.filter(bulan='1').aggregate(produksi=Sum('hasil_produksi'))
    #data = json.dumps(produksi)
    # for entry in produksi:
    #     data.append(entry[produksi])
    jan =   Dataset.objects.filter(bulan='1').aggregate(produksi=Sum('hasil_produksi'))
    data.append(jan["produksi"])
    feb =   Dataset.objects.filter(bulan='2').aggregate(produksi=Sum('hasil_produksi'))
    data.append(feb["produksi"])
    mar =   Dataset.objects.filter(bulan='3').aggregate(produksi=Sum('hasil_produksi'))
    data.append(mar["produksi"])
    apr =   Dataset.objects.filter(bulan='4').aggregate(produksi=Sum('hasil_produksi'))
    data.append(apr["produksi"])
    mei =   Dataset.objects.filter(bulan='5').aggregate(produksi=Sum('hasil_produksi'))
    data.append(mei["produksi"])
    jun =   Dataset.objects.filter(bulan='6').aggregate(produksi=Sum('hasil_produksi'))
    data.append(jun["produksi"])
    jul =   Dataset.objects.filter(bulan='7').aggregate(produksi=Sum('hasil_produksi'))
    data.append(jul["produksi"])
    agt =   Dataset.objects.filter(bulan='8').aggregate(produksi=Sum('hasil_produksi'))
    data.append(agt["produksi"])
    sep =   Dataset.objects.filter(bulan='9').aggregate(produksi=Sum('hasil_produksi'))
    data.append(sep["produksi"])
    okt =   Dataset.objects.filter(bulan='10').aggregate(produksi=Sum('hasil_produksi'))
    data.append(okt["produksi"])
    nov =   Dataset.objects.filter(bulan='11').aggregate(produksi=Sum('hasil_produksi'))
    data.append(nov["produksi"])
    des =   Dataset.objects.filter(bulan='12').aggregate(produksi=Sum('hasil_produksi'))
    data.append(des["produksi"])
    return JsonResponse(data = {
        'labels': ["Januari", "Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November", "Desember",],
        #'default': [3796021, 6139452, 7383764, 6294813, 5069996, 5375692, 7024194, 6801511, 7045971, 7280953, 5378355, 5375143,],
        'default':data,
    })
    # contex = {
    #     'labels': ["Januari", "Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November", "Desember",],
    #     'default': data,
    # }

    # return (request,'index.html', contex)
