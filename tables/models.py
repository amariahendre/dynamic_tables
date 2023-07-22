from django.db import models

# Represents a dynamic table with customizable fields and titles.
class DynamicTable(models.Model):
    name = models.CharField(max_length=255, default='userTable')  # Field to store the name of the table
    fields_and_titles = models.JSONField()  # JSONField to store dynamic fields and titles.

# Represents a row in a DynamicTable.
class DynamicTableRow(models.Model):
    table = models.ForeignKey(DynamicTable, related_name='rows', on_delete=models.CASCADE)
    data = models.JSONField()  # JSONField to store the data for this row.
