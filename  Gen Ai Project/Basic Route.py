from fastapi import APIRouter

router = APIRouter()

@router.post("/guess")
async def guess_word(seed: str, guess: str):
    return {"message": f"Received your guess '{guess}' for '{seed}'."}
