from django.contrib import admin
from django.urls import path
from mlearn.apps.mlr import views as mlr_views 
from . views import index, loginView, logoutView, lineChart

urlpatterns = [
    
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("login/", loginView, name="login"),
    path("logout/", logoutView, name="logout"),
    path("chart/", lineChart, name="chart"),
    
    # multiple linear regression
    path("training", mlr_views.training, name="training"),
    path("multiple", mlr_views.multiple, name="multiple"),
    path("process", mlr_views.process, name="process"),
    path("update", mlr_views.update, name="update"),

]
