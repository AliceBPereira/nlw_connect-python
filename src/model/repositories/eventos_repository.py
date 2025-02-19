from src.model.configs.connection import DBconnectiosHandler
from src.model.entities.eventos import Eventos

class EventosRepository:
    def insert(self, event_name: str) -> None:
        with DBconnectiosHandler() as db:
            try:
                new_event = Eventos(nome = event_name)
                db.session.add(new_event)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_event(self, event_name: str) -> Eventos:
        with DBconnectiosHandler() as db:
            data= (
                db.session
                   .query(Eventos)
                   .filter(Eventos.nome == event_name)
                   .one_or_none()
                   )
            
            return data
            
