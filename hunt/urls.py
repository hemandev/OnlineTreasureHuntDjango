from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^$', views.home_view, name='home'),
    url(r'^leaderboard/$', views.leaderboard_view, name='leaderboard'),
    url(r'^rules/$', views.rules_view, name='rules'),
    url(r'^arena/$', views.arena_view, name='arena'),
    url(r'^levels/$', views.levels_view, name='levels'),
    url(r'^check_answer/$', views.check_ans_view, name='check')

]
