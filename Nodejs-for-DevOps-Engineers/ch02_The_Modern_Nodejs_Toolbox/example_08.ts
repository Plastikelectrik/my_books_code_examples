// Book: Node.js for DevOps Engineers — Example 08
// src/list-services.ts
import { label, type Service } from './lib/service.ts';

const services: Service[] = [
  { name: 'api', url: 'https://api.example.com',
    team: 'core', critical: true },
  { name: 'billing', url: 'https://bill.example.com',
    team: 'payments' },
];

for (const s of services) console.log(label(s));
