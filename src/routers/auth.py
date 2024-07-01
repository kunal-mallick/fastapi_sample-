from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.models.model import model

router = APIRouter()

router.mount("/static", StaticFiles(directory="src/static"), name="static")

templates = Jinja2Templates(directory="templates")
@router.get("/",response_class= HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="item.html")