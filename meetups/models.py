from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'

# (the location and meetup has one-to-many relationship)

# class Participant(models.Model):
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.email

class Meetup(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(unique=True) #text that adheres to the slug format so there's no whitespace. Ps: can i use the uniqyue keyword fora username?
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE) #you show relationship between id's by calling them into another class they are related to.
    # participants = models.ManyToManyField(Participant, blank=True, null=True) #setting blank to true means that we don't need to provide a related record when creating a new meetup. Null=True doesn't have effect on manyToMany field


    def __str__(self):
        return f'{self.title} - {self.slug}'
