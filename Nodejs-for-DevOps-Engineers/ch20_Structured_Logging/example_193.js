// Book: Node.js for DevOps Engineers — Example 193
// src/lib/context.js
import { AsyncLocalStorage } from 'node:async_hooks';
import { logger } from './logger.js';

const store = new AsyncLocalStorage();

export function withContext(fields, fn) {
  const parent = store.getStore()?.log ?? logger;
  return store.run({ log: parent.child(fields) }, fn);
}

export function log() {
  return store.getStore()?.log ?? logger;
}
