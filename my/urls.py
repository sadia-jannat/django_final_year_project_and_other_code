"""my URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from .import views


#image add ar jonno
from django.conf import settings
from django.conf.urls.static import static

from myfinal import views

#API
from myfinal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
   
    #bellow path not related our main path
    path('homepage/',views.home), 

    path('',views.indexpage, name='indexpage'),
    path('userform/',views.userform),

    path('test/',views.test),

    path('delete/<int:id>/', views.delete_data, name="deletedata"),

    path('updata_data/<int:id>/', views.update_data, name="updatedata"),



    #house final ar page start
    path('house/', views.house, name='house'),
    path('houseform/', views.houseform, name='houseform'),

    #google map ar jonno
    path('rental/', views.rental, name='rental'),

    path('owner/', views.owner, name='owner'),
    path('search/', views.search, name='search'),   #try for fetch rate
    

    #this signin and login for django UserCreationForm their site use
    path('signup/', views.signup, name='signup'),
    path('uselog/', views.uselog, name='uselog'),
    path('logout/', views.uselogout, name='logout'),

    
    #ownerform page for house details add by house owner that will go to database
    path('ownerform/', views.ownerform, name='ownerform'),

    path('fill/', views.fill, name='fill'),

    path('imgall/', views.imgall, name='imgall'),
    path('dhaka/', views.dhaka, name='dhaka'),
    path('auto/', views.auto, name='auto'),

    path('info/<str:pk>', views.info, name='info'), #details data primary key(pk) ar maddhome dekhabe
    path('save/<int:pid>', views.save, name='save'),
    path('reviewok/', views.reviewok, name='reviewok'), 

    path('recommandation_details/<str:pk>', views.recommandation_details, name='recommandation_details'),

    path('recomitem/<str:pk>', views.recomitem, name='recomitem'),
    
    path('tes/', views.tes, name='tes'),

    path('auto_house/', views.auto_house, name='auto_house'),
    
    path('showhouse/', views.showhouse, name='showhouse'),
    path('details/<int:pk>/', views.details, name='details'),

    path('dashbord/', views.dashbord, name='dashbord'),
    path('dashbord_edit/<int:id>/', views.dashbord_edit, name='dashbordedit'),
    path('dashbord_delete/<int:id>/', views.dashbord_delete, name='dashborddelete'),
 
    
 
   
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


   
