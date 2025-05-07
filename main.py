from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from data import produto_repo
from data import cliente_repo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
produto_repo.criar_tabela()
cliente_repo.criar_tabela_cliente()

@app.get("/")
async def home(request: Request):
    produtos = produto_repo.obter_todos()
    response = templates.TemplateResponse("index.html", {"request": request, "produtos": produtos})
    return response

@app.get("/cliente")
async def cliente(request: Request):
    clientes = cliente_repo.obter_todos()
    response = templates.TemplateResponse("clientes.html", {"request": request, "clientes": clientes})
    return response

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
