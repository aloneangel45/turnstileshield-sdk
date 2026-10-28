import httpx
from typing import Dict, Any, Optional

class TurnstileShield:
    """
    Client for resolving Cloudflare Turnstile challenges & acquiring cf_clearance cookies.
    """
    def __init__(
        self,
        api_key: str,
        host: str = "turnstileshield-cloudflare-turnstile-solver-api.p.rapidapi.com"
    ):
        self.api_key = api_key
        self.host = host
        self.base_url = f"https://{self.host}/api/v1/turnstile"
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.host,
            "Content-Type": "application/json",
            "User-Agent": "TurnstileShield-Python/1.0.2"
        }

    def solve(
        self,
        page_url: str,
        sitekey: str,
        action: Optional[str] = None,
        data: Optional[str] = None
    ) -> Dict[str, Any]:
        """Solve a Turnstile challenge and return token + cf_clearance."""
        payload = {"page_url": page_url, "sitekey": sitekey}
        if action: payload["action"] = action
        if data: payload["data"] = data

        with httpx.Client(timeout=30.0) as client:
            resp = client.post(f"{self.base_url}/solve", headers=self.headers, json=payload)
            resp.raise_for_status()
            return resp.json()
