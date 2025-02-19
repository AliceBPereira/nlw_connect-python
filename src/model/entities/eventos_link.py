from src.model.configs.base import Base
from sqlalchemy import Integer, String, Column, ForeignKey

class Eventos_link(Base):
    __tablename__ = "eventos_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_if = Column(Integer, ForeignKey("Eventos.id"), nullable=False)
    inscrito_id = Column(Integer, ForeignKey("Inscritos.id"), nullable=False)
    link = Column(String)
    