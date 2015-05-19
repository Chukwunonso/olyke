"""
Use python to send cd into manage.py folder to ensure gunicorn runs
on project path.
"""

import os

os.system("cd olyke && gunicorn olyke.wsgi:application --bind 0.0.0.0:8000")
