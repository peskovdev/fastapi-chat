from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.chat import Chat
from app.db.models import BaseTable


class Message(BaseTable):
    __tablename__ = "messages"

    content: Mapped[str] = mapped_column(nullable=False)

    chat: Mapped[Chat] = relationship("Chat", back_populates="messages")
    chat_id: Mapped[str] = mapped_column(ForeignKey("chats.id", ondelete="CASCADE"))
