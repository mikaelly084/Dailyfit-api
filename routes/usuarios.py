from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.usuario import UsuarioModel
from schemas.usuario import UsuarioCreate, UsuarioResponse


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


# CRIAR USUÁRIO
@router.post(
    "",
    response_model=UsuarioResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    usuario_existente = (
        db.query(UsuarioModel)
        .filter(UsuarioModel.email == usuario.email)
        .first()
    )

    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado"
        )

    novo_usuario = UsuarioModel(
        nome=usuario.nome,
        email=usuario.email
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


# LISTAR USUÁRIOS
@router.get(
    "",
    response_model=list[UsuarioResponse]
)
def listar_usuarios(
    db: Session = Depends(get_db)
):
    return db.query(UsuarioModel).all()