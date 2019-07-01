from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.response import Response
from .models import Greeting
from django.http import JsonResponse
import os
from gettingstarted.settings import BASE_DIR
import random
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



def get_event_names(request):
    # p=BASE_DIR+ '\\hello\\DataFile\\total_tweets.json'
    # json_data = open(p)
    # data = json.load(json_data)
    # event="1"
    # currentList=[]
    # for json_obj in data:
    #     if json_obj['event']!=event:
    #         filename =BASE_DIR+ '\\hello\\DataFiles\\'+ event + '.json'
    #         with open(filename, 'a') as out_json_file:
    #             # Save each obj to their respective filepath
    #             # with pretty formatting thanks to `indent=4`
    #             json.dump(currentList, out_json_file, indent=4)
    #         event=json_obj['event']
    #         currentList=[]
    #         currentList.append(json_obj)
    #     else:
    #         currentList.append(json_obj)
    # filename = BASE_DIR + '\\hello\\DataFile\\' + event + '.json'
    # with open(filename, 'a') as out_json_file:
    #     json.dump(currentList, out_json_file, indent=4)
    event_names=["NEWTOT", "LIVARS", "CHEMCI", "MUNTOT", "MUNMCI", "NEWMCI", "MUNCHE", "TOTMCI", "NEWCHE", "TOTCHE", "CHEARS", "NEWLIV", "MUNNEW", "TOTMUN", "TOTARS", "NEWMUN", "MUNLIV", "NEWARS", "MUNARS"]

    return HttpResponse(json.dumps(event_names),status=status.HTTP_200_OK)

def get_sample_data(request,event_name, count):
    p =  '\\hello\\DataFiles\\'+event_name+'.json'
    json_data = open(p)
    data = json.load(json_data)
    s=random.sample(data,count)
    j=json.dumps(s)
    return HttpResponse(j,status=status.HTTP_200_OK,content_type="application/json")


def get_tweet_with_id(request,event_name, tweet_id):
    p =  '\\hello\\DataFiles\\'+event_name+'.json'
    json_data = open(p)
    data = json.load(json_data)
    for json_obj in data:
        if json_obj['tweet_id'] == tweet_id:
            j=json.dumps(json_obj)
            return HttpResponse(j,status=status.HTTP_200_OK,content_type="application/json")
    return HttpResponse("tweet not found", status=status.HTTP_204_NO_CONTENT)

