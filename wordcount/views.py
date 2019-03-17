from rest_framework.test import APIRequestFactory
from rest_framework.decorators import api_view
from rest_framework.response import Response
import mysql.connector as mariadb
import requests

# Create your views here.
@api_view(["POST"])
def wordcount(request, format=None):

    try:
        url = request.data['url']
    except:
        return Response("No url in input!")
    try:
        word = request.data['word']
    except:
        return Response("No word in input!")
    try:
        r = requests.get(url)
        if r.status_code == 200:
            count = r.text.count(word)
            '''
            # Store to DB.
            mariadb_connection = mariadb.connect(user='root', password='09071992ma', database='wordcount')
            cursor = mariadb_connection.cursor()
            cursor.execute("INSERT INTO wordcount (url,word,status,count) VALUES (%s,%s, %s, %s)", (url,word,status,count))
            mariadb_connection.commit()
            mariadb_connection.close()
            '''
            return Response({"status": r.status_code, "count": count})                
        else:
            return Response({"status": r.status_code, "message": "Error in url"})
    except:
        pass

    # Create a JSON POST request
    factory = APIRequestFactory()
    request = factory.post('/wordcount/', {'url': 'https://www.virtusize.jp/', 'word': 'fit'}, format='json')    
