from django.contrib import admin

from .models import *

admin.site.register(Service)
admin.site.register(Logo)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('topic', u'discription')
admin.site.register(AboutUs, AboutUsAdmin)


class SettingAdmin(admin.ModelAdmin):
    list_display = ('facebook', 'instagram', 'youtube', 'twitter')
admin.site.register(Settings, SettingAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone_number')
admin.site.register(ContactUs, ContactUsAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_no', 'email', 'address')
admin.site.register(Enquiry, EnquiryAdmin)

admin.site.register(Slider)
admin.site.register(WhyUs)
