// Book: Node.js for DevOps Engineers — Example 80
// src/commands/github/audit.js
import { github } from '../../integrations/github.js';
import { paginateLinks } from '../../lib/paginate.js';
import { mapLimit } from '../../lib/pool.js';
import { HttpError } from '../../lib/api-client.js';
import { Secret } from '../../secrets/secret.js';

export const meta = {
  name: 'github audit',
  summary: 'Find repos without default-branch protection',
  usage: 'kes github audit --org NAME [--json]',
  options: {
    org: { type: 'string', description: 'Organisation' },
  },
};

export async function run({ values, out }) {
  const gh = github(new Secret(process.env.GITHUB_TOKEN));
  const repos = [];
  for await (const r of paginateLinks(gh,
    `/orgs/${values.org}/repos`, { per_page: 100 })) {
    if (!r.archived) repos.push(r);
  }
  out.info(`auditing ${repos.length} repositories`);

  const results = await mapLimit(repos, 6, async (r) => {
    const branch = r.default_branch;
    try {
      const base = `/repos/${r.full_name}/branches`;
      await gh.get(`${base}/${branch}/protection`);
      return { repo: r.full_name, protected: true };
    } catch (err) {
      if (err instanceof HttpError && err.status === 404) {
        return { repo: r.full_name, protected: false };
      }
      throw err;
    }
  });

  const missing = results.filter((r) => !r.protected);
  out.result(missing, (rows) => {
    for (const r of rows) console.log(out.bad(r.repo));
    const n = results.length;
    console.log(`${rows.length} of ${n} unprotected`);
  });
  if (missing.length) process.exitCode = 1;
}
