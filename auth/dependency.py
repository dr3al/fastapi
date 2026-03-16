from typing import Annotated, Any

from fastapi import Depends, Header, HTTPException

from schemas.dependency import PaginationParams, FilterParams

PaginationDep = Annotated[PaginationParams, Depends(PaginationParams)]
FilterParamsDep = Annotated[FilterParams, Depends(FilterParams)]


def check_headers(
    auth_token: str = Header()
):
    if auth_token == "123":
        return True
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
