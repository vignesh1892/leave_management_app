from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import logger
import db

app = FastAPI()

# Allow frontend (HTML/JS) to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Pydantic Models
# ==========================
class Leave(BaseModel):
    description: str
    empname: str
    date: str
    leave_id: int | None = None 


#read leave
@app.get("/get_leaves")
def get_leaves():
    try:
        logger.info("Fetching all leaves")
        return db.get_leave_types()
    except Exception as e:
        logger.error(f"Error in get_leave_types: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch leaves")


# CREATE leave
@app.post("/add_leave")
def add_leave(leave: Leave):
    try:
        logger.info("Inserting leaves")
        return db.insert_leave(leave.description,leave.empname,leave.date,leave.leave_id)
    except Exception as e:
        logger.error(f"Error in insert_leave: {e}")
        raise HTTPException(status_code=500, detail="Failed to insert_leave")