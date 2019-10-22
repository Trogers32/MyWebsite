from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime, timedelta
import bcrypt
import pytz


def index(request):
    return render(request, "home/index.html") 