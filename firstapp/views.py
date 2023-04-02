import subprocess
import pandas as pd
from firstapp.models import Vehicles
from django.shortcuts import render

'''
view first call the scrapy crawl and scrapy save all the data inside an excel file.
thenwe use pd to read that data fastly and making a bulk create highly efficient orm
query to insert all the data in db. we can do all the stuff without django but then
we cannot havae the beautiful admin panel which djago provides with few lines of code
'''
def home(request):
    if request.method == "POST":
        # three unnecessary params to limit things for future use
        name = request.POST.get("name")
        maxval = request.POST.get('max')
        runtime = request.POST.get('runtime')
        try:
            spider_name = 'pakwheelsp'
            process = subprocess.Popen(['scrapy', 'crawl', spider_name])
            process.wait()
            df = pd.read_excel('outputnew.xlsx')
            Vehicles.objects.bulk_create((Vehicles(
                brand=row['brand'],
                price=row['price'],
                location=row['location'],
                img_url=row['pic']
            ) for index, row in df.iterrows()))
            return render(request, "firstapp/list.html")
        except Exception as e:
                print('Error', str(e))
    return render(request, "firstapp/list.html")


'''
just a simple view for testing purpose.
'''
def running(request):
    return render(request, "firstapp/runing.html")