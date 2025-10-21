from django.db import models

# Create your models here.
class Member(models.Model):
    '''Class defining the club member fields to be stored in the app database.
        
        :param str first_name: Members first name. Max length 25 characters.
        :param str last_name: Members last name/surname/family name. Max length 50 characters.
        :param str id_number: Unique ID number of the member. Usually government issued.
        :param DateField dob: Date of birth of the member.
        :param EmailField email: Email address of the member.
        
    '''

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=20, primary_key=True)
    dob = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)