from django.db import models
from django.contrib.auth.models import User

# Create your models here        .
class Group(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    start_date = models.DateField()
    total_months = models.IntegerField()
    commision = models.FloatField()
    started = models.NullBooleanField(null=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.BigIntegerField()
    user = models.OneToOneField(User)

class Subscriptions(models.Model):
    member = models.ForeignKey(Customer)
    group = models.ForeignKey(Group)
    comments = models.CharField(max_length=1000)
    auction_amount = models.IntegerField(null=True)
    auction_date = models.DateField(null=True)
    auction_number = models.IntegerField(null=True)
    
class Journal(models.Model):
    member = models.ForeignKey(Customer, null=True)
    amount = models.IntegerField(null=True)
    entry_date = models.DateField()
    comment = models.CharField(max_length=1000)
    AUCTION = 'A'
    PAYMENT = 'P'
    DISBURSEMENT = 'D'
    ENTRY_TYPES = (
        (AUCTION, 'Auction'),
        (PAYMENT, 'Payment'),
        (DISBURSEMENT, 'Disbursement')
    )
    entry_type = models.CharField(max_length=10, choices=ENTRY_TYPES)

class JournalItem(models.Model):
    txn = models.ForeignKey(Journal)
    subscription = models.ForeignKey(Subscriptions)
    debit = models.IntegerField()
    credit = models.IntegerField()
