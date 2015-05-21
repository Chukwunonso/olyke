"""
Use python to send cd into manage.py folder to ensure gunicorn runs
on project path.
"""

import os

os.system("gunicorn olyke.wsgi:application -w 2 -b :8000")
