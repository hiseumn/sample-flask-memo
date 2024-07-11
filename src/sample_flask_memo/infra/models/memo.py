from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from uuid6 import uuid7
from sqlalchemy_utils import UUIDType
from sqlalchemy.types import Text

Base = declarative_base()
class Memo(Base):
    __tablename__ = "memo"  # テーブル名を指定
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid7)
    memo = Column(Text)

    def memo_result(self):  # メモの内容を返す
        return "{self.id} {self.memo}"
    