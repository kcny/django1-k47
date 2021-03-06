from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __strr__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __strr__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __strr__(self):
        return str(self.date)
