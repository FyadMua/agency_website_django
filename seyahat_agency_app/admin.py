from django.contrib import admin
from seyahat_agency_app.models import PackageModel, CategoryModel, Comment, Setting, Image, Reservation, FAQ, SocialMedia
# Register your models here.
admin.site.register(PackageModel)
admin.site.register(CategoryModel)
admin.site.register(Comment)
admin.site.register(Setting)
admin.site.register(Image)
admin.site.register(Reservation)
admin.site.register(SocialMedia)
admin.site.register(FAQ)

