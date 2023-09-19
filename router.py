from fastapi import APIRouter,Request, Form
import requests
from app import *
import stripe
router = APIRouter()
templates = Jinja2Templates(directory="templates")


stripe.api_key = "sk_test_51Ns4UrLFjtCoG6X7bMYImKXrpSdxLBWVTzOFEslrFIdmkzOY1up6uAfp0VNsUxebmwzHT9A9VdWbd37tjcbLgqKb008TCS0SLA"
@router.get("/")
async def index(request : Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })
@router.get("/success")
async def index(request : Request):
    return templates.TemplateResponse("success.html", {
        "request": request
    })
@router.get("/cancel")
async def index(request : Request):
    return templates.TemplateResponse("cancel.html", {
        "request": request
    })


@router.post("/create-checkout-session")
async def create_checkout_session(request : Request):
    
    session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'idr',
        'product_data': {
          'name': 'Yureza',
        },
        'unit_amount': 50000000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
    cancel_url='http://127.0.0.1:8000/cancel?session_id={CHECKOUT_SESSION_ID}',
  )
    
    return RedirectResponse(session.url, status_code=303)