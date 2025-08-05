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
    print(f'Create user status code: {create_user_response.status_code}')
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
    print(f'Login response status code: {login_response.status_code}')
    print('Login data:', login_response_data)

    # Запись необходимых данных в переменные для последующих запросов
    access_token = login_response_data['token']['accessToken']

    # Обновление данных пользователя
    patch_payload = {
        'email': get_random_email(),
        'lastName': 'string',
        'firstName': 'string',
        'middleName': 'string'
    }
    user_headers = {'Authorization': f'Bearer {access_token}'}
    url = f'http://localhost:8000/api/v1/users/{user_id}'

    patch_user_response = client.patch(url, headers=user_headers, json=patch_payload)
    patch_user_data = patch_user_response.json()
    print(f'Patch user response status code: {patch_user_response.status_code}')
    print(f'Patch user data: {patch_user_data}')