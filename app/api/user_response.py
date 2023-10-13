
from fastapi import APIRouter

from app.repository import UserDBOperations
from app.service import UserResponseService
from app.schema import UserRequestModel, UserCreateRequest
from fastapi.logger import logger
from app.lib.exception_handler import error_handler

user_response_router = APIRouter()


@user_response_router.post("/create_user")
@error_handler
async def create_user(request: UserCreateRequest):
    user = UserDBOperations().create(
        register_dict=request, commit=False
        )
    return user


@user_response_router.post("/create")
@error_handler
async def create_question(request: UserRequestModel):
    logger.info("Calling the post user response API.")
    parsed_data = request.request_list
    user_response = UserResponseService().create(parsed_data)
    return user_response

