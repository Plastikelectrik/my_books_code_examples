// Book: Node.js for DevOps Engineers — Example 68
// src/lib/banner.js
import { styleText } from 'node:util';

export function envBanner(config) {
  if (config.env !== 'production') return;
  const text = ' PRODUCTION ';
  console.error(styleText(['bgRed', 'white', 'bold'], text)
    + ` region ${config.region}`);
}
