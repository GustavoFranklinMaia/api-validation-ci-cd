from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional
import requests


@dataclass(frozen=True)
class APIResponse:
    status_code: int
    json: Optional[Dict[str, Any]]
    elapsed_ms: float


class RickAndMortyClient:
    def __init__(self, base_url: str = "https://rickandmortyapi.com/api", timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str, params: Optional[dict] = None) -> APIResponse:
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = requests.get(url, params=params, timeout=self.timeout)
        elapsed_ms = resp.elapsed.total_seconds() * 1000

        try:
            body = resp.json()
        except ValueError:
            body = None

        return APIResponse(status_code=resp.status_code, json=body, elapsed_ms=elapsed_ms)

    def get_character_by_id(self, character_id: int) -> APIResponse:
        return self.get(f"character/{character_id}")

    def search_character(self, name: str) -> APIResponse:
        return self.get("character", params={"name": name})
