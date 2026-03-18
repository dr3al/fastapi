from typing import Annotated, Any
from fastapi import Depends, Header, HTTPException

from schemas.dependency import PaginationParams, FilterParams

PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]
FilterParamsDep = Annotated[FilterParams, Depends(FilterParams)]

