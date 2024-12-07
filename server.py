# it uses FastAPI behind the scenes
from codeBase import chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="My translator app using AI", description="Translater texts to any idioms")

# the chain value contains the runable functions. All functions which have the INVOKE method, are considered runable
add_routes(app, chain, path="/translate")

if __name__ == "__main__":
    #uvicorn turns on the server - this has been installed with the langserve
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

# to run this server, we just need to run the corresponding file and after go to the link: http://localhost:8000/translate/playground/
# this one will have an interface, where we'll be able to iterate through, and test the code developed 