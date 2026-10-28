# 🛡️ TurnstileShield Python SDK

[![PyPI version](https://img.shields.io/badge/pypi-v1.0.2-blue.svg)](https://pypi.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Success Rate](https://img.shields.io/badge/Success%20Rate-99.8%25-brightgreen)](https://rapidapi.com/organization/aether-protocol-labs)

Instant Cloudflare Turnstile token resolution & `cf_clearance` session cookie generation.

```python
from turnstileshield.solver import TurnstileShield

shield = TurnstileShield(api_key="YOUR_RAPIDAPI_KEY")
result = shield.solve(page_url="https://nowsecure.nl", sitekey="0x4AAAAAAADnPIDROrmt1Wwj")
print("Token:", result["token"])
```
