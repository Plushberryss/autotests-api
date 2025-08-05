import httpx


with httpx.Client() as client:
    # Данные для входа в систему
    login_payload = {
        'email': 'petrov@example.com',
        'password': '12345qwerty'
    }

    # Запрос на аутентификацию
    login_response = client.post(
        'http://localhost:8000/api/v1/authentication/login',
        json=login_payload
    )
    login_response_data = login_response.json()
    # Сохранение access токена в отдельную переменную
    access_token = login_response.json()['token']['accessToken']

    # Данные авторизованного пользователя для передачи в заголовке
    headers = {'Authorization': f'Bearer {access_token}'}

    # Запрос на получение данных о текущем пользователе
    get_user_response = client.get(
        'http://localhost:8000/api/v1/users/me',
        headers=headers
    )
    get_user_response_data = get_user_response.json()

    # Вывод ответа
    print("Status Code:", get_user_response.status_code)
    print("Get user response:", get_user_response_data)
