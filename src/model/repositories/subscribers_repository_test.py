import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("insert in db")
def test_insert():
    subscriber_info = {
        "name": "Meu nome2",
        "email": "meu_email2@email.com",
        "evento_id": 2
    }
    subscriber_repo = SubscribersRepository()
    subscriber_repo.insert(subscriber_info)

@pytest.mark.skip("select in db")

def test_select_subscriber():
    email = "meu_email2@email.com"
    evento_id = 2

    subscriber_repo = SubscribersRepository()
    resp = subscriber_repo.select_subscriber(email, evento_id)
    print(resp.nome)