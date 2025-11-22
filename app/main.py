# main.py
import sys
from pathlib import Path
import uvicorn
from fastapi import FastAPI
from app.routes import basic_info_routes, contract_info_routes, accounts_routes, roles_routes, leave_absence_routes
from app.database import engine, Base

root = Path(__file__).resolve().parent.parent
sys.path.append(str(root))

# Create tables if they don't exist. This will create metadata for models into the DB.
# NOTE: If your DB already has tables (you created via SQL script), this is harmless.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="GSA HR - Employee Management API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the GSA HR - Employee Management API"}
# include routers
app.include_router(basic_info_routes.router, prefix="/basic-info")
app.include_router(contract_info_routes.router)
app.include_router(accounts_routes.router)
app.include_router(roles_routes.router)
app.include_router(leave_absence_routes.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
