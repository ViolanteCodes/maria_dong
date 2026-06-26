from django.contrib import admin
from shorts.models import Short
from shorts.models import ReprintRecord
from shorts.models import ReviewRecord

# Register your models here.
admin.site.register(Short)
admin.site.register(ReviewRecord)
admin.site.register(ReprintRecord)
