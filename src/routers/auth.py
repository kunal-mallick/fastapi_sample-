from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.models.model import model

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")
@router.get("/",response_class= HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")