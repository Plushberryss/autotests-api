import httpx


with httpx.Client() as client:
    # Данные для входа в систему
    login_payload = {
        'email': 'petrov@example.com',
        'password': '12345qwerty'
    }

    # Выполняем запрос на аутентификацию
    login_response = client.post(
        'http://localhost:8000/api/v1/authentication/login',
        json=login_payload
    )
    login_response_data = login_response.json()

    # Сохраняем токены в отдельные переменные для удобства
    access_token = login_response.json()['token']['accessToken']
    refresh_token = login_response.json()['token']['refreshToken']

    # Выводим полученные токены
    print("Login response:", login_response_data)
    print("Status Code:", login_response.status_code)

    # Формируем payload для обновления токена
    refresh_payload = {'refreshToken': refresh_token}

    # Выполняем запрос на обновление токена
    refresh_response = client.post(
        'http://localhost:8000/api/v1/authentication/refresh',
        json=refresh_payload
    )
    refresh_response_data = refresh_response.json()

    # Выводим обновленные токены
    print("Refresh response:", refresh_response_data)
    print("Status Code:", refresh_response.status_code)

