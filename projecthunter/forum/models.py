from django.db import models

class Post(models.Model):
	author = models.ForeignKey('enter.Profile', on_delete=models.CASCADE)
	text = models.TextField(max_length=1000)
	theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.theme.name}: {self.author}'
	
class Theme(models.Model):
    """
    Model representation forum themes
    """
    name = models.CharField(max_length=254)
    author = models.ForeignKey('enter.Profile',on_delete=models.CASCADE)
    def __str__(self):
    	return f'{self.name}: {self.author}'