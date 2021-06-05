from django.core import validators
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from datetime import date

from account.models import CustomUser

import uuid



class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(_("slug name"), max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.slug

class Campaign(models.Model):
    '''
    Fundraising Event
    '''

    title = models.CharField(_("title"), max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name="campaign")
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    goal = models.FloatField(_("goal"))
    deadline = models.DateField()

    def __str__(self):
        return self.title

    @property
    def total_donations(self):
        '''
        Get total amount of donations
        '''
        amount = 0
        for donation in self.donations_set.all():
            amount += donation.amount

        return float(amount)

    @property
    def amount_left(self):
        '''
        Get total amount left
        '''

        amount = self.goal - self.total_donations

        if self.total_donations > self.goal:
            amount = float(0)

        return amount

    @property
    def percentage_donated(self):
        '''
        Get percentage of amount donated
        '''

        total_donations = self.total_donations
        percentage = (total_donations/self.goal) * 100

        return percentage

    @property
    def days_left(self):
        '''
        Get days left to campaign's deadline
        '''

        deadline = self.deadline
        todays_date = date.today()

        pass


class CampaignAttachment(models.Model):

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    media_id = models.UUIDField(_('media id'), default=uuid.uuid4, editable=False)
    file = models.FileField(_("file"), upload_to='attachment', validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg','png','mp4'])])
    file_type = models.CharField(_("file type"), max_length=32, blank=True)




class Update(models.Model):

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField()


class Wallet(models.Model):

    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True)
    balance = models.FloatField(default=float(0))

