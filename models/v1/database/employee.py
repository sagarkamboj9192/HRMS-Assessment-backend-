from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "departments"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    full_name = models.CharField(
        max_length=255
    )
    email = models.EmailField(
        unique=True
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.full_name} ({self.id})"

    class Meta:
        db_table = "employees"
        indexes = [models.Index(fields=["email"])]
        ordering = ["-created_at"]
    
