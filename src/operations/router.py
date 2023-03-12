from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()


# @router.get("/")
# async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
#     try:
#         query = select(operation).where(operation.c.type == operation_type)
#         result = await session.execute(query)
#         # if the request done, getting the successful response
#         return {
#             'status': 'success',
#             'data': result.all(),
#             'details': 'None'
#         }
#     except Exception:
#         # if the request fail, getting the  exception response
#         raise HTTPException(status_code=500, detail={
#             'status': 'error',
#             'data': None,
#             'details': None
#         })


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

