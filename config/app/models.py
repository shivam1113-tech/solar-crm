from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Qualified', 'Qualified'),
        ('Proposal', 'Proposal'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='New')
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_leads')

    monthly_bill = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    solar_kwh_required = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_customers')

    def __str__(self):
        return self.name
    

# ── Product (Inventory) ──────────────────────────────────────
class Product(models.Model):
    name          = models.CharField(max_length=200)
    brand         = models.CharField(max_length=200, blank=True)
    hsn_code      = models.CharField(max_length=50, blank=True)
    unit          = models.CharField(max_length=50, default='pcs')  # pcs, meter, kg, etc.
    quantity      = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # current stock
    price         = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price per unit
    low_stock_alert = models.DecimalField(max_digits=10, decimal_places=2, default=5)  # warn if below this
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.brand})" if self.brand else self.name

    @property
    def is_low_stock(self):
        return self.quantity <= self.low_stock_alert

    @property
    def total_value(self):
        return self.quantity * self.price


# ── ProjectProduct (products used in a project) ──────────────
class ProjectProduct(models.Model):
    project       = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project_products')
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deducted      = models.BooleanField(default=False)  # True once stock has been deducted

    def __str__(self):
        return f"{self.product.name} x {self.quantity_used} → {self.project.title}"



class Project(models.Model):
    STATUS_CHOICES = [
        ('Planning', 'Planning'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Planning')
    previous_status = models.CharField(max_length=50, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Quote(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Sent', 'Sent'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Draft')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote #{self.id} - {self.lead.name}"


class Invoice(models.Model):
    STATUS_CHOICES = [
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid'),
        ('Overdue', 'Overdue'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Unpaid')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice #{self.id} - {self.customer.name}"
    


class FollowUp(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    follow_up_date = models.DateField()
    follow_up_time = models.TimeField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.lead.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"