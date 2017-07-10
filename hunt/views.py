from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm, LevelForm
from .facebook import FacebookHelper
from .models import UserModel, LevelModel
from django.http import JsonResponse




# Create your views here.


def login_user(request):
    details = None

    if request.GET.get('code', None) is not None:
        code = request.GET['code']
        facebook_helper = FacebookHelper(code)
        details = facebook_helper.get_details()
        request.session['uid'] = details['id']
        request.session['name'] = details['name']

    if UserModel.objects.filter(uid__exact=request.session['uid']).exists():
        return redirect('hunt:arena')

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_data = login_form.save(commit=False)
            user_data.name = request.session['name']
            user_data.uid = request.session['uid']
            user_data.save()
            print(user_data)
            return redirect('hunt:arena')

    else:
        login_form = LoginForm()

    return render(request, 'hunt/login.html', {'form': login_form})


def home_view(request):
    return render(request, 'hunt/home.html')


def rules_view(request):

    return render(request, 'hunt/rules.html')


def leaderboard_view(request):

    user_object = UserModel.objects.all()
    users = []
    for i in range(len(user_object)):

        details = {'name': user_object[i].name,
                   'college': user_object[i].college,
                   'level': user_object[i].level}
        users.append(details)
    sorted_list = sorted(users, key=lambda x: x['level'], reverse=True)

    return render(request, 'hunt/leaderboard.html', {'list': sorted_list})


def arena_view(request):
    if request.session.get('uid', None) is None:
        return redirect('hunt:home')
    else:
        user = UserModel.objects.get(uid__exact=request.session['uid'])
        level_no = user.level
        try:
            level = LevelModel.objects.get(level_no__exact=level_no)
        except:
            return render(request, 'hunt/arena.html', {'level': False})
        print("PATH" + level.question_image.path)

        return render(request, 'hunt/arena.html', {'level': level, 'user': user})


def levels_view(request):
    if request.session.get('uid', None) is None:
        return redirect('hunt:home')
    else:
        level_form = LevelForm()

    if request.method == 'POST':
        level_form = LevelForm(request.POST)
        if level_form.is_valid():
            level_form.save(commit=True)
            return render(request, 'hunt/levels.html', {'form': level_form, 'success': True})

    return render(request, 'hunt/levels.html', {'form': level_form, 'success': False})


def check_ans_view(request):
    if request.session.get('uid', None) is None:
        return redirect('hunt:home')
    else:

        user = UserModel.objects.get(uid__exact=request.session['uid'])
        level_no = user.level
        level = LevelModel.objects.get(level_no__exact=level_no)
        ans = level.answer

        if request.method == 'POST':
            answer = request.POST['answer']
            if str(answer).lower().strip() == str(ans).lower().strip():
                user.level += user.level
                user.save()
                return JsonResponse({'answer': True})

            else:
                return JsonResponse({'answer': False})

