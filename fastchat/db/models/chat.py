from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastchat.db.models.base import BaseTable
# from fastchat.db.models.message import Message


class Chat(BaseTable):
    __tablename__ = "chats"

    title: Mapped[str] = mapped_column(nullable=False)

    messages = relationship("Message", back_populates="chat")
    # messages: Mapped[list[Message]] = relationship("Message", back_populates="chat")
