from src.model.configs.connection import DBconnectiosHandler
from src.model.entities.inscritos import Inscritos

class SubscribersRepository:
    def insert(self, subscriber_infos: dict) -> None:
        with DBconnectiosHandler() as db:
            try:
                new_subscriber = Inscritos(
                    nome = subscriber_infos.get("name"),
                    email = subscriber_infos.get("email"),
                    link = subscriber_infos.get("link"),
                    evento_id = subscriber_infos.get("evento_id")
                    # importar entidades em init.py (foreignkey)
                    )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            

# retornar um elemento de inscritos -> Inscritos
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
        with DBconnectiosHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(Inscritos.email == email,
                        evento_id == evento_id)
                .one_or_none()
            )
            return data
    