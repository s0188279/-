import re

class Client:
    def __init__(
        self,
        client_id: int,
        last_name: str,
        first_name: str,
        passport_series: str,
        passport_number: str,
        phone: str,
        patronymic: str | None = None,
        email: str | None = None,
    ):
        self.client_id = client_id
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.passport_series = passport_series
        self.passport_number = passport_number
        self.phone = phone
        self.email = email

    # валидаторы

    @staticmethod
    def validate_id(client_id: int) -> bool:
        if not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("ID клиента должен быть положительным целым числом.")
        return True

    @staticmethod
    def validate_name(name: str, field_name: str = "ФИО") -> bool:
        if not isinstance(name, str):
            raise TypeError(f"Поле '{field_name}' должно быть строкой.")
        if not re.match(r"^[A-Za-zА-Яа-яЁё\-]+$", name):
            raise ValueError(f"Некорректный формат поля '{field_name}': {name}")
        return True

    @staticmethod
    def validate_passport_series(series: str) -> bool:
        if not isinstance(series, str):
            raise TypeError("Серия паспорта должна быть строкой.")
        if not re.match(r"^\d{4}$", series):
            raise ValueError(f"Серия паспорта должна содержать 4 цифры: {series}")
        return True

    @staticmethod
    def validate_passport_number(number: str) -> bool:
        if not isinstance(number, str):
            raise TypeError("Номер паспорта должен быть строкой.")
        if not re.match(r"^\d{6}$", number):
            raise ValueError(f"Номер паспорта должен содержать 6 цифр: {number}")
        return True

    @staticmethod
    def validate_phone(phone: str) -> bool:
        if not isinstance(phone, str):
            raise TypeError("Телефон должен быть строкой.")
        if not re.match(r"^(\+7|8)\d{10}$", phone):
            raise ValueError(f"Некорректный номер телефона: {phone}")
        return True

    @staticmethod
    def validate_email(email: str | None) -> bool:
        if email is None:
            return True
        if not isinstance(email, str):
            raise TypeError("Email должен быть строкой.")
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise ValueError(f"Некорректный email: {email}")
        return True

    # геттеры и сеттеры
    
    # --- client_id ---
    @property
    def client_id(self) -> int:
        return self._client_id

    @client_id.setter
    def client_id(self, value: int):
        Client.validate_id(value)
        self._client_id = value

    # --- last_name ---
    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        Client.validate_name(value, "Фамилия")
        self._last_name = value

    # --- first_name ---
    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        Client.validate_name(value, "Имя")
        self._first_name = value

    # --- patronymic ---
    @property
    def patronymic(self) -> str | None:
        return self._patronymic

    @patronymic.setter
    def patronymic(self, value: str | None):
                if value is not None:
            Client.validate_name(value, "Отчество")
            self._patronymic = value.capitalize()
        else:
            self._patronymic = None

    # --- passport_series ---
    @property
    def passport_series(self) -> str:
        return self._passport_series

    @passport_series.setter
    def passport_series(self, value: str):
        Client.validate_passport_series(value)
        self._passport_series = value

    # --- passport_number ---
    @property
    def passport_number(self) -> str:
        return self._passport_number

    @passport_number.setter
    def passport_number(self, value: str):
        Client.validate_passport_number(value)
        self._passport_number = value

    # --- phone ---
    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str):
        Client.validate_phone(value)
        self._phone = value

    # --- email ---
    @property
    def email(self) -> str | None:
        return self._email

    @email.setter
    def email(self, value: str | None):
        Client.validate_email(value)
        self._email = value
