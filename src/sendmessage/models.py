from django.db import models


YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)

class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, default="null")
    number = models.CharField(max_length=50)
    grade = models.CharField(max_length=50, blank=True, null=True)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.firstname


class Message(models.Model):
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # sender =
    recipient = models.ForeignKey(Group)

    def __str__(self):
        return self.timestamp