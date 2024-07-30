import pytest
from faker import Faker

from EmployeeApi import EmployeeApi
from CompanyApi import CompanyApi

base_url = 'https://x-clients-be.onrender.com'

emp = EmployeeApi(base_url)
com = CompanyApi(base_url)
fake = Faker("ru_RU")

first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
middle_name = fake.first_name_male()
is_active = True
id = 1
phone = fake.random_number(digits=11, fix_len=True)
birthdate = '2005-04-26T11:19:37.153Z'
url = fake.url()

new_last_name = 'Changed2'
new_email = 'string34@gh.ru'
new_url = 'https://sky.pro/wiki/python'
new_phone = '89018765523'
new_is_active = False


def test_get_list_employee():
    # Создание новой компании
    new_company = com.create_company('Компания для получения списка сотрудников 8')
    company_id = new_company["id"]

    # Создание трёх новых сотрудников для компании
    for i in range(3):
        emp.create_employee(
            company_id, first_name, last_name, email, is_active)

    result = emp.get_list_employee(params_to_add={'company': company_id})

    # Проверка, что количество сотрудников равно 3
    assert len(result) == 3

    # будет проверка из базы данных


@pytest.mark.xfail(reason="Ожидается статус 400, но возвращается 500")
def test_get_list_employee_without_company_id():
    com.create_company('Компания для получения списка сотрудников 8')

    result = emp.get_list_employee_without_company_id()
    assert result["statusCode"] == 400
    assert result["message"] == 'Bad Request'


def test_create_employee():
    # Создание новой компании
    new_company = com.create_company('Компания для нового сотрудника 8')
    company_id = new_company["id"]

    # Проверка, что у созданной компании нет сотрудников
    emp_list_f = emp.get_list_employee(params_to_add={'company': company_id})
    len_before = len(emp_list_f)
    assert len(emp_list_f) == 0

    # Создание нового сотрудника
    new_emp = emp.create_employee(
        company_id, first_name, last_name, email, is_active,
        id, middle_name, url, phone, birthdate)
    id_new_emp = new_emp["id"]
    assert len(new_emp) == 1

    # Проверка, что создан 1 сотрудник
    emp_list_a = emp.get_list_employee(params_to_add={'company': company_id})
    len_after = len(emp_list_a)
    assert len_after - len_before == 1

    # Проверка созданного сотрудника
    new_emp_result = emp.get_employee_by_id(id_new_emp)

    # Проверка полей
    assert new_emp_result["id"] == id_new_emp
    assert new_emp_result["firstName"] == first_name
    assert new_emp_result["lastName"] == last_name
    assert new_emp_result["isActive"] is True

    # assert new_emp_result["email"] == email # - не сохраняется значение
    assert new_emp_result["middleName"] == middle_name
    assert new_emp_result["avatar_url"] == url
    assert new_emp_result["phone"] == str(phone)
    assert new_emp_result["birthdate"] == '2005-04-26'

    emp_list = emp.get_list_employee(params_to_add={'company': company_id})
    emp_list_id = emp_list[-1]['id']
    assert id_new_emp == emp_list_id

    # будет проверка из базы данных

    # Удаление компании через базу данных
    # возможно сначала нужно будет удалить сотрудника


def test_create_employee_without_auth_token():
    new_company = com.create_company('Компания для нового сотрудника 8')
    company_id = new_company["id"]

    # Проверка, что у созданной компании нет сотрудников
    emp_list_f = emp.get_list_employee(params_to_add={'company': company_id})
    len_before = len(emp_list_f)
    assert len(emp_list_f) == 0

    # Создание нового сотрудника без авторизационного токена
    new_emp = emp.create_employee_without_auth_token(
        company_id, first_name, last_name, email, is_active,
        id, middle_name, url, phone, birthdate)

    assert new_emp["statusCode"] == 401
    assert new_emp["message"] == 'Unauthorized'

    # Проверка, что не создан ни один сотрудник
    emp_list_a = emp.get_list_employee(params_to_add={'company': company_id})
    len_after = len(emp_list_a)
    assert len_after - len_before == 0


