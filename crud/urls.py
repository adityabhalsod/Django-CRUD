from . import views
from django.urls import path

urlpatterns = [
    path('create',views.create), # create method url
    path('',views.read), # read method url but here, null because type localhost show read view
    path('update/<id>',views.update), # update method url
    path('delete/<id>',views.delete), # delete method url 
]
