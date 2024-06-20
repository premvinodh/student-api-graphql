import uvicorn
from fastapi import FastAPI
# from graphene import ObjectType, Schema, String, Int, List
# from pydantic import BaseModel
from starlette_graphene3 import GraphQLApp, make_graphiql_handler, make_playground_handler

from schema import schema

app = FastAPI()
app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))
app.mount("/graphql-p", GraphQLApp(schema=schema, on_get=make_playground_handler()))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
