from django.contrib import admin

# Register your models here.



from myfinal.forms import houserateform

# Register your models here.
from .models import Useri
@admin.register(Useri)
class UserAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'email', 'password')
    
        

#project models registra

from .models import Userform
@admin.register(Userform)
class UserformAdmin(admin.ModelAdmin):
    list_display=( 'id', 'name', 'email', 'password','code')


#image ar jonno check page
from .models import Item
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=( 'details', 'image')    


##ownerform name for owner can add his house details ..
# it is from model and model name is ownerform**
# new admin a class name ownerformadmin***
 
from  .models import Ownerform  
@admin.register(Ownerform)
class OwnerformAdmin(admin.ModelAdmin):
    list_display =( 'id', 'ownername', 'email', 'ownerpin', 'housecategory', 'housename', 'division',
    'district', 'area', 'housesize', 'bedroom', 'dinning', 'drawing', 'bathroom', 'kitchen', 'balcony',
    'housedetail', 'img', 'houserent')




#new ownerformfill model create and here fillAdmin create

from  .models import ownerformfill  
@admin.register(ownerformfill)

class tonni(admin.ModelAdmin):
    list_display= ('id', 'ownername', 'email',  'housecategory','housename','houserent','img','imgidfont','imgidback',
    'division','district', 'area', 'housesize', 'bedroom', 'dinning', 'drawing', 'bathroom', 'kitchen', 
    'balcony', 'allinfo', 'phn')






#rating anothor admin for model houserate
from .models import houserate
@admin.register(houserate)
class houseratereg(admin.ModelAdmin):
    list_display=('infor_id', 'info_review', 'info_rate', 'get_info_rate')



#map add
from .models import measurement
@admin.register(measurement)
class mapreg(admin.ModelAdmin):
    list_display=()



#again map add..work
from .models import map
@admin.register(map)
class mymapreg(admin.ModelAdmin):
    list_display=()




#auto Location model try
from .models import Location
@admin.register(Location)
class Locationreg(admin.ModelAdmin):
    list_display=()


