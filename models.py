from django.db import models

# Create your models here.


#image ar time ,date debr jonno bellow
import datetime
import os

# Create your models here.
class Useri(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)



#project models create

class Userform(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    code=models.CharField(max_length=7)


    def __str__(self):
        return self.code
    


#ownerform name for owner can add his house details

DIVISION=(
    ('Dhaka', 'Dhaka'),
    ('Chattogram', 'Chattogram'),
    (' Khulna', ' Khulna'),
    ('Barishal', 'Barishal'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Mymensingh', 'Mymensingh'),
)

#house-category for ownerform model ar..work
HOUSES=(                
    ('flat', 'flat'),
    ('duplex', 'duplex'),
    ('commercial', ' commercial'),
    ('family_house', 'family_house'),
   
)

#image ar jonno
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Ownerform(models.Model):

    ownername=models.CharField(max_length=100)
    email=models.EmailField()
    ownerpin=models.PositiveIntegerField(default=0)

    housecategory=models.CharField(choices=HOUSES, max_length=100)
    housename=models.CharField(max_length=100)
    

    division=models.CharField(choices=DIVISION, max_length=50)
    district=models.CharField(max_length=100) 
    area=models.CharField(max_length=100)

    housesize=models.CharField(max_length=100)
    bedroom=models.PositiveIntegerField(default=0)
    dinning=models.PositiveIntegerField(default=0)
    drawing=models.PositiveIntegerField(default=0)
    bathroom=models.PositiveIntegerField(default=0) 
    kitchen=models.PositiveIntegerField(default=0)
    balcony=models.PositiveIntegerField(default=0)
    housedetail=models.CharField(max_length=100)  

    img=models.ImageField(upload_to=filepath, null=True, blank=True )

    houserent=models.CharField(max_length=100, default='')
    
    
    


def file(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Item(models.Model):
    
    details = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to=file, null=True, blank=True)





#ownerformfill new create

#division ar list
DIVISION=(                #dity pari nai ata
    ('Dhaka', 'Dhaka'),
    ('Chattogram', 'Chattogram'),
    (' Khulna', ' Khulna'),
    ('Barishal', 'Barishal'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Mymensingh', 'Mymensingh'),
)


#img ar jonno
def fileimg(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)





#house-category for ownerformfill model ar..work
HOUSE_CATEGORY=(                
    ('flat', 'flat'),
    ('duplex', 'duplex'),
    ('commercial', ' commercial'),
    ('family_house', 'family_house'),
   
)

class ownerformfill(models.Model):
    ownername=models.CharField(max_length=100)
    email=models.EmailField()
    phn=models.CharField(max_length=100,default='')  #new add last tai default='' disi    

    housecategory=models.CharField(choices=HOUSE_CATEGORY, max_length=100)
    housename=models.CharField(max_length=100)

    houserent=models.PositiveIntegerField(default=0)
    
    img=models.ImageField(upload_to=fileimg, null=True, blank=True )
    imgidfont=models.ImageField(upload_to=fileimg, null=True, blank=True )
    imgidback=models.ImageField(upload_to=fileimg, null=True, blank=True )
    

    division=models.CharField(max_length=50)   #select dity pari nai..tai choices=DIVIDSION cut korlm
    district=models.CharField(max_length=100) 
    area=models.CharField(max_length=250, verbose_name='Area', blank=True)
    

    housesize=models.IntegerField()
    bedroom=models.PositiveIntegerField(default=0)
    dinning=models.PositiveIntegerField(default=0)
    drawing=models.PositiveIntegerField(default=0)
    bathroom=models.PositiveIntegerField(default=0) 
    kitchen=models.PositiveIntegerField(default=0)
    balcony=models.PositiveIntegerField(default=0)

    allinfo=models.CharField(max_length=100, default='')  #new add last tai default='' disi
    
   
    
    class Meta:
        verbose_name = "Ownerformfill"
        verbose_name_plural = "Ownerformfill"
        


    



    

#RATE AR RAVIEWS AR JONNO
RATING=(
(1, '1'),
(2, '2'),
(3, '3'),
(4, '4'),
(5, '5'),
)

class houserate(models.Model):
    infor_id=models.ForeignKey(ownerformfill, on_delete=models.CASCADE)
    info_review=models.TextField()
    info_rate=models.CharField(choices=RATING, max_length=100)

    def get_info_rate(self):
        return self.info_rate




#map add..vlo tutorial silo..distance shoho map silo,..not work
class measurement(models.Model):
    location=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    distance=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance}km"




#again try map..work
class map(models.Model):
    address=models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.address
        

#Auto search for location last try..not work

class Location(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self) -> str:
       return self.name

