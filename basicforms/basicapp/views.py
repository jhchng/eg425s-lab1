from django.shortcuts import render
from . import forms
from rest_framework import viewsets
from rest_framework import permissions
#from basicapp.serializers import UserSerializer
import re
import pymongo
from datetime import datetime as dt

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request,'basicapp/form_page.html',{'form':form})

def viewdevices(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["UIOT"]
    mycol = mydb["Devices"]
    devconncol = mydb["DeviceConns"]
    viewdevices = []
    viewdeviceconns=[]
    for device in mycol.find():
        viewdevices.append(device)
        print(device)
    for devconns in devconncol.find():
        viewdeviceconns.append(devconns)
        print(devconns)
    return render(request, 'basicapp/viewdevices.html',context={'viewdevicesdata':viewdevices, 'viewdeviceconndata':viewdeviceconns})

def devices(request,param1):
    data = str(request)
    devname = param1
    dtnow = dt.now()
    #x = re.split("/", data)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["UIOT"]
    mycol = mydb["Devices"]
    devconncol = mydb["DeviceConns"]
    mydict = { "name": devname, "datetime": dtnow }
    viewdevices = []
    for device in mycol.find({'name':devname}):
        viewdevices.append(device)
    print(viewdevices)
    print(len(viewdevices))
    if (len(viewdevices) >= 1):
        mydictconn={ "name": devname, "datetime": dtnow, "status":"updated" }
        y = devconncol.insert_one(mydictconn)
        dev_name = "{} updated in DB".format(devname)
    else:
        x = mycol.insert_one(mydict)
        mydictconn={ "name": devname, "datetime": dtnow, "status":"new" }
        y = devconncol.insert_one(mydictconn)
        dev_name = "{} device has been recorded!!".format(devname)
    print(dev_name)
    return render(request, 'basicapp/devices.html', context={'data': dev_name})

#class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all().order_by('name')
    #myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    #mydb = myclient["mydatabase"]
    #mycol = mydb["customers"]
    #mydict = { "name": "John", "address": "Highway 37" }
    #x = mycol.insert_one(mydict)
    #print("Inserting data - Views")
    #serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class DeviceViewSet(viewsets.ModelViewSet):
    print("Inserting data - Views")
