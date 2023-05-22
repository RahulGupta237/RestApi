
from dataclasses import replace
import re
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import os
import json
import traceback
# from grpc import Status
import requests
from django.http import HttpResponse
from django.conf import settings
# from gui.functions import string_to_list, readJsonFileData, readJsonFileDatainList
from django.views.decorators.cache import cache_control
from EtlApp.service import do_login, file_upload
# service_url = settings.BACKEND_URL
# FRONT_URL = settings.FRONT_URL

# Create your views here.
def Login(request):
    request.session.flush()
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        try:
            email = request.POST['username']
            password = request.POST['password']
            request.session['username'] = email
            DATA = {'email': request.POST['username'],
                    'password': request.POST['password']}

            response = do_login(DATA)
            print('response>>>>>', response)

            # if username == 'brandiq-admin' and password == 'brandiq@123':
            #     user = authenticate(username=username, password=password)
            #     form = login(request, user)
            #     request.session.set_expiry(3000)
            #     return redirect('index')
            # else:
            #     messages.info(request, f'Username Or Password Is Incorrect')
            # if response['message'] == 'Login Success':
            #     request.session['_token_'] = response['token']
            #     request.session['user_id'] = response['id']
            #     request.session.set_expiry(90000)
            #     return redirect('uploadPdf')
            # else:
            #     messages.info(request, f'Username Or Password Is Incorrect')
            if response['status']==200:
            #     request.session.set_expiry(3000)
            #     return redirect('index')
                  request.session['_token_'] = response['token']["access"]
                 
                  return redirect('uploadPdf')
            else:
                 messages.info(request, f'Username Or Password Is Incorrect')
            
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + " " + str(trace_back)
            messages.info(request, f'Username OR Password Is Incorrect')
            print(message)

    form = AuthenticationForm()
    return render(request, 'gui/login.html', {'form': form, 'title': 'login'})

def uploadPdf(request):
    try:
        if request.method == 'POST':
            token=request.session['_token_'] 
            print(token)
            file = request.FILES['file']
            # url = 'https://example.com/upload'  # replace with your API endpoint
            files = {'file': file}
            print(files)
            response=file_upload(files,request.session['_token_'] )
            print("SucessFully Working")
            print("hello",response)
            if response["status"]==200:
                print("successfully uploaded")

            return render(request, '404.html', {},)
        else:

        

            return render(request, 'gui/neurovision-upload.html')
    except:
         return render(request, '404.html', {},)

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        url = 'https://example.com/upload'  # replace with your API endpoint
        files = {'file': file}
        response = requests.post(url, files=files)
        # do something with the API response
    return render(request, 'upload.html')