def test_create_employee_without_body():
    new_company = com.create_company('Компания для нового сотрудника 8')
    company_id = new_company["id"]

    # Проверка, что у созданной компании нет сотрудников
    emp_list_f = emp.get_list_employee(params_to_add={'company': company_id})
    assert len(emp_list_f) == 0

    # Попытка создания сотрудника без тела запроса
    new_emp = emp.create_employee_without_body()
    assert new_emp == 500
    # необходимо прописать более информационный статус код и сообщение.
    # возможно 400 - плохой запрос


def test_get_employee_by_id():
    # Создание новой компании
    new_company = com.create_company('Компания для сотрудника по ID 8')
    company_id = new_company["id"]

    # Создание нового сотрудника
    new_emp = emp.create_employee(
        company_id, first_name, last_name, email, is_active)
    emp_id = new_emp['id']
    # временная проверка вместо проверки схемы
    assert len(new_emp) == 1

    # Получение сотрудника по ID
    get_new_emp = emp.get_employee_by_id(emp_id)
    get_new_emp_id = get_new_emp['id']

    # Проверка значений ключей ответа
    assert get_new_emp["id"] == emp_id
    assert get_new_emp["firstName"] == first_name
    assert get_new_emp["lastName"] == last_name
    # assert get_new_emp["email"] == email
    # ФР: возвращается null
    # ОР: возвращается значение email
    assert get_new_emp["isActive"] == is_active

    assert get_new_emp["middleName"] == ''
    # ФР: ключ avatar_url
    # ОР: ключ url (по сваггеру)
    assert get_new_emp["avatar_url"] == ''
    assert get_new_emp["phone"] == ''
    assert get_new_emp["birthdate"] == '2005-05-03'

    # Проверка, что сотрудник есть в списке сотрудников компании
    list_emps = emp.get_list_employee(params_to_add={'company': company_id})
    emp_list_id = list_emps[-1]['id']
    assert emp_list_id == get_new_emp_id

    # будет проверка из базы данных

    # Удаление компании через базу данных
    # возможно сначала нужно будет удалить сотрудника


def test_get_employee_by_id_without_id():
    # Создание новой компании
    new_company = com.create_company('Компания для сотрудника по ID 8')
    company_id = new_company["id"]

    # Создание нового сотрудника
    new_emp = emp.create_employee(
        company_id, first_name, last_name, email, is_active)
    # временная проверка вместо проверки схемы
    assert len(new_emp) == 1

    # Попытка получения сотрудника без указания ID
    get_new_emp = emp.get_employee_by_id_without_id()
    assert get_new_emp["statusCode"] == 500
    assert get_new_emp["message"] == 'Internal server error'
    # необходимо прописать более информационный статус код и сообщение.
    # возможно 400 - плохой запрос


@pytest.mark.xfail(reason="ФР: тело ответа пустое, ОР: 404 сотрудник не найден")
def test_get_employee_by_wrong_id():
    # Создание новой компании
    new_company = com.create_company('Компания для сотрудника по ID 8')
    company_id = new_company["id"]

    # Создание нового сотрудника
    new_emp = emp.create_employee(
        company_id, first_name, last_name, email, is_active)
    emp_id = new_emp['id']
    # временная проверка вместо проверки схемы
    assert len(new_emp) == 1
    wrong_emp_id = emp_id + 1000

    # Попытка получения сотрудника по неправильному ID
    get_new_emp = emp.get_employee_by_id(wrong_emp_id)
    assert len(get_new_emp) == 1


