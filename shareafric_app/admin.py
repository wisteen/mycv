from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *
from django import forms

# class IndividualRegistrationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone','country_of_origin')
#     list_filter = ('name', 'email','phone', 'country_of_origin', 'state_region' )
#     search_fields = ('name', 'email', 'phone', 'country_of_origin', 'state_region', 'sector')

# admin.site.register(ContactUs)
# admin.site.register(Webdata)
# admin.site.register(Service)
# admin.site.register(SkillRight)
# admin.site.register(SkillLeft)
# admin.site.register(Client)

# admin.site.register(Summary)

# admin.site.register(Facts)

# admin.site.register(Education)
# admin.site.register(Experience)
# admin.site.register(Portfolio)

# Custom admin class for Feedback model
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']

# Custom admin class for Webdata model
class WebdataAdmin(admin.ModelAdmin):
    list_display = ['logo', 'phone', 'email', 'location']

# Custom admin class for Client model
class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'quote']

# Custom admin class for Service model
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'service_brief_description', 'service_link']

# Custom admin class for SkillRight model
class SkillRightAdmin(admin.ModelAdmin):
    list_display = ['skill_title', 'skill_percent']

# Custom admin class for SkillLeft model
class SkillLeftAdmin(admin.ModelAdmin):
    list_display = ['skill_title', 'skill_percent']

# Custom admin class for Summary model
class SummaryAdmin(admin.ModelAdmin):
    list_display = ['name', 'about_me', 'phone', 'email']

# Custom admin class for Education model
class EducationAdmin(admin.ModelAdmin):
    list_display = ['certificate', 'school', 'location', 'year_range']

# Custom admin class for Experience model
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['experience', 'organisation', 'location', 'year_range']

# Custom admin class for ContactUs model
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']

# Custom admin class for Facts model
class FactsAdmin(admin.ModelAdmin):
    list_display = ['happy_clients', 'project', 'hours_of_support', 'award_and_certifications']

# Custom admin class for Portfolio model
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['category', 'link', 'image']

# Register the custom admin classes
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Webdata, WebdataAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SkillRight, SkillRightAdmin)
admin.site.register(SkillLeft, SkillLeftAdmin)
admin.site.register(Summary, SummaryAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Facts, FactsAdmin)
admin.site.register(Portfolio, PortfolioAdmin)




AdminSite.index_title = 'Wisteen Admin'  # Replace with your desired index title
AdminSite.site_title = 'Wisteen Dashboard'  # Replace with your desired site title