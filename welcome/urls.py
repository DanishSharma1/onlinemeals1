from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="index"),
    #path('',views.xyz),
    path('add/',views.add, name='add'),
    path('add/hotel/',views.hotel,name='hotel'),
    path('add/hotel/addrecord/',views.addrecord, name='addrecord'),
    path('add/delete/<int:id>',views.delete,name='delete'),
    path('add/update/<int:id>',views.update,name='update'),
    path('add/update/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),

]
