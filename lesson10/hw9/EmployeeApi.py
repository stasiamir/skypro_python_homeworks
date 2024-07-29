import requests
import allure


class EmployeeApi:
    user = 'bloom'
    password = 'fire-fairy'

    def __init__(self, url: str):
        """
        Инициализирует API для работы с сотрудниками.

        :param url: URL для доступа к API.
        """
        self.url = url

    @allure.step("api.получить токен авторизации")
    def get_token(self, user: str = user, password: str = password) -> str:
        """
        Метод получает токен для авторизации.

        :param user: Имя пользователя для авторизации.
        :param password: Пароль для авторизации.
        :return: Токен пользователя.
        :rtype: str
        """
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("api.создать нового сотрудника компании")
    def create_employee(
            self, company_id: int, first_name: str, last_name: str,
            email: str, isActive: bool, id: int = 1,
            middle_name: str = '', url: str = '', phone: str = '',
            birthdate: str = '2005-05-03T11:19:37.153Z') -> dict:
        """
        Метод создает нового сотрудника компании.

        :param company_id: ID компании, в которую будет добавлен сотрудник.
        :param first_name: Имя сотрудника.
        :param last_name: Фамилия сотрудника.
        :param email: Email сотрудника.
        :param isActive: Статус активности сотрудника.
        :param id: ID сотрудника (по умолчанию 1).
        :param middle_name: Отчество сотрудника (по умолчанию '').
        :param url: URL (по умолчанию '').
        :param phone: Телефон сотрудника (по умолчанию '').
        :param birthdate: Дата рождения сотрудника (по умолчанию '2005-05-03T11:19:37.153Z').
        :return: Ответ API с данными нового сотрудника.
        :rtype: dict
        """
        creds = {
            'id': id,
            'firstName': first_name,
            'lastName': last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', headers=my_headers, json=creds)
        return resp.json()

    @allure.step("api.создать несколько - {num_emp} новых сотрудников компании")
    def create_list_employee_get_list_id(
            self, num_emp: int, company_id: int, first_name: str, last_name: str,
            email: str, isActive: bool, id: int = 1,
            middle_name: str = '', url: str = '', phone: str = '',
            birthdate: str = '2005-05-03T11:19:37.153Z') -> list:
        """
        Метод создает несколько сотрудников компании и возвращает их ID.

        :param num_emp: Количество создаваемых сотрудников.
        :param company_id: ID компании, в которую будут добавлены сотрудники.
        :param first_name: Имя сотрудников.
        :param last_name: Фамилия сотрудников.
        :param email: Email сотрудников.
        :param isActive: Статус активности сотрудников.
        :param id: ID сотрудников (по умолчанию 1).
        :param middle_name: Отчество сотрудников (по умолчанию '').
        :param url: URL (по умолчанию '').
        :param phone: Телефон сотрудников (по умолчанию '').
        :param birthdate: Дата рождения сотрудников (по умолчанию '2005-05-03T11:19:37.153Z').
        :return: Список ID созданных сотрудников.
        :rtype: list
        """
        list_new_emp = []
        list_new_emp_id = []
        creds = {
            'id': id,
            'firstName': first_name,
            'lastName': last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        for i in range(num_emp):
            resp = requests.post(self.url + '/employee', headers=my_headers, json=creds)
            resp_json = resp.json()
            list_new_emp.append(resp_json)

        for i in range(len(list_new_emp)):
            emp_full = list_new_emp[i]["id"]
            list_new_emp_id.append(emp_full)

        return list_new_emp_id

    @allure.step("api.создать сотрудника без токена авторизации")
    def create_employee_without_auth_token(
            self, company_id: int, dict_creds_emp: dict) -> dict:
        """
        Метод для проверки возможности создания сотрудника компании
        без токена авторизации.

        :param company_id: ID компании, в которую будет добавлен сотрудник (не используется).
        :param dict_creds_emp: Словарь с данными сотрудника.
        :return: Ответ API с данными нового сотрудника.
        :rtype: dict
        """
        resp = requests.post(self.url + '/employee', json=dict_creds_emp)
        return resp.json()

    @allure.step("api.создать сотрудника без тела запроса")
    def create_employee_without_body(self) -> dict:
        """
        Метод отправляет запрос на создание сотрудника без тела запроса.

        :return: Ответ API.
        :rtype: dict
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', headers=my_headers)
        return resp.json()

    @allure.step("api.получить список сотрудников по параметру - {params}")
    def get_list_employee(self, params: dict) -> list:
        """
        Метод возвращает список словарей с данными сотрудников,
        соответствующих определенному параметру.

        :param params: Параметры для фильтрации списка сотрудников.
        :return: Список сотрудников.
        :rtype: list
        """
        resp = requests.get(self.url + '/employee', params=params)
        return resp.json()

    @allure.step("api.получить сотрудника по id")
    def get_employee_by_id(self, emp_id: int) -> dict:
        """
        Метод получает словарь с информацией о сотруднике по id.

        :param emp_id: ID сотрудника.
        :return: Словарь с данными сотрудника.
        :rtype: dict
        """
        resp = requests.get(self.url + '/employee/' + str(emp_id))
        return resp.json()

    @allure.step("api.получить сотрудника по id без id")
    def get_employee_by_id_without_id(self) -> dict:
        """
        Метод пытается получить сотрудника без указания ID.

        :return: Ответ API.
        :rtype: dict
        """
        resp = requests.get(self.url + '/employee/')
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике - {cred}")
    def change_info_employee(
            self, emp_id: int, api_creds_emp: dict) -> dict:
        """
        Метод находит сотрудника по id и изменяет значение полей.

        :param emp_id: ID сотрудника.
        :param api_creds_emp: Словарь с новыми данными сотрудника.
        :return: Ответ API с обновленными данными сотрудника.
        :rtype: dict
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(self.url + '/employee/' + str(emp_id), headers=my_headers, json=api_creds_emp)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике без токена авторизации")
    def change_info_employee_without_auth_token(
            self, emp_id: int, api_creds_emp: dict) -> dict:
        """
        Метод отправляет запрос на изменение информации о сотруднике
        без токена авторизации.

        :param emp_id: ID сотрудника.
        :param api_creds_emp: Словарь с новыми данными сотрудника.
        :return: Ответ API с обновленными данными сотрудника.
        :rtype: dict
        """
        resp = requests.patch(self.url + '/employee/' + str(emp_id), json=api_creds_emp)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике без id")
    def change_info_employee_without_id(
            self, api_creds_emp: dict) -> dict:
        """
        Метод отправляет запрос на изменение информации о сотруднике
        без ID сотрудника.

        :param api_creds_emp: Словарь с новыми данными сотрудника.
        :return: Ответ API.
        :rtype: dict
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(self.url + '/employee/', headers=my_headers, json=api_creds_emp)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике без тела запроса")
    def change_info_employee_without_body(
            self, emp_id: int) -> dict:
        """
        Метод отправляет запрос на изменение информации о сотруднике
        без тела запроса.

        :param emp_id: ID сотрудника.
        :return: Ответ API.
        :rtype: dict
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(self.url + '/employee/' + str(emp_id), headers=my_headers)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике с несущест. id")
    def change_info_employee_wrong_id(
            self, emp_id: int) -> dict:
        """
        Метод отправляет запрос на изменение информации о сотруднике
        с неправильным ID сотрудника.

        :param emp_id: ID сотрудника.
        :return: Ответ API.
        :rtype: dict
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(self.url + '/employee/' + str(emp_id), headers=my_headers)
        return resp.json()