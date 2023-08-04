from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastchat.db.models.base import BaseTable
# from app.db.models.chat import Chat


class Message(BaseTable):
    __tablename__ = "messages"

    content: Mapped[str] = mapped_column(nullable=False)

    # chat: Mapped[Chat] = relationship("Chat", back_populates="messages")
    chat = relationship("Chat", back_populates="messages")
    chat_id: Mapped[str] = mapped_column(ForeignKey("chats.id", ondelete="CASCADE"))
