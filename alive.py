import time
import requests

BASE_URL="https://addressformatterapi.herokuapp.com"
while True:
    time.sleep(600)
    status = requests.get(BASE_URL).status_code