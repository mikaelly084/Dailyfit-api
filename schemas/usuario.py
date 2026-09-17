from pydantic import BaseModel, ConfigDict


class UsuarioCreate(BaseModel):
    nome: str
    email: str


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str

    model_config = ConfigDict(from_attributes=True)

    