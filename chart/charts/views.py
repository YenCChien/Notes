from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from . import SQLite
from os import listdir
from os.path import isfile, join
import json

table = ""
db = ""
# print('-----{}'format(os.getcwd()))
User = get_user_model()
class HomeView(View):
    def get(self, request, *args, **kwargs):
        table = ""
        if 'mySelect' in request.GET:
            global db
            db = request.GET['mySelect']
            print(request.GET['mySelect'])
        elif 'myTable' in request.GET:
            global table
            table = request.GET['myTable']
            print(request.GET['myTable'])
        return render(request, 'charts.html', {})

def get_data(request, *args, **kwargs):
    print(request.GET['mySelect'])
    data = {
        "mySelect": request.GET['mySelect'],
    }
    return JsonResponse(data) # http response

class DataView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        mypath = 'C:/Users/nick/chart/sqlite'
        dbfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        qs_count = User.objects.all().count()
        labels = []
        default_items = []
        tablelist = []
        if db:
            global table, db
            sql = SQLite.SQLite('C:/Users/nick/chart/sqlite/{}'.format(db),'ABCDEFG')
            sql.connect()
            sql.cursor()
            # if not table:
            # print("'{}'".format(table))
            # table = "'PHY21-ABCDEFG-201710131155'"
            # print(table)
            alltable = sql.table()
            for tname in alltable:
                tablelist.append(tname[1])
            # tablelist=json.dumps(tablelist)
            if table:
                table = "'{}'".format(table)
                alldata = sql.select(table)
                for i in alldata:
                    labels.append(i[0])
                    default_items.append(i[4])
            sql.close()
        # print(labels)
        # print('-----------{}'.format(default_items))
        # labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        # default_items = [2.2, 23, 2, 3, 12, 2]
        data = {
            "dbfiles": dbfiles,
            "labels": labels,
            "default": default_items,
            "tables": tablelist,
        }
        
        return Response(data)

