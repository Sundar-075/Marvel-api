from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from decouple import config
import datetime
from hashlib import md5
from rest_framework.response import Response
# Create your views here.

gateway_url = "https://gateway.marvel.com"
private_key = config('PRIVATE_API_KEY')
public_key = config('PUBLIC_API_KEY')


@api_view(["GET", "POST"])
def get_characater_with_name(request):

    name = request.data

    m = md5()
    ts = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    ts_byte = bytes(ts, 'utf-8')  # This converts the timestamp into a byte

    m.update(ts_byte)  # encode converts into bytes
    m.update(private_key.encode('utf-8'))
    m.update(public_key.encode('utf-8'))

    hash = m.hexdigest()
    # print(config('PUBLIC_API_KEY'))
    name = request.GET.get("name")
    print(name)
    # print(config('PUBLIC_API_KEY'))
    # print(hash, ts)
    params = {
        'name': name, 'apikey': str(public_key), 'ts': ts, 'hash': hash, 'limit': 5}
    character_info = requests.get("https://gateway.marvel.com/v1/public/characters",
                                  params=params, headers={'Accept': '*/*'})

    return Response(character_info.json())
