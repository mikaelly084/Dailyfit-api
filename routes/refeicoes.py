from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.refeicao import RefeicaoModel
from models.usuario import UsuarioModel
from schemas.refeicao import RefeicaoCreate, RefeicaoResponse


router = APIRouter(
    prefix="/usuarios/{usuario_id}/refeicoes",
    tags=["Refeições"]
)


def verificar_usuario(usuario_id: int, db: Session):
    usuario = (
        db.query(UsuarioModel)
        .filter(UsuarioModel.id == usuario_id)
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    return usuario


# CRIAR REFEIÇÃO
@router.post(
    "",
    response_model=RefeicaoResponse,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_refeicao(
    usuario_id: int,
    refeicao: RefeicaoCreate,
    db: Session = Depends(get_db)
):
    verificar_usuario(usuario_id, db)

    nova_refeicao = RefeicaoModel(
        usuario_id=usuario_id,
        nome=refeicao.nome,
        descricao=refeicao.descricao,
        nao_dieta=refeicao.nao_dieta
    )

    db.add(nova_refeicao)
    db.commit()
    db.refresh(nova_refeicao)

    return nova_refeicao


# LISTAR REFEIÇÕES
@router.get(
    "",
    response_model=List[RefeicaoResponse]
)
def listar_refeicoes(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    verificar_usuario(usuario_id, db)

    return (
        db.query(RefeicaoModel)
        .filter(RefeicaoModel.usuario_id == usuario_id)
        .order_by(RefeicaoModel.data_hora.desc())
        .all()
    )


# OBTER UMA REFEIÇÃO
@router.get(
    "/{refeicao_id}",
    response_model=RefeicaoResponse
)
def obter_refeicao(
    usuario_id: int,
    refeicao_id: int,
    db: Session = Depends(get_db)
):
    refeicao = (
        db.query(RefeicaoModel)
        .filter(
            RefeicaoModel.id == refeicao_id,
            RefeicaoModel.usuario_id == usuario_id
        )
        .first()
    )

    if not refeicao:
        raise HTTPException(
            status_code=404,
            detail="Refeição não encontrada"
        )

    return refeicao


# EDITAR REFEIÇÃO
@router.put(
    "/{refeicao_id}",
    response_model=RefeicaoResponse
)
def editar_refeicao(
    usuario_id: int,
    refeicao_id: int,
    dados: RefeicaoCreate,
    db: Session = Depends(get_db)
):
    refeicao = (
        db.query(RefeicaoModel)
        .filter(
            RefeicaoModel.id == refeicao_id,
            RefeicaoModel.usuario_id == usuario_id
        )
        .first()
    )

    if not refeicao:
        raise HTTPException(
            status_code=404,
            detail="Refeição não encontrada"
        )

    refeicao.nome = dados.nome
    refeicao.descricao = dados.descricao
    refeicao.nao_dieta = dados.nao_dieta

    db.commit()
    db.refresh(refeicao)

    return refeicao


# DELETAR REFEIÇÃO
@router.delete(
    "/{refeicao_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar_refeicao(
    usuario_id: int,
    refeicao_id: int,
    db: Session = Depends(get_db)
):
    refeicao = (
        db.query(RefeicaoModel)
        .filter(
            RefeicaoModel.id == refeicao_id,
            RefeicaoModel.usuario_id == usuario_id
        )
        .first()
    )

    if not refeicao:
        raise HTTPException(
            status_code=404,
            detail="Refeição não encontrada"
        )

    db.delete(refeicao)
    db.commit()

    return None