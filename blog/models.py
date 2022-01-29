from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100,blank=True )
    description = models.TextField(max_length=250, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

    def smartdate(self):
        return self.date.strftime("%A %d %B %Y") # abbrievation of the month name and %e is for the day
    
    def summary(self):
        return self.description[:100] # to show only 100 caracters of the body text os change it on your html
