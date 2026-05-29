# django_app

Plain Django app for adding employees to an in-memory employee list.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Open http://127.0.0.1:8000/.

## Notes

- Django project: `test_app_1`
- App: `employees`
- No database models are used.
- Employee entries are stored in memory and reset when the server restarts.
