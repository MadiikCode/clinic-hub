from django.db import models
from django.contrib.auth import get_user_model


# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     descriptions = models.TextField()
#     image = models.ImageField(upload_to='category/')
#
#     def __str__(self):
#         return self.name
#
# #
# # class Clinic(models.Model):
# #     name = models.CharField(max_length=100)
# #     descriptions = models.TextField()
# #     location = models.CharField(max_length=100)
# #     image = models.ImageField(upload_to='clinic/')
# #     contact = models.CharField(max_length=100)
# #     email = models.EmailField()
# #     logo = models.ImageField(upload_to='clinic/')
# #    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
# #     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clinics_by_category')
# #     services = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clinics_by_services')
# #     schedule = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clinics_by_schedule')
# #
# #     rating = models.IntegerField()
# #     created_at = models.DateTimeField(auto_now_add=True)
#
#
# class Clinic(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     location = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='clinic/')
#     contact = models.CharField(max_length=100)
#     email = models.EmailField()
#     logo = models.ImageField(upload_to='clinic/')
#
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clinics')
#     schedule = models.OneToOneField('Schedule', on_delete=models.SET_NULL, null=True, blank=True)
#     services = models.ManyToManyField('Service', related_name='clinics')
#
#     rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Schedule(models.Model):
#     work_days = models.CharField(max_length=100)
#     rest_days = models.CharField(max_length=100)
#     start_time = models.CharField(max_length=100)
#     end_time = models.CharField(max_length=100)
#     is_working = models.BooleanField(default=True)
#
#
# class Service(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     duration = models.IntegerField(help_text="Продолжительность в минутах")
#
#     def __str__(self):
#         return self.name
#

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Продолжительность в минутах")

    def __str__(self):
        return self.name


class Schedule(models.Model):
    work_days = models.CharField(max_length=100)  # пример: "Mon-Fri"
    rest_days = models.CharField(max_length=100)  # пример: "Sat-Sun"
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_working = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.work_days} {self.start_time}-{self.end_time}"


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clinics/')
    logo = models.ImageField(upload_to='clinics/')
    contact = models.CharField(max_length=100)
    email = models.EmailField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='clinics')
    services = models.ManyToManyField(Service, related_name='clinics')
    schedule = models.OneToOneField(Schedule, on_delete=models.SET_NULL, null=True, blank=True)

    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WeekDay(models.Model):
    name = models.CharField(max_length=20)
    order = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name