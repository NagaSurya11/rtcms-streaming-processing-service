from fastapi import APIRouter
from fastapi import Response, status, HTTPException


router = APIRouter()
@router.get('/health')
def health_check():
    return Response(content='Healthy',status_code=status.HTTP_200_OK)