from django.db import models

class Post(models.Model):
	author = models.ForeignKey('enter.Profile', on_delete=models.CASCADE)
	text = models.TextField(max_length=1000)
	theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		pass
	
class Theme(models.Model):
    """
    Model representation forum themes
    """
    name = models.CharField(max_length=254)
    author = models.ForeignKey('hunter.Project',on_delete=models.CASCADE)
