import subprocess

from django.http import HttpResponse
from django.shortcuts import render, redirect
import os
from django.http import HttpResponse, FileResponse
import pandas as pd
from openpyxl import load_workbook

from firstapp.models import Vehicles


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        maxval = request.POST.get('max')
        runtime = request.POST.get('runtime')
        print(name,maxval,runtime)
        try:
            spider_name = 'pakwheelsp'
            process = subprocess.Popen(['scrapy', 'crawl', spider_name])
            process.wait()
            df = pd.read_excel('outputnew.xlsx')
            for index, row in df.iterrows():
                my_model_instance = Vehicles(
                    brand=row['brand'],
                    price=row['price'],
                    location=row['location'],
                    img_url=row['pic'],
                )
                my_model_instance.save()
            return render(request, "firstapp/list.html")
        except Exception as e:
                print('Error', str(e))
    return render(request, "firstapp/list.html")

def running(request):
    return render(request, "firstapp/runing.html")