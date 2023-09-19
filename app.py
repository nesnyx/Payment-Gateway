from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from router import router
app = FastAPI()




app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")