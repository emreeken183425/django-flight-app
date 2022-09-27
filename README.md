 
 DJANGO PROJE AYAĞA KALDIRMA KOMUTLARI 

 1  python -m venv env
 2  .\env\Scripts\activate
 3  pip install django
 4  python -m pip install --upgrade pip
 5  history
 6  clear
 7  pip list
 8  pip freeze
 9  pip freeze > requirements.txt
 10  django-admin startproject main .
 11  python manage.py runserver
 12 python manage.py startapp student(yeni app için )
 
 pip install python-decouple >> import et
gitignore ile aynı konumda env dosyası oluştur

setting.py içerisindeki SECRET KEY'i >>>>> env file taşı

setting.py file içerisine aşağıdaki komutları çalıştır.

from decouple import config

SECRET_KEY = config('SECRET_KEY')
!!!! SECRET KEY TIRNAKLARINI KALDIR.!!!

 GİTHUB REPODAN PROJE ÇEKİNCE YAPILACAK ADIMLAR

1-python -m venv env
2-env/Scripts/activate
3-pip install -r requirements.txt
4-python.exe -m pip install --upgrade pip
5-pip install python-decouple
6-pip freeze > requirements.txt
7-python manage.py migrate
8-python manage.py createsuperuser
9-python manage.py runserver

KISAYOLDAN ENV HAZIRLAMAK TERMİNALDEN 
'''echo SECRET_KEY=yuliemkauiyemieü234952/4867(ŞİFRE İSTEDİĞİNİ YAZ) > .env'''

Templates
Variables: {{ variable }}
Tags: {% tag %}
Filters : {{ dict1.django|title }}
Comments:: Single line: {# this won't be rendered #}
{# This is a single line comment #}

Multi line: {% comment %}
{% comment %} This is a multi line comment, you can't see it on the page! {% endcomment %}


başlangıç dosyasını almak için aşağıdaki işlemler yapılır

git checkout -b branchname hash(githubdan aldık)
Example: git checkout -b emre 43534546345436346346
1.Reveal in finder aç dosyayı kopyala masaüstüne yapıştır
terminalde 
git checkout main >>>>>ana brancha get
git branch -d branchname >>>branchı sil





