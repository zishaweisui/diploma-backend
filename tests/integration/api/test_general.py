import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_general(client: AsyncClient) -> None:
    response = await client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"message": "Healthy"}
