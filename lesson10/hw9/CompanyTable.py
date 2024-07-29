import allure
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.engine.base import Engine


class CompanyTable:
    __scripts = {
        "select": "select * from company where deleted_at is Null",
        "select only active": "select * from company where is_active = true and deleted_at is Null",
        "delete by id": text("delete from company where id =:id_to_delete"),
        "insert new": text("insert into company(\"name\") values (:new_name)"),
        "get max id": "select MAX(\"id\") from company",
        "select by id": text("select * from company where id =:select_id")
    }

    def __init__(self, connection_string: str):
        """
        Инициализирует таблицу компаний.

        :param connection_string: Строка подключения к базе данных.
        """
        self.__db: Engine = create_engine(connection_string)

    @allure.step("Получение всех компаний")
    def get_companies(self) -> list:
        """
        Получает все компании из базы данных.

        :return: Список всех компаний.
        :rtype: list
        """
        return self.__db.execute(self.__scripts["select"]).fetchall()

    @allure.step("Получение всех активных компаний")
    def get_active_companies(self) -> list:
        """
        Получает все активные компании из базы данных.

        :return: Список всех активных компаний.
        :rtype: list
        """
        return self.__db.execute(self.__scripts["select only active"]).fetchall()

    @allure.step("Удаление компании по ID: {com_id}")
    def delete_company(self, com_id: int) -> None:
        """
        Удаляет компанию из базы данных по указанному ID.

        :param com_id: ID компании для удаления.
        :return: None
        """
        self.__db.execute(self.__scripts["delete by id"], id_to_delete=com_id)

    @allure.step("Создание новой компании с именем: {name}")
    def create_company(self, name: str) -> None:
        """
        Создает новую компанию в базе данных.

        :param name: Имя новой компании.
        :return: None
        """
        self.__db.execute(self.__scripts["insert new"], new_name=name)

    @allure.step("Получение максимального ID компании")
    def get_max_id(self) -> int:
        """
        Получает максимальный ID компании из базы данных.

        :return: Максимальный ID компании.
        :rtype: int
        """
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]

    @allure.step("Получение компании по ID: {com_id}")
    def get_company_by_id(self, com_id: int) -> list:
        """
        Получает компанию из базы данных по указанному ID.

        :param com_id: ID компании для получения.
        :return: Список компаний с указанным ID.
        :rtype: list
        """
        return self.__db.execute(self.__scripts["select by id"], select_id=com_id).fetchall()