# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
'''
主页
未使用模板
'''
'''
def homepage(request):
    posts = models.Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append(b"No.{}:".format(str(count)) + str(post) + b"<hr/>")
        post_lists.append(b"<small>" + str(post.body.encode('utf-8')) + b"</small><br/><br/>")
    
    return HttpResponse(post_lists)
'''

'''
主页
使用模板
'''
def homepage(request):
    template = get_template('index.html')
    posts = models.Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    
    return HttpResponse(html)

'''
文章详细页
'''
def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = models.Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')