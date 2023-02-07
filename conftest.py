import pytest
from modules.api.clients.github import Github
from modules.common.database import Database


class User:

    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Vitalii'
        self.second_name = 'Kots'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

@pytest.fixture
def github_api():
    api = Github()
    yield api

@pytest.fixture
def database_fixt():
    db = Database()
    yield db