from django.db import models
# from users.get_usernames import current_request
from users.models import User
from users.get_usernames import current_request

class Client(models.Model):
    CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    name_of_customer = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    test_provided = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    referral_name = models.CharField(max_length=150)
    discount = models.CharField(max_length=3, choices=CHOICES)
    amount_given = models.DecimalField(max_digits=1000000, decimal_places=2)
    provided_test_results = models.CharField(max_length=250)
    date_of_arrival = models.DateField(auto_now=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name_of_customer)
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    
    def save(self, *args, **kwargs):
        '''Automatically generate registry number'''
        if not self.id:
            self.user = current_request().user
        return super(Client, self).save(*args, **kwargs)
