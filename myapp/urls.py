from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home,name='home'),
    path('', views.HomeView.as_view()),
    path('employees/', views.lvindex.as_view(), name='lvindex'),
    path('pemployees/', views.pindex, name='pindex'),
    path('searchform/', views.search_form, name='searchForm'),
    path('search_res/', views.psearch_res, name='psearch'),
    path('pemployees/add/', views.add, name='add'),
    path('pemployees/add/addrecord/', views.addrecord, name='addrecord'),
    path('pemployees/delete/<int:id>', views.delete, name='delete'),
    path('pemployees/update/<int:id>', views.update, name='update'),
    path('pemployees/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]