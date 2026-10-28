const axios = require('axios');

class TurnstileShield {
  constructor(apiKey, host = 'turnstileshield-cloudflare-turnstile-solver-api.p.rapidapi.com') {
    this.apiKey = apiKey;
    this.host = host;
    this.http = axios.create({
      baseURL: `https://${this.host}/api/v1/turnstile`,
      timeout: 30000,
      headers: {
        'x-rapidapi-key': this.apiKey,
        'x-rapidapi-host': this.host,
        'Content-Type': 'application/json'
      }
    });
  }

  async solve(pageUrl, sitekey, action, data) {
    const payload = { page_url: pageUrl, sitekey };
    if (action) payload.action = action;
    if (data) payload.data = data;
    const res = await this.http.post('/solve', payload);
    return res.data;
  }
}

module.exports = { TurnstileShield };
