from django.contrib import admin
from .models import Lead, Customer, Project, Quote, Invoice, Task, FollowUp

admin.site.register(Lead)
admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Quote)
admin.site.register(Invoice)
admin.site.register(Task)
admin.site.register(FollowUp)