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

    # --- client_id ---
    @property
    def client_id(self) -> int:
        return self._client_id

    @client_id.setter
    def client_id(self, value: int):
        self._client_id = value

    # --- last_name ---
    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

    # --- first_name ---
    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    # --- patronymic ---
    @property
    def patronymic(self) -> str | None:
        return self._patronymic

    @patronymic.setter
    def patronymic(self, value: str | None):
        self._patronymic = value

    # --- passport_series ---
    @property
    def passport_series(self) -> str:
        return self._passport_series

    @passport_series.setter
    def passport_series(self, value: str):
        self._passport_series = value

    # --- passport_number ---
    @property
    def passport_number(self) -> str:
        return self._passport_number

    @passport_number.setter
    def passport_number(self, value: str):
        self._passport_number = value

    # --- phone ---
    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str):
        self._phone = value

    # --- email ---
    @property
    def email(self) -> str | None:
        return self._email

    @email.setter
    def email(self, value: str | None):
        self._email = value