from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.refeicao import RefeicaoModel
from models.usuario import UsuarioModel


router = APIRouter(
    prefix="/usuarios/{usuario_id}",
    tags=["Resumo"]
)


@router.get("/resumo")
def obter_resumo(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    # Verifica se o usuário existe
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

    # Busca as refeições em ordem cronológica
    refeicoes = (
        db.query(RefeicaoModel)
        .filter(RefeicaoModel.usuario_id == usuario_id)
        .order_by(RefeicaoModel.data_hora.asc())
        .all()
    )

    total_refeicoes = len(refeicoes)

    dentro_dieta = sum(
        1 for refeicao in refeicoes
        if not refeicao.nao_dieta
    )

    fora_dieta = total_refeicoes - dentro_dieta

    # Calcula a maior sequência dentro da dieta
    melhor_sequencia = 0
    sequencia_atual = 0

    for refeicao in refeicoes:
        if not refeicao.nao_dieta:
            sequencia_atual += 1

            if sequencia_atual > melhor_sequencia:
                melhor_sequencia = sequencia_atual
        else:
            sequencia_atual = 0

    return {
        "total_refeicoes_cadastradas": total_refeicoes,
        "total_refeicoes_dentro_da_dieta": dentro_dieta,
        "total_refeicoes_fora_da_dieta": fora_dieta,
        "melhor_sequencia_de_refeicoes_dentro_da_dieta": melhor_sequencia
    }