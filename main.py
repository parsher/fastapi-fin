from fastapi import FastAPI
from routers import User, Diary
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost",
]

app.include_router(User.router)
app.include_router(Diary.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://lucky516.tistory.com/92 #FAST API

# https://github.com/mongodb/motor/blob/master/doc/tutorial-asyncio.rst
# https://www.mongodb.com/developer/quickstart/python-quickstart-fastapi/

# https://github.com/mongodb-developer/mongodb-with-fastapi
# https://pypi.org/project/motor/ > mongodb driver

# https://ggn0.tistory.com/114  > bson

# https://wikidocs.net/21054 > @classmethod > 정적 메서드

# https://pydantic-docs.helpmanual.io/usage/types/#arbitrary-types-allowed
# https://pydantic-docs.helpmanual.io/usage/types/#classes-with-__get_validators__ > validator 설정
# https://pydantic-docs.helpmanual.io/usage/models/#field-with-dynamic-default-value > Field > default_factory
# https://pydantic-docs.helpmanual.io/usage/schema/#field-customisation > Field > default:
# https://pydantic-docs.helpmanual.io/usage/models/#required-fields >  (a positional argument) the default value of the field. Since the Field replaces the field's default, this first argument can be used to set the default. Use ellipsis (...) to indicate the field is required.


