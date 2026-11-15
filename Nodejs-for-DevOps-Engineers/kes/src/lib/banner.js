// Make production impossible to miss (Chapter 7).
import { styleText } from 'node:util';

export function envBanner(config) {
  if (config.env !== 'production') return;
  const text = ' PRODUCTION ';
  console.error(styleText(['bgRed', 'white', 'bold'], text)
    + ` region ${config.region}`);
}
