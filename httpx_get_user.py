import httpx
from tools.fakers import get_random_email


create_user_payload = {
  'email': get_random_email(),
  'password': 'string',
  'lastName': 'string',
  'firstName': 'string',
  'middleName': 'string'
}

urls = [
    'http://localhost:8000/api/v1/users',
    'http://localhost:8000/api/v1/authentication/login'
]

with httpx.Client() as client:
    # Создание нового пользователя
    create_user_response = client.post(urls[0], json=create_user_payload)
    create_user_data = create_user_response.json()
    print('Create user data:', create_user_data)

    # Запись необходимых данных в переменные для последующих запросов
    user_email = create_user_payload['email']
    user_password = create_user_payload['password']
    user_id = create_user_data['user']['id']

    # Аутентификация созданного пользователя
    login_payload = {
        'email': user_email,
        'password': user_password
    }

    login_response = client.post(urls[1], json=login_payload)
    login_response_data = login_response.json()
    print('Login data:', login_response_data)

    # Запись необходимых данных в переменные для последующих запросов
    access_token = login_response_data['token']['accessToken']

    # Получение информации о пользователе по его id
    user_headers = {'Authorization': f'Bearer {access_token}'}
    url = f'http://localhost:8000/api/v1/users/{user_id}'

    get_user_response = client.get(url, headers=user_headers)
    get_user_data = get_user_response.json()
    print('Get user data:', get_user_data)
