from django.db import models

# Create your models here.
BOOK_CATEGORY=(('Electronics','ECE'),('Computers','CSC'),('Civil','CIVIL'),('Human Resoures','HR'),('Finance','FIN'),('Marketing','MKT'))


AVILABLE=(('Yes','Y'),('No','N'))

class Book(models.Model):

    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    edition=models.IntegerField()
    category=models.CharField(choices=BOOK_CATEGORY,max_length=50)
    publisher=models.CharField(max_length=50)
    reviews=models.FloatField()
    avilable=models.CharField(choices=AVILABLE,max_length=50)
    issued_date=models.DateTimeField()
    return_date = models.DateTimeField()

    def __str__(self):

        return '{} - {}'.format(self.name,self.edition)


