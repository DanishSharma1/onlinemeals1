from django.urls import path
from.import views

urlpatterns = [
    path('index/',views.index,name="index"),
    #path('',views.xyz),
    path('index/add/',views.add, name='add'),
    path('index/add/hotel/',views.hotel,name='hotel'),
    path('index/add/hotel/addrecord/',views.addrecord, name='addrecord'),
    path('index/add/delete/<int:id>',views.delete,name='delete'),
    path('index/add/update/<int:id>',views.update,name='update'),
    path('index/add/update/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),

]