from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout, login

app_name = 'registration'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'registration/login.html',
                             'redirect_authenticated_user': True}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^profiles/$', views.profiles, name="profiles"),
    url(r'^profiles/edit/$', views.edit_profiles, name="edit_profiles"),
    url(r'^profiles/change_password/$', views.changePassword, name="change_password"),
]