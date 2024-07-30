from sqlalchemy import create_engine
from sqlalchemy.sql import text
from faker import Faker
import allure


@allure.epic("HW9")
@allure.story("BD.employee")
class EmployeeTable:
    __scripts = {
        "select by id": text("select * from employee where id =:id_to_select"),
        "select list emp by id company": text("select * from employee where company_id =:company_id order by id"),
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "select_by_name": text("select * from company where name = 'Company Empoyees 8'"),
        "get max id": "select MAX(id) from employee",
        "insert new": text(
            "insert into employee( first_name, last_name,company_id, is_active, phone, email, middle_name, birthdate, avatar_url) values (:first_name, :last_name, :company_id, :is_active, :phone, :email, :middle_name, :birthdate, :url)"),
        "update by id": text(
            "update employee set first_name=:first_name, last_name=:last_name, email=:email, middle_name=:middle_name, is_active=:is_active, phone=:phone, birthdate=:birthdate,avatar_url=:url where id=:id_emp")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    @allure.step("db.получить сотрудника по id")
    def get_emp_by_id(self, emp_id: int) -> list:
        """ Метод находит сотрудника по id."""
        query = self.__db.execute(self.__scripts["select by id"],
                                  id_to_select=emp_id)
        allure.attach(str(query.context.cursor.query), 'SQL',
                      allure.attachment_type.TEXT)
        return query.fetchall()

    @allure.step("db.получить список сотрудников по id компании")
    def get_list_emps_by_id_company(self, com_id: int) -> list:
        """
        Метод находит всех сотрудников компании
        и возращает список словарей с информацией по сотрудникам.
        """
        query = self.__db.execute(
            self.__scripts["select list emp by id company"], company_id=com_id)
        allure.attach(str(query.context.cursor.query), 'SQL',
                      allure.attachment_type.TEXT)
        return query.fetchall()

    @allure.step("db.получить список id сотрудников по id компании")
    def get_list_id_emps_by_id_company(self, com_id: int) -> list:
        """
        Метод находит всех сотрудников компании
        и возвращает список id сотрудников
        """
        list_id_emp = []

        id_emp = self.get_list_emps_by_id_company(com_id)
        for i in range(len(id_emp)):
            get_id_emp = id_emp[i][0]
            list_id_emp.append(get_id_emp)

        return list_id_emp

    @allure.step("db.получить max id сотрудника")
    def get_emp_max_id(self) -> int:
        """
        Метод находит наибольшее значение id сотрудника
        и возвращает его.
        """
        query = self.__db.execute(self.__scripts["get max id"])
        allure.attach(str(query.context.cursor.query), 'SQL',
                      allure.attachment_type.TEXT)
        max_id_emp = query.fetchall()[0][0]
        return max_id_emp

    # а что если изменятся названия ключей - как упростить поддержку тестовых данных?
    @allure.step("db.создать нового сотрудника компании")
    def create_employee(self, com_id: int, is_active: bool,
                        dict_creds_emp: dict) -> None:
        """
        Метод создает нового сотрудника компании с генерируемыми
        значениями ключей
        """

        query = self.__db.execute(self.__scripts["insert new"],
                                  company_id=com_id,
                                  first_name=dict_creds_emp["first_name"],
                                  last_name=dict_creds_emp["last_name"],
                                  is_active=is_active,
                                  phone=dict_creds_emp["phone"],
                                  url=dict_creds_emp["url"],
                                  birthdate=dict_creds_emp["birthdate"],
                                  email=dict_creds_emp["email"],
                                  middle_name=dict_creds_emp["middle_name"])
        allure.attach(str(query.context.cursor.query), 'SQL',
                      allure.attachment_type.TEXT)

    # как создать несколько разных сотрудников ???
    # создание тестовых данных в классе бд плохо
    # как сгенерировать несколько сотрудников если передавая один словарь
    # и все сотрудники будут с одинаковыми данными
    @allure.step("db.создать несколько ({num_emp}) новых сотрудников компании")
    def create_employees_mult(self, com_id: int, num_emp: int,
                              is_active: bool) -> None:
        """
        Метод создает заданное количество сотрудников компании,
        используя генерируемые значения ключей
        """
        fake = Faker("ru_RU")
        for i in range(num_emp):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            middle_name = fake.first_name_male()
            phone = fake.random_number(digits=11, fix_len=True)
            birthdate = '2005-04-26'
            url = fake.url()
            max_id_b = self.get_emp_max_id()
            max_id = max_id_b + 1
            self.__db.execute(self.__scripts["insert new"], id=max_id,
                              company_id=com_id, first_name=first_name,
                              last_name=last_name, is_active=is_active,
                              phone=phone, url=url, birthdate=birthdate,
                              email=email, middle_name=middle_name)

    @allure.step("db.удалить сотрудника по id")
    def delete(self, emp_id: int) -> None:
        """
        Метод удаляет сотрудника компании по id сотрудника
        """
        query = self.__db.execute(self.__scripts["delete by id"],
                                  id_to_delete=emp_id)
        allure.attach(str(query.context.cursor.query), 'SQL',
                      allure.attachment_type.TEXT)

    @allure.step("db.удалить список сотрудников по id")
    def delete_list_emps(self, list: list) -> None:
        """
        Метод удаляет сотрудников компании
        по списку id сотрудников.
        """
        for i in range(len(list)):
            query = self.__db.execute(self.__scripts["delete by id"],
                                      id_to_delete=list[i])
            allure.attach(str(query.context.cursor.query), 'SQL',
                          allure.attachment_type.TEXT)

    @allure.step("db.удалить список сотрудников по id компании")
    def delete_list_emps_by_company_id(self, company_id: int) -> None:
        """
        Метод удаляет сотрудников компании
        по id компании. Сначала по id компании получает список id сотрудников.
        Затем удалеяет сотрудников по id из полученного списка.
        """
        list_id_emp = self.get_list_id_emps_by_id_company(company_id)
        for i in range(len(list_id_emp)):
            query = self.__db.execute(self.__scripts["delete by id"],
                                      id_to_delete=list_id_emp[i])
            allure.attach(str(query.context.cursor.query), 'SQL',
                          allure.attachment_type.TEXT)

    def patch_employee(self, id_emp: int, is_active: bool,
                       dict_creds_emp: dict) -> None:
        query = self.__db.execute(self.__scripts["update by id"],
                                  id_emp=id_emp,
                                  first_name=dict_creds_emp["first_name"],
                                  last_name=dict_creds_emp["last_name"],
                                  is_active=is_active,
                                  phone=dict_creds_emp["phone"],
                                  url=dict_creds_emp["url"],
                                  birthdate=dict_creds_emp["birthdate"],
                                  email=dict_creds_emp["email"],
                                  middle_name=dict_creds_emp["middle_name"])
        allure.attach(str(query.context.cursor.query), 'SQL',
                      allure.attachment_type.TEXT)

    # db = create_engine(db_connection_string).connect()
    # sql_statement = text("select * from company where id=:company_id")
    # row = db.evecute(sql_statement, {"company_id": 2338}).fetchall()
    # db.commit()
    #
    def get_companies(self):
        return self.__db.execute(self.__scripts["select_by_name"]).fetchall()