import pytest
from httpx import AsyncClient
from backend.main import app

@pytest.mark.asyncio
async def test_duplicate_guess_flow():
    seed = "Rock"
    guess = "Paper"

    async with AsyncClient(app=app, base_url="http://test") as ac:
        # First guess — should be accepted
        res1 = await ac.post(f"/game/guess?seed={seed}&guess={guess}")
        assert res1.status_code == 200
        assert "beats" in res1.json().get("message", "").lower()

        # Second identical guess — should trigger Game Over
        res2 = await ac.post(f"/game/guess?seed={seed}&guess={guess}")
        assert res2.status_code == 200
        assert "game over" in res2.json().get("message", "").lower()
