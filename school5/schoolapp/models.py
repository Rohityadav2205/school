from django.db import models


# Create your models here.
class SchoolModel(models.Model):
    Schoolsname = models.CharField(max_length=200)
    Section = models.CharField(max_length=200)
    Cr = models.CharField(max_length=200)
    Classteachername = models.CharField(max_length=200)


def __str__(self):
    return "Schoolname={0},Section{1},cr{2},Classteacher{3}".format(self.schoolname, self.section, self.cr,
                                                                    self.classteachername)


class SoftwaresModel(models.Model):
    softwarename = models.CharField(max_length=200)
    softwarecreator = models.CharField(max_length=200)
    cr = models.CharField(max_length=200)


def __str__(self):
    return "softwarename={0},softwarecreator{1},cr{2},".format(self.softwarename, self.softwarecreator, self.cr)


class CricketersModel(models.Model):
    cricketername = models.CharField(max_length=200)
    coachname = models.CharField(max_length=200)
    cr = models.CharField(max_length=200)

    crcoachanushka = models.CharField(max_length=200)


def __str__(self):
    return "cricketername={0},coachname{1},cr{2},crcoachanushka".format(self.softwarename, self.softwarecreator,
                                                                        self.cr, self.crcoachanushka)


subjects = (
    (1, 'c'),
    (2, 'java'),
    (3, 'python'),

)


class BooksModel(models.Model):
    bookname = models.CharField(max_length=200)
    subject = models.IntegerField(choices=subjects, default=1)
    price = models.IntegerField()

    def __str__(self):
        return "Bookname={0},subject{1},price{2},".format(self.bookname, self.subject, self.price)


class StatesModel(models.Model):
    statename = models.CharField(max_length=200)

    def __str__(self):
        return "statename={0}".format(self.statename)


class Citymodel(models.Model):
    cityname = models.CharField(max_length=220)

    def __str__(self):
        return "cityname ={0} ".format(self.cityname)
