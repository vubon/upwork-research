#!/usr/bin/env bash
DEFAULT_USER="admin"
DEFAULT_EMAIL="admin@mail.com"
DEFAULT_PASS="nothing1234"

######### MAIN CLEAN #########

rm 'db.sqlite3'
readonly virtual='/home/vubon/personal/upwork_env/bin/activate'
source ${virtual}
python manage.py makemigrations
python manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DEFAULT_USER', '$DEFAULT_EMAIL', '$DEFAULT_PASS')" | python manage.py shell --plain