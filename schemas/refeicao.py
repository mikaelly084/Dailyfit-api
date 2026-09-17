from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RefeicaoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    nao_dieta: bool


class RefeicaoResponse(BaseModel):
    id: int
    usuario_id: int
    nome: str
    descricao: Optional[str]
    data_hora: datetime
    nao_dieta: bool

    model_config = ConfigDict(from_attributes=True)