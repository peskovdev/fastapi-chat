from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models import BaseTable
from app.db.models.message import Message


class Chat(BaseTable):
    __tablename__ = "chats"

    title: Mapped[str] = mapped_column(nullable=False)

    messages: Mapped[list[Message]] = relationship("Message", back_populates="chat")
