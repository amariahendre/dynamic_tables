from django.urls import path
from tables.views import (
    DynamicTableCreateView,
    DynamicTableUpdateView,
    DynamicTableRowCreateView,
    DynamicTableRowListView,
)

urlpatterns = [
    path('api/table/', DynamicTableCreateView.as_view(), name='create_table'),
    # Endpoint to create a new DynamicTable. HTTP POST to /api/table/

    path('api/table/<int:id>/', DynamicTableUpdateView.as_view(), name='update_table'),
    # Endpoint to update an existing DynamicTable. HTTP PUT to /api/table/{id}/

    path('api/table/<int:id>/row/', DynamicTableRowCreateView.as_view(), name='add_row'),
    # Endpoint to add a new row to a DynamicTable. HTTP POST to /api/table/{id}/row/

    path('api/table/<int:id>/rows/', DynamicTableRowListView.as_view(), name='get_rows'),
    # Endpoint to get all rows of a DynamicTable. HTTP GET to /api/table/{id}/rows/
]
