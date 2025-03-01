from django.db import models

class FundraisingCampaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='campaign_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title