def test_patch_employee():
    # Создание новой компании для изменения данных сотрудника
    new_company = com.create_company(
        'Компания для изменения данных сотрудника', 'проверка всех ключей и значений')
    new_company_id = new_company['id']

    # Создание нового сотрудника
    new_employee = emp.create_employee(
        new_company_id, first_name, last_name, email, is_active)
    new_employee_id = new_employee['id']

    # Изменение данных сотрудника
    result = emp.change_info_employee(
        new_employee_id, new_last_name, new_email, new_url, new_phone,
        new_is_active)
    # assert len(result) == 7 # временная проверка вместо проверки схемы ответа
    # Проверка ключей ответа
    # ФР: отсутствуют ключи, прописанные в сваггер
    # ОР: все ключи есть в json
    assert result.get('id') == new_employee_id

    # assert result.get('lastName') == new_last_name
    # ФР: ключ-значение не возвращается
    # ОР: ключ - значение (новое)
    assert result.get('isActive') == new_is_active
    assert result.get('email') == new_email
    # assert result.get('phone') == new_phone
    # ФР: ключ-значение не возвращается
    # ОР: ключ - значение (новое)
    assert result.get('url') == new_url

    # assert result.get('firstName') == first_name
    # ФР: ключ-значение не возвращается
    # ОР: ключ - значение
    assert result.get('middleName') == new_employee.get('middleName')
    assert result.get('companyId') == new_employee.get('companyId')
    assert result.get('birthdate') == new_employee.get('birthdate')

    # будет проверка из базы данных

    # Удаление компании через базу данных
    # возможно сначала нужно будет удалить сотрудника


def test_patch_employee_without_auth_token():
    # Создание новой компании для изменения данных сотрудника
    new_company = com.create_company(
        'Компания для изменения данных сотрудника', 'проверка всех ключей и значений')
    new_company_id = new_company['id']

    # Создание нового сотрудника
    new_employee = emp.create_employee(
        new_company_id, first_name, last_name, email, is_active)
    new_employee_id = new_employee['id']

    # Попытка изменения данных сотрудника без авторизационного токена
    result = emp.change_info_employee_without_auth_token(
        new_employee_id, new_last_name, new_email,
        new_url, new_phone, new_is_active)

    # Удалить компанию
    assert result["statusCode"] == 401
    assert result["message"] == 'Unauthorized'


def test_patch_employee_without_id():
    # Создание новой компании для изменения данных сотрудника
    new_company = com.create_company(
        'Компания для изменения данных сотрудника', 'проверка всех ключей и значений')
    new_company_id = new_company['id']

    emp.create_employee(
        new_company_id, first_name, last_name, email, is_active)

    # Попытка изменения данных сотрудника без указания ID
    result = emp.change_info_employee_without_id(
        new_last_name, new_email, new_url, new_phone, new_is_active)

    # Удалить компанию
    assert result["statusCode"] == 404
    assert result["error"] == 'Not Found'


@pytest.mark.xfail(reason="ФР: без тела возвращает информацию по пользователю ОР: статус 400")
def test_patch_employee_without_body():
    # Создание новой компании для изменения данных сотрудника
    new_company = com.create_company(
        'Компания для изменения данных сотрудника', 'проверка всех ключей и значений')
    new_company_id = new_company['id']

    # Создание нового сотрудника
    new_employee = emp.create_employee(
        new_company_id, first_name, last_name, email, is_active)
    new_employee_id = new_employee['id']

    # Попытка изменения данных сотрудника без тела запроса
    result = emp.change_info_employee_without_body(new_employee_id)

    # Удалить компанию
    assert result["statusCode"] == 400
    assert result["error"] == 'Bad Request'


@pytest.mark.xfail(reason="ФР: 500, ОР: 404")
def test_patch_employee_wrong_id():
    # Создание новой компании для изменения данных сотрудника
    new_company = com.create_company(
        'Компания для изменения данных сотрудника', 'проверка всех ключей и значений')
    new_company_id = new_company['id']

    # Создание нового сотрудника
    new_employee = emp.create_employee(
        new_company_id, first_name, last_name, email, is_active)
    new_employee_id = new_employee['id']
    wrong_emp_id = new_employee_id + 1000

    # Попытка изменения данных сотрудника с неправильным ID
    result = emp.change_info_employee(
        wrong_emp_id, new_last_name, new_email, new_url, new_phone,
        new_is_active)

    # Удалить компанию
    assert result["statusCode"] == 404
    assert result["message"] == 'Not Found'
    