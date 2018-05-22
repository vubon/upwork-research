#!/usr/bin/env bash
##!/usr/bin/env bash
#DEFAULT_USER="admin"
#DEFAULT_EMAIL="admin@mail.com"
#DEFAULT_PASS="nothing1234"
#
#function usage
#{
#    echo "usage: $0 [-r | --runserver]"
#}
#
#runserver=
#
#while [ "$1" != "" ]; do
#    case $1 in
#        -r | --runserver )      runserver=1
#                                ;;
#        -h | --help )           usage
#                                exit
#                                ;;
#        * )                     usage
#                                exit 1
#    esac
#    shift
#done
#
#
######### MAIN CLEAN #########
## rm website.db
#python manage.py syncdb --noinput
#python manage.py migrate
#
#### Create super-user
## echo "from django.contrib.auth.models import User; User.objects.create_superuser('$DEFAULT_USER', '$DEFAULT_EMAIL', '$DEFAULT_PASS')" | python manage.py shell --plain
#
#
######### OPTIONAL RUNSERVER ########
#if [ "$runserver" = "1" ]; then
#	python manage.py runserver
#fi
#

# rm 'db.sqlite3'
git add .
git commit -m"checking"
git status
git push origin master