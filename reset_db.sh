python manage.py dumpdata lol > temp_data.json
python manage.py reset lol
python manage.py syncdb
python manage.py loaddata temp_data.json
