import  httpx
from tools.fakers import get_random_email


payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

url = 'http://localhost:8000/api/v1/users'

with httpx.Client() as client:
    response = client.post(url, json=payload)
    print(response.text)
    print(response.status_code)
