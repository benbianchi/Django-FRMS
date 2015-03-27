from django.db import models


# Create your models here.

ClubOptions = (
    (1, 'Special Interest'),
    (2, 'Club Sports'),
    (3, 'Campus Wide'),
    (4, 'Selective Membership'),
    (5,'Greek-life'),
    (6,'Provinsial'),
)

class Club(models.Model):
	"""
	Description: Model Description
	"""
    # i++;
	clubID=models.AutoField(primary_key=True)
	officerAlias = models.CharField(default="",max_length=50,verbose_name="Officer Email Alias")
	shortName = models.CharField(default="",max_length=20,verbose_name="Colloquial Name for Club")
	numMembers = models.IntegerField(default=0,verbose_name="Number of Active Members")
	clubPurpose = models.TextField(default="",max_length=256,verbose_name="Club's Purpose")
	clubClass = models.IntegerField(max_length=2,choices=ClubOptions,default=1,verbose_name="Club Class")
	def __str__(self):
		return self.shortName


requestTypeOptions = ((1, 'Funding Request'),(2, 'Sponsorship'))

class Funding(models.Model):
    """
    Description: Model Description
    """
    requestinfo = models.TextField(max_length=512,verbose_name="Event Summary")
    requestNumber = models.AutoField(primary_key=True)


class Request(models.Model):
    requestNumber=models.ForeignKey(Funding)
    requestAmount = models.FloatField()
    requestDescription = models.TextField()
    outcome = models.TextField()
    reviewDate = models.DateField()
    requestType = models.IntegerField(choices=requestTypeOptions,default=1)
    clubID = models.ForeignKey('Club')
    
class Budget(models.Model):
    """
    Description: Model Description
    """
    year = models.IntegerField();
    budgetAmount = models.FloatField()
    clubID = models.ForeignKey('Club')


