from django.conf.urls import url
from . import views

app_name = 'pools'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='details'),
    url(r'^(?P<pk>\d+)/results/', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/', views.vote, name='vote'),
]


# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<question_id>\d+)/$', views.detail, name='details'),
#     url(r'^(?P<question_id>\d+)/results/', views.results, name='results'),
#     url(r'^(?P<question_id>\d+)/vote/', views.vote, name='vote'),
# ]