from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Topic



def index(request):
    list_of_topics = Topic.objects.order_by('title')
    main_cover = None;
    woman_topic_shoes = None;
    woman_topic_accessories = None;
    woman_topic_clothes = None;
    new_entry = None;
    promotion_woman = None;
    promotion_man = None;
    for topic in list_of_topics:
        if topic.category == 'main_cover':
            main_cover = topic
        if topic.category == 'woman_topic' and topic.title == 'calçados':
            woman_topic_shoes = topic
        if topic.category == 'woman_topic' and topic.title == 'acessórios':
            woman_topic_accessories = topic
        if topic.category == 'woman_topic' and topic.title == 'roupas':
            woman_topic_clothes = topic
        if topic.category == 'new_entry':
            new_entry = topic
        if topic.category == 'promotion_woman':
            promotion_woman = topic
        if topic.category == 'promotion_man':
            promotion_man = topic


    template = loader.get_template('index.html')
    context = {
        'main_cover':main_cover,
        'woman_topic_clothes' : woman_topic_clothes,
        'woman_topic_accessories' : woman_topic_accessories,
        'woman_topic_shoes' : woman_topic_shoes,
        'new_entry' : new_entry,
        'promotion_woman': promotion_woman,
        'promotion_man' : promotion_man,
    }
    return HttpResponse(template.render(context, request))