from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.forms.models import model_to_dict
from .models import User
from django.contrib import messages
import json

# 로그인
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        try:
            User.objects.get(user_id=user_id)
            if user_pw == User.objects.get(user_id=user_id).user_pw:
                user = User.objects.get(user_id=user_id)
                request.session['user_id'] = user_id
                return HttpResponseRedirect('/map/main/')
                # return render(request, 'mapAPI/main_v2.0.html', {'user':user})
            else :
                return HttpResponseRedirect('/map/main/')
        except :
            print('except')
            return HttpResponseRedirect('/map/main/')
    else :
        return HttpResponseRedirect('/map/main/')
# 로그아웃
def logout(request):
    request.session.modified = True
    del request.session['user_id']
    return HttpResponseRedirect('/map/main/')

# 회원가입
def join(request):
    print(1111)
    if request.method == 'POST':
        try:
            user_id = request.POST.get('join_id')
            User.objects.get(user_id = user_id)
            return HttpResponseRedirect('/map/main/')
        except:
            user_id = request.POST.get('join_id')
            user_pw = request.POST.get('join_pw')
            user_email = request.POST.get('join_email')
            user_dog = request.POST.get('join_dog')
            User.objects.create(user_id=user_id, user_pw=user_pw, user_email=user_email, user_dog=user_dog)
            return HttpResponseRedirect('/map/main/')
    else:
        return HttpResponseRedirect('/map/main/')

# 중복 아이디 확인
def id_check(request):
    user_id = request.GET.get('user_id')
    try:
        user = User.objects.get(user_id = user_id)
    except:
        #중복 검사 성공
        user = None
    if user is None:
        overlap = "pass"
    else :
        overlap = "fail"
    context = {'overlap': overlap}
    return JsonResponse(context)   

# 비밀번호 확인
def pw_check(request):
    user_pw = request.GET.get('join_pw')
    user_pw2 = request.GET.get('join_pw2')
    if user_pw == user_pw2:
        context ={'overlap' : 'pass'}
    else :
        context ={'overlap' : 'fail'}
    return JsonResponse(context)

# 회원정보 확인
def user_info(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(user_id=user_id)
    return JsonResponse(model_to_dict(user), safe=False)

# 회원정보 수정
def modi_info(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.get(user_id=user_id)
        user.user_id = request.POST.get('user_id')
        user.user_pw = request.POST.get('user_pw')
        user.user_email = request.POST.get('user_email')
        user.user_dog = request.POST.get('user_dog')
        user.save()
        request.session['user_id'] = user.user_id
        return HttpResponseRedirect('/map/main/')
    else :
        return HttpResponseRedirect('/map/main/')
#회원 탈퇴
def user_drop(request):
    user = User.objects.get(user_id=request.session['user_id'])
    user.delete()
    request.session.modified = True
    del request.session['user_id']
    return HttpResponseRedirect('/map/main/')
