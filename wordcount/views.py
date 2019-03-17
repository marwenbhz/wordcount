from rest_framework.decorators import api_view
from rest_framework.response import Response
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
            return Response({"status": r.status_code, "count": count})                
        else:
            return Response({"status": r.status_code, "message": "Error in url"})
    except:
        pass   
