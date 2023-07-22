from rest_framework import generics
from .models import DynamicTable, DynamicTableRow
from .serializers import DynamicTableSerializer, DynamicTableRowSerializer

# View to create a new DynamicTable instance.
class DynamicTableCreateView(generics.CreateAPIView):
    queryset = DynamicTable.objects.all()  # Queryset of all DynamicTable instances.
    serializer_class = DynamicTableSerializer  # Serializer class used for creating DynamicTable instances.

# View to retrieve and update an existing DynamicTable instance.
class DynamicTableUpdateView(generics.RetrieveUpdateAPIView):
    queryset = DynamicTable.objects.all()  # Queryset of all DynamicTable instances.
    serializer_class = DynamicTableSerializer  # Serializer class used for retrieving and updating DynamicTable instances.
    lookup_url_kwarg = 'id'  # The URL keyword argument used to lookup the DynamicTable instance.

# View to create a new DynamicTableRow instance associated with a DynamicTable.
class DynamicTableRowCreateView(generics.CreateAPIView):
    queryset = DynamicTableRow.objects.all()  # Queryset of all DynamicTableRow instances.
    serializer_class = DynamicTableRowSerializer  # Serializer class used for creating DynamicTableRow instances.
    lookup_url_kwarg = 'id'  # The URL keyword argument used to lookup the DynamicTable for association.

    def perform_create(self, serializer):
        # Custom method to associate the created DynamicTableRow with a DynamicTable.
        table_id = self.kwargs['id']  # Extract the 'id' from the URL.
        table = DynamicTable.objects.get(pk=table_id)  # Get the corresponding DynamicTable instance.
        serializer.save(table=table)  # Save the DynamicTableRow instance with the associated DynamicTable.

# View to list all DynamicTableRow instances associated with a DynamicTable.
class DynamicTableRowListView(generics.ListAPIView):
    serializer_class = DynamicTableRowSerializer  # Serializer class used for serializing DynamicTableRow instances.

    def get_queryset(self):
        table_id = self.kwargs['id']  # Extract the 'id' from the URL.
        try:
            table = DynamicTable.objects.get(pk=table_id)  # Get the corresponding DynamicTable instance.
            return DynamicTableRow.objects.filter(table=table)  # Filter DynamicTableRow instances associated with the DynamicTable.
        except DynamicTable.DoesNotExist:
            return []  # Return an empty queryset if the DynamicTable does not exist.
