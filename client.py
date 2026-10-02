import json
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

    # альтернативные конструкторы    
    @classmethod
    def from_dict(cls, data: dict) -> "Client":
        # cоздание объекта из словаря Python
        return cls(
            client_id=int(data["client_id"]),
            last_name=data["last_name"],
            first_name=data["first_name"],
            passport_series=str(data["passport_series"]),
            passport_number=str(data["passport_number"]),
            phone=str(data["phone"]),
            patronymic=data.get("patronymic"),
            email=data.get("email"),
        )

    @classmethod
    def from_json(cls, json_str: str) -> "Client":
        # cоздание объекта из JSON-строки
        data = json.loads(json_str)
        return cls.from_dict(data)

    @classmethod
    def from_string(cls, str_data: str, sep: str = ";") -> "Client":
        """
        cоздание объекта из строки с разделителем
        формат: id;last_name;first_name;patronymic;passport_series;passport_number;phone;email
        """
        parts = [p.strip() for p in str_data.split(sep)]
        if len(parts) < 7:
            raise ValueError("Недостаточно данных в строке для создания Client.")

        client_id = int(parts[0])
        last_name = parts[1]
        first_name = parts[2]
        patronymic = parts[3] if parts[3] and parts[3] != "None" else None
        passport_series = parts[4]
        passport_number = parts[5]
        phone = parts[6]
        email = (
            parts[7]
            if len(parts) > 7 and parts[7] and parts[7] != "None"
            else None
        )

        return cls(
            client_id=client_id,
            last_name=last_name,
            first_name=first_name,
            patronymic=patronymic,
            passport_series=passport_series,
            passport_number=passport_number,
            phone=phone,
            email=email,
        )
        
    # валидаторы

    @staticmethod
    def _validate_by_regex(
        value: str | None,
        pattern: str,
        field_name: str,
        allow_none: bool = False,
    ) -> bool:
        # вспомогательный метод для устранения дублирования проверок по регулярным выражениям
        if allow_none and value is None:
            return True
        if not isinstance(value, str):
            raise TypeError(f"Поле '{field_name}' должно быть строкой.")
        if not re.match(pattern, value):
            raise ValueError(f"Некорректный формат поля '{field_name}': {value}")
        return True

    @staticmethod
    def validate_id(client_id: int) -> bool:
        if not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("ID клиента должен быть положительным целым числом.")
        return True

    @staticmethod
    def validate_name(name: str, field_name: str = "ФИО") -> bool:
        pattern = r"^[A-Za-zА-Яа-яЁё\-]+$"
        return Client._validate_by_regex(name, pattern, field_name)

    @staticmethod
    def validate_passport_series(series: str) -> bool:
        return Client._validate_by_regex(series, r"^\d{4}$", "Серия паспорта")

    @staticmethod
    def validate_passport_number(number: str) -> bool:
        return Client._validate_by_regex(number, r"^\d{6}$", "Номер паспорта")

    @staticmethod
    def validate_phone(phone: str) -> bool:
        pattern = r"^(\+7|8)\d{10}$"
        return Client._validate_by_regex(phone, pattern, "Номер телефона")

    @staticmethod
    def validate_email(email: str | None) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return Client._validate_by_regex(
            email, pattern, "Email", allow_none=True
        )
    
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

    
    def get_initials(self) -> str:
        # вспомогательный метод: формирование ФИО с инициалами
        patronymic_initial = f" {self.patronymic[0]}." if self.patronymic else ""
        return f"{self.last_name} {self.first_name[0]}.{patronymic_initial}"

    def __str__(self) -> str:
        # краткая версия объекта для пользователей
        return f"{self.get_initials()} | Тел: {self.phone}"

    def __repr__(self) -> str:
        # полная версия объекта для разработчиков / отладки
        return (
            f"Client(id={self.client_id}, "
            f"name='{self.last_name} {self.first_name} {self.patronymic or ''}'.strip(), "
            f"passport='{self.passport_series} {self.passport_number}', "
            f"phone='{self.phone}', email='{self.email}')"
        )

    def __eq__(self, other: object) -> bool:
        # сравнение объектов на равенство по паспортным данным или ID
        if not isinstance(other, Client):
            return False
        return (
            self.client_id == other.client_id
            or (
                self.passport_series == other.passport_series
                and self.passport_number == other.passport_number
            )
        )

class ClientShort:
    # класс, содержащий краткую версию данных клиента 

    def __init__(
        self,
        client_id: int,
        last_name: str,
        first_name: str,
        phone: str,
    ):
        self.client_id = client_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone = phone

    # валидаторы

    @staticmethod
    def validate_id(client_id: int) -> bool:
        if not isinstance(client_id, int) or client_id <= 0:
            raise ValueError("ID клиента должен быть положительным целым числом.")
        return True

    @staticmethod
    def validate_name(name: str, field_name: str = "ФИО") -> bool:
        pattern = r"^[A-Za-zА-Яа-яЁё\-]+$"
        return Client._validate_by_regex(name, pattern, field_name)

    @staticmethod
    def validate_phone(phone: str) -> bool:
        pattern = r"^(\+7|8)\d{10}$"
        return Client._validate_by_regex(phone, pattern, "Номер телефона")

    # геттеры и сеттеры

    @property
    def client_id(self) -> int:
        return self._client_id

    @client_id.setter
    def client_id(self, value: int):
        ClientShort.validate_id(value)
        self._client_id = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        ClientShort.validate_name(value, "Фамилия")
        self._last_name = value.capitalize()

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        ClientShort.validate_name(value, "Имя")
        self._first_name = value.capitalize()

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str):
        ClientShort.validate_phone(value)
        self._phone = value

    # вывод и сравнение

    def get_initials(self) -> str:
        return f"{self.last_name} {self.first_name[0]}."

    def __str__(self) -> str:
        return f"{self.get_initials()} | Тел: {self.phone}"

    def __repr__(self) -> str:
        return (
            f"ClientShort(id={self.client_id}, name='{self.get_initials()}', "
            f"phone='{self.phone}')"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ClientShort):
            return False
        return self.client_id == other.client_id
