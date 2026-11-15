// Book: Node.js for DevOps Engineers — Example 150
// test/repository.test.js
import { test, before, after } from 'node:test';
import { startPostgres } from './helpers/postgres.js';

let pg;
before(async () => { pg = await startPostgres(); });
after(async () => { await pg?.stop(); });

test('stores and reads a parcel', async () => {
  // connect to pg.url and test real SQL here
});
