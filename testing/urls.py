from django.conf.urls import url, include

from testing import views


urlpatterns = [
    url('TESTING', views.test_python, name='test_python'),
]