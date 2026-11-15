// Book: Node.js for DevOps Engineers — Example 15
// eslint.config.js
import js from '@eslint/js';
import globals from 'globals';

export default [
  js.configs.recommended,
  {
    languageOptions: {
      globals: globals.node,
    },
    rules: {
      'no-unused-vars': ['error', { args: 'none' }],
    },
  },
];
