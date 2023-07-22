# Dynamic Tables App

**dynamic_tables** is a Django app that allows users to dynamically create and manage tables with custom fields and titles. It provides an API to create tables and add rows to them, respecting the table schema. All API calls are handled by Django REST framework, and Postgres is used as the database backend.

## Features

- Create dynamic tables with custom field types and titles.
- Update the structure of dynamically generated tables.
- Add rows to the tables, respecting the table schema.
- Retrieve all rows associated with a specific table.

## Requirements

- Python 3.7 or higher
- Django 3.2
- Django REST framework
- PostgreSQL

## Installation

1. Clone the repository:
git clone https://github.com/amariahendre/dynamic_tables.git
cd dynamic_tables


2. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate # On Windows, use "venv\Scripts\activate"

3. Install the required packages:
pip install -r requirements.txt


4. Setup the PostgreSQL database:

- Create a new PostgreSQL database for the project.
- Update the database settings in `dynamic_tables_project/settings.py` with your database credentials.

5. Apply the database migrations:
python manage.py migrate


6. Run the development server:
python manage.py runserver



7. Now you can access the API at `http://127.0.0.1:8000/api/`.

## API Endpoints

- `POST /api/table/`: Generate a dynamic Django model based on user-provided fields types and titles.
- `PUT /api/table/:id`: Update the structure of a dynamically generated model.
- `POST /api/table/:id/row`: Add rows to the dynamically generated model, respecting the model schema.
- `GET /api/table/:id/rows`: Get all the rows in the dynamically generated model.

## Example Usage

1. Create a table:
curl -X POST http://127.0.0.1:8000/api/table/ -H "Content-Type: application/json" -d '{
"name": "EmployeeTable",
"fields_and_titles": [
{"title": "Name", "field_type": "string"},
{"title": "Age", "field_type": "number"},
{"title": "Is Employed", "field_type": "boolean"}
]
}'


2. Add a row to the "EmployeeTable":
curl -X POST http://127.0.0.1:8000/api/table/1/row/ -H "Content-Type: application/json" -d '{
"data": {
"Name": "John Doe",
"Age": 30,
"Is Employed": true
}
}'


3. Get all rows of the "EmployeeTable":
curl http://127.0.0.1:8000/api/table/1/rows/



## License

This project is licensed under the [MIT License](LICENSE).







