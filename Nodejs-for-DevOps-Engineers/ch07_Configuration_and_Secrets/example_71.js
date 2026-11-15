// Book: Node.js for DevOps Engineers — Example 71
// src/secrets/secret.js
import { inspect } from 'node:util';

export class Secret {
  #value;
  constructor(value) {
    this.#value = value;
  }
  reveal() {
    return this.#value;
  }
  toString() {
    return '[secret]';
  }
  toJSON() {
    return '[secret]';
  }
  [inspect.custom]() {
    return '[secret]';
  }
}
