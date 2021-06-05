from django.db.models.fields import NullBooleanField
from campaign.models import Campaign, Wallet
from django.db import models
from django.utils.translation import gettext_lazy as _

from campaign.models import Campaign, Wallet

import uuid


class Donor(models.Model):

    name = models.CharField(_("full name"), max_length=255)
    email = models.EmailField(_("email"))


class Donation(models.Model):

    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True)
    donor = models.ForeignKey(Donor, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    note = models.TextField(null=True, blank=True)
    donation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now=True)
