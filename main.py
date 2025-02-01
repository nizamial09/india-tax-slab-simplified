from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


arr = [0, 5, 10, 15, 20, 25, 30]

def _percentage_of_current_slab(slab, amount=400000):
    return amount * (arr[slab] / 100)

def _slab_at_each_level(count, reminder):
    taxes = []
    if count > 5:
        count = 6

    for i in range(count):
        taxes.append(_percentage_of_current_slab(i))
    
    taxes.append(_percentage_of_current_slab(slab=count, amount=reminder))
    return { 'slabs' : taxes }

def _calculate_tax(income):
    if income <= 1200000:
        return { 'total_tax_per_year': 0, 'total_tax_per_month': 0 }
    count = income // 400000
    sum = 0
    reminder = income % 400000

    if count > 5:
        count = 6
        reminder = income - 2400000

    for i in range(count):
        sum = sum + _percentage_of_current_slab(i)

    sum += _percentage_of_current_slab(slab=count, amount=reminder)

    return { 'total_tax_per_year': sum, 'total_tax_per_month': sum / 12 }


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/tax_slab/")
async def calculate_tax(request: Request, income: int = Form(...)):
    tax_details = _calculate_tax(income)
    return JSONResponse(content=tax_details)

@app.get("/tax_slab/")
async def slab_at_each_level(request: Request, income: int):
    if income <= 1200000:
        return JSONResponse(content={ 'slabs': [] })
    taxes = _slab_at_each_level(income // 400000, income % 400000)
    return JSONResponse(content=taxes)