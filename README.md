# Backend Coding Test - Word Counter
Design an API which counts how many times a word exists in a webpage 
source.
## Getting Started
Design an API with Django Rest API.
## Django Rest API:
Django REST framework is apowerful and flexible toolkit for building Web 
APIS.
## Prerequisites
```pip install -r requirements.txt```
## Clone the project and run.
```cd wordcount``` ```python3 manage runserver```
## Deployment
This deployed to ec2 instance. 
[wordcount](http://3.209.30.156:8000/wordcount/) 
http://3.209.30.156:8000/wordcount/
## Test
Post: { "word": "fit", "url": "https://www.virtusize.jp/"}
![alt text](https://image.noelshack.com/fichiers/2019/11/7/1552852584-screen5.png)
## Result
{"status": 200,"count": 5}
