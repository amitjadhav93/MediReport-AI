from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User
from app.schemas.user import UserCreate, TokenResponse

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=TokenResponse)
def register(payload: UserCreate, db: Session= Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(400,"Email already exist")
    user = User(email=payload.email, hashed_password=hash_password(payload.password))
    db.add(user); db.commit(); db.refresh(user)
    token = create_access_token({"sub":str(user.id)})
    return {"access_token":token}

router.post("/login", response_model=TokenResponse)
def login(payload: UserCreate, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(401, "Invalid credentials")
    token = create_access_token({"sub":str(user.id)})
    return {"access_token":token}

