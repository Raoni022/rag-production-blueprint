from fastapi import APIRouter, Depends
from src.api.schemas import QueryRequest, QueryResponse
from src.api.deps import get_rag_service
from src.api.services import RAGService

router = APIRouter(tags=["rag"])


@router.post("/query", response_model=QueryResponse)
def query(req: QueryRequest, service: RAGService = Depends(get_rag_service)):
    return service.handle_query(req)
