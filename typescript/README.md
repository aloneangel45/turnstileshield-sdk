# 🛡️ turnstileshield-sdk (Node.js)

Cloudflare Turnstile solver client for Node.js, TypeScript, and Bun.

```javascript
const { TurnstileShield } = require('turnstileshield-sdk');
const solver = new TurnstileShield('YOUR_RAPIDAPI_KEY');

async function test() {
  const res = await solver.solve('https://nowsecure.nl', '0x4AAAAAAADnPIDROrmt1Wwj');
  console.log('Solved token:', res.token);
}
test();
```
