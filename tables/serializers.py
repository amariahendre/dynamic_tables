from rest_framework import serializers
from .models import DynamicTable, DynamicTableRow

# Serializer for the DynamicTableRow model.
class DynamicTableRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicTableRow
        fields = ('id', 'data')  # Fields to include when serializing a DynamicTableRow instance.

# Serializer for the DynamicTable model.
class DynamicTableSerializer(serializers.ModelSerializer):
    rows = DynamicTableRowSerializer(many=True, read_only=True)  # Nested serializer for the 'rows' relationship.

    class Meta:
        model = DynamicTable
        fields = ('id', 'name', 'fields_and_titles', 'rows')  # Fields to include when serializing a DynamicTable instance.
