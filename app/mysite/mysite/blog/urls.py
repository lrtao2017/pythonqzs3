#!/usr/bin/env python 
__author__ = "lrtao2010"

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name="blog_title"),
]

