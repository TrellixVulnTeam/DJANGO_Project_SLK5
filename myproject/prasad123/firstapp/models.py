from django.db import models

# Create your models here.
 
class Candidate(models.Model):
    name = models.CharField(max_length =264)
    marks = models.IntegerField()
    
    def __str__(self):
        return (self.name + " " + str(self.marks))
    
class Entry(models.Model):
    name = models.CharField(max_length =264)
    marks = models.IntegerField()
    
    def __str__(self):
        return (self.name + " " + str(self.marks))
    