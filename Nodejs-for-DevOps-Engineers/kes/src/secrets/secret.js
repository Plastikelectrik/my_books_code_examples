// A value that refuses to be printed (Chapter 7).
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
