from django.contrib import admin


from .models import SchoolModel
from  .models import SoftwaresModel
from  .models import CricketersModel
from . models import BooksModel
from . models import  StatesModel
from . models import  Citymodel
# Register your models here.
admin.site.register(SchoolModel)
admin.site.register(SoftwaresModel)
admin.site.register(CricketersModel)
admin.site.register(BooksModel)
admin.site.register(StatesModel)
admin.site.register(Citymodel)