from django.db import models
from hrm_backend.models.v1.database.employee import Employee


class Attendance(models.Model):

    STATUS_CHOICES = [
        ("present", "Present"),
        ("absent", "Absent"),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    marked_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "attendance"
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "date"],
                name="unique_employee_attendance_per_day"
            )
        ]
        ordering = ["-date"]

    def __str__(self):
        return f"{self.employee.full_name} - {self.date} - {self.status}"