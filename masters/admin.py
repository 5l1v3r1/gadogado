from django.contrib import admin
from .models import Adult, Kid,Membership
from .models import Publisher,Author,Book



class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1
    

        
class AdultAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['first_name','last_name','gender', 'mobile_no','email', 'city','postcode','state','country','is_active']}),
        ('Date information', {'fields': ['date_joined','date_left'], 'classes': ['collapse']}),
        ('Others information', {'fields': ['line1','line2','line3'], 'classes': ['collapse']}),
    ]
    list_filter = ('gender','country')
    list_per_page = 20
    inlines = (MembershipInline,)
    search_fields = ('first_name',)
    list_display = ('colored_first_name','first_name','last_name','gender', 'mobile_no','email', 'city','postcode','state','country', 'date_joined', 'date_left','is_active')



class KidAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['first_name','last_name','gender', 'mobile_no','email']}),
        ('Date information', {'fields': ['date_joined','date_left'], 'classes': ['collapse']}),
    ]
    list_filter = ('gender',)
    list_per_page = 20
    inlines = (MembershipInline,)
    search_fields = ('first_name',)
    list_display = ('first_name','last_name','gender', 'mobile_no','email', 'date_joined', 'date_left')
    

admin.site.register(Adult,AdultAdmin)
admin.site.register(Kid,KidAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)