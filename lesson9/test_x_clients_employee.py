import pytest
from faker import Faker
import allure

from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable
from CompanyTable import CompanyTable


base_url = 'https://x-clients-be.onrender.com'
db_url = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'

db_emp = EmployeeTable(db_url)
db_com = CompanyTable(db_url)
emp = EmployeeApi(base_url)
Faker.seed()
fake = Faker("ru_RU")

api_creds_emp = {
    'lastName': fake.last_name(),
    'email': fake.email(),
    'url': fake.url(),
    'phone': fake.random_number(digits=11, fix_len=True),
    'isActive': False
    }

dict_creds_emp = {
    'first_name': fake.first_name(),
    'last_name': fake.last_name(),
    'email': fake.email(),
    'middle_name': fake.first_name_male(),
    'is_active': True,
    'phone': fake.random_number(digits=11, fix_len=True),
    'birthdate': '2005-04-26',
    'url': fake.url()
    }
is_active = True

num_emps = 3  # кол-во сотрудников (пока одинаковых) создаваемых авто


@allure.epic("hw9")
@allure.feature("сотрудник компании")
class TestEmployee:

    # Создаются одинаковые сотрудники
    @allure.story("получить сотрудника/список сотрудников")
    def test_get_list_employees(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # проверить что у компании нет сотрудников бд
        list_emp_db = db_emp.get_list_emps_by_id_company(company_id)
        assert len(list_emp_db) == 0

        # создать нескольких сотрудников
        for i in range(num_emps):
            db_emp.create_employee(company_id, is_active, dict_creds_emp)

        # проверить что создали верное кол-во сотрудников
        assert len(db_emp.get_list_id_emps_by_id_company(company_id)) == num_emps

        result_api = emp.get_list_employee(params={"company": company_id})
        result_db = db_emp.get_list_emps_by_id_company(company_id)
        assert len(result_api) == len(result_db)

        # сравнить значения ключа id сотрудников,
        # полученных по апи и через запрос к бд
        # считаем, что списки отсортированы по
        # возрастанию по id сотрудника
        for i in range(num_emps):
            assert result_api[i]["id"] == result_db[i]["id"]

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("получить сотрудника/список сотрудников")
    def test_get_employee_by_id(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        # получить сотрудника по id
        get_new_emp = emp.get_employee_by_id(id_new_emp)

        # проверка значений ключей ответа
        assert get_new_emp["id"] == id_new_emp
        assert get_new_emp["firstName"] == list_id_new_emp[0][4]
        assert get_new_emp["lastName"] == list_id_new_emp[0][5]
        # assert get_new_emp["email"] == list_id_new_emp[0][8]
        # ФР:возвращается null
        # ОР: возвращается значение email
        assert get_new_emp["isActive"] == list_id_new_emp[0][1]

        assert get_new_emp["middleName"] == list_id_new_emp[0][6]
        # ФР:ключ avatar_url ОР: ключ url (сваггер)
        assert get_new_emp["avatar_url"] == list_id_new_emp[0][10]
        assert get_new_emp["phone"] == list_id_new_emp[0][7]
        assert get_new_emp["birthdate"] == '2003-04-26'

        # проверка что сотрудник есть в списке сотрудников компании
        list_emps = db_emp.get_list_emps_by_id_company(company_id)
        emp_list_id = list_emps[-1][0]
        assert emp_list_id == get_new_emp["id"]

        # удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.получить сотрудника/список сотрудников")
    def test_get_employee_by_id_without_id(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        db_emp.create_employee(
            company_id, is_active, dict_creds_emp)

        # получить сотрудника по id
        get_new_emp = emp.get_employee_by_id_without_id()
        assert get_new_emp["statusCode"] == 500
        assert get_new_emp["message"] == 'Internal server error'
        # необходимо прописать более информационный статус код и сообщение.
        # возможно 400 - плохой запрос

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.получить сотрудника/список сотрудников")
    @pytest.mark.xfail(reason="company_id is required")
    def test_get_list_employee_without_company_id(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        result = db_emp.get_list_emps_by_id_company(company_id)
        assert len(result) == 1

        # удалить компанию
        db_com.delete_company(company_id)

    @allure.story("создание сотрудника/сотрудников")
    def test_create_employee(self):
        # создать новую компанию
        db_com.create_company('Company Empoyees 8')
        company_id = db_com.get_max_id()

        # проверить, что у созданной компании нет работников
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        len_before = len(emp_list_f)
        assert len_before == 0

        # создать нового работника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        # проверка, что создан 1 работник
        emp_list = db_emp.get_list_emps_by_id_company(company_id)
        id_emp_create = emp_list[-1]['id']
        len_after = len(emp_list)
        assert len_after - len_before == 1

        # проверка созданного работника
        result_api = emp.get_employee_by_id(id_new_emp)

        # проверка заполненных
        assert result_api["id"] == id_new_emp
        assert result_api["firstName"] == dict_creds_emp["first_name"]
        assert result_api["lastName"] == dict_creds_emp["last_name"]
        assert result_api["isActive"] is True

        # - не сохраняется значение
        # assert result_api ["email"] == dict_creds_emp["email"]
        assert result_api["middleName"] == dict_creds_emp["middle_name"]
        assert result_api["avatar_url"] == dict_creds_emp["url"]
        assert result_api["phone"] == str(dict_creds_emp["phone"])
        assert result_api["birthdate"] == dict_creds_emp["birthdate"]

        # проверить, что последний id сотрудника равен созданному сотруднику
        assert id_new_emp == id_emp_create

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.создание сотрудника/сотрудников")
    def test_create_employee_without_auth_token(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # проверить что у созданной компании нет сотрудника
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        len_before = len(emp_list_f)
        assert len(emp_list_f) == 0

        # создать нового сотрудника
        new_emp = emp.create_employee_without_auth_token(
            company_id, dict_creds_emp)

        assert new_emp["statusCode"] == 401
        assert new_emp["message"] == 'Unauthorized'

        # проверка, что не создан сотрудник
        emp_list_a = db_emp.get_list_emps_by_id_company(company_id)
        len_after = len(emp_list_a)
        assert len_after - len_before == 0

        # удаление компании
        db_com.delete_company(company_id)

    @allure.story("negative.создание сотрудника/сотрудников")
    def test_create_employee_without_body(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # проверка что у созданной компании нет сотрудников
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        assert len(emp_list_f) == 0

        # создать нового сотрудника
        new_emp = emp.create_employee_without_body()
        assert new_emp["statusCode"] == 500
        assert new_emp["message"] == 'Internal server error'
        # необходимо прописать более информационный статус код и сообщение.
        # возможно 400 - плохой запрос

        # удаление компании
        db_com.delete_company(company_id)

    # есть вопросы
    @allure.story("редактировать сотрудника/сотрудников")
    def test_patch_employee(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        db_emp.patch_employee(id_new_emp, is_active, dict_creds_emp)
        result_db = db_emp.get_emp_by_id(id_new_emp)

        # проверить ключи ответа - ФР: нет ключей прописанных в свагере
        # ОР: все ключи есть в json
        assert result_db[0][0] == id_new_emp
        result_api = emp.get_employee_by_id(id_new_emp)

        # assert result_db[0][5] == result_api['lastName']
        # ФР: ключ-значение не возвращается
        # ОР: ключ - значение (новое)
        assert result_db[0][1] == result_api.get('isActive')
        assert result_db[0][8] == result_api.get('email')
        # assert result_db[0][7] == result_api['phone']
        # ФР: ключ-значение не возвращается
        # ОР: ключ - значение (новое)
        assert result_db[0][10] == result_api.get('avatar_url')

        # assert result_db[0][4] == result_api['firstName']
        # ФР: ключ-значение не возвращается
        # ОР: ключ - значение
        assert result_db[0][6] == result_api.get('middleName')
        assert result_db[0][11] == result_api.get('companyId')
        # assert result_db[0][9] == result_api.get('birthdate') # дата через запятую как исправить?

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.редактировать сотрудника/сотрудников")
    def test_patch_employee_without_auth_token(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        result = emp.change_info_employee_without_auth_token(
            id_new_emp, api_creds_emp)

        assert result["statusCode"] == 401
        assert result["message"] == 'Unauthorized'

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.редактировать сотрудника/сотрудников")
    def test_patch_employee_without_id(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)

        result = emp.change_info_employee_without_id(api_creds_emp)

        assert result["statusCode"] == 404
        assert result["error"] == 'Not Found'

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @pytest.mark.xfail(reason="без тела запроса возвращается информация по пользователю")
    @allure.story("negative.редактировать сотрудника/сотрудников")
    def test_patch_employee_without_body(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        result = emp.change_info_employee_without_body(
            id_new_emp)

        assert result["statusCode"] == 404
        assert result["error"] == 'Not Found'

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @pytest.mark.xfail(reason="ФР: 500, ОР: 404")
    @allure.story("negative.редактировать сотрудника/сотрудников")
    def test_patch_employee_wrong_id(self):
        # создать новую компанию
        db_com.create_company("Company Empoyees 8")
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        db_emp.create_employee(company_id, is_active, dict_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        wrong_emp_id = id_new_emp + 1000

        result = emp.change_info_employee_wrong_id(wrong_emp_id)

        assert result["statusCode"] == 404
        assert result["message"] == 'Not Found'

        # удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_soft(company_id)
