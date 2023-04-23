from django.db import models


CUSTOMER_STATUS_CODES = (
    ('0', 'Inactive'),
    ('1', 'Active'),
)


INVENTORY_STATUS_CODES = (
    ('0', 'Inducted'),
    ('1', 'Order received'),
    ('2', 'Order started'),
    ('3', 'Order completed'),
    ('4', 'Shipped'),
    # Status codes above 1 digit length are
    # only used for Work Orders & WorkOrderOps
    ('999', 'Terminated'),
)


class Toy(models.Model):
    toy_name = models.CharField(max_length=30, blank=False)
    desc = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(default=20000)
    photo = models.ImageField(blank=False, upload_to="photos/%Y/%m/%d/")
    status = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.toy_name


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50, blank=False)
    customer_email = models.EmailField(max_length=50, blank=False)
    customer_ph_number = models.CharField(max_length=11, blank=False)
    customer_address = models.CharField(max_length=200, blank=False, default="Not specified")
    status = models.CharField(max_length=1, choices=CUSTOMER_STATUS_CODES, default=1)
    ordering_toys = models.ManyToManyField(Toy, blank=True)
    createdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.id)
