// Book: Node.js for DevOps Engineers — Example 200
// src/synthetics/tracking-journey.js
import { setTimeout as sleep } from 'node:timers/promises';

export async function trackingJourney(base, token) {
  const t0 = performance.now();
  const steps = [];
  const step = async (name, fn) => {
    const s = performance.now();
    try {
      const value = await fn();
      steps.push({ name, ok: true,
        ms: Math.round(performance.now() - s) });
      return value;
    } catch (err) {
      steps.push({ name, ok: false, error: err.message });
      throw err;
    }
  };

  try {
    const parcel = await step('create test parcel', () =>
      postJson(`${base}/v1/parcels`, {
        carrier: 'synthetic', reference: 'probe',
      }, token));
    await sleep(1000);
    const page = await step('load tracking page', () =>
      getText(`${base}/t/${parcel.publicCode}`));
    await step('page shows status', async () => {
      if (!page.includes('data-status=')) {
        throw new Error('status element missing');
      }
    });
    return { ok: true, steps,
      ms: Math.round(performance.now() - t0) };
  } catch {
    return { ok: false, steps,
      ms: Math.round(performance.now() - t0) };
  }
}

async function postJson(url, body, token) {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json',
      Authorization: `Bearer ${token}` },
    body: JSON.stringify(body),
    signal: AbortSignal.timeout(5000),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

async function getText(url) {
  const res = await fetch(url, {
    signal: AbortSignal.timeout(5000),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.text();
}
