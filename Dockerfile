FROM python 
RUN pip install django==5.2.7
COPY . .
RUN python manage.py migrate
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
