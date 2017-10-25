netstat -ntlp
sudo lsof -t -i tcp:80 | xargs kill -9
python manage.py runserver 0.0.0.0:80
