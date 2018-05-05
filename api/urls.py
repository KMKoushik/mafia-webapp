from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/createNewGame/$', views.createNewGame, name='createGame'),
    url(r'^api/addRoles/$', views.addRoles, name='createGame'),
    url(r'^api/addPlayer/$', views.addPlayer, name='createGame'),
    url(r'^api/assignRoles/$', views.assignRoles, name='assignRoles'),
    url(r'^api/getRole/$', views.getRole, name='assignRoles'),
    url(r'^api/resetGame/$', views.resetGame, name='assignRoles'),
]