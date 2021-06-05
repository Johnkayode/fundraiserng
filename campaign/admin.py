from django.contrib import admin

from .models import Category, Campaign, CampaignAttachment, Update, Comment, Wallet


admin.site.register(Category)
admin.site.register(Campaign)
admin.site.register(CampaignAttachment)
admin.site.register(Update)
admin.site.register(Comment)
admin.site.register(Wallet)