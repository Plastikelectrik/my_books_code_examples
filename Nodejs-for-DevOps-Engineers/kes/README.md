# kes — the Kestrel platform CLI

This folder is the **runnable version of the capstone project** of
*Node.js for DevOps Engineers* (Chapter 26). It gathers the pieces
built across the book (async helpers, configuration, the API client,
deploy plans, canary analysis, release automation, fleet tasks,
Kubernetes and Docker checks, alert deduplication) into one CLI you
can clone, test and extend.

The numbered `example_NN` files in the chapter folders show each
piece exactly as printed in the book. Here the same code is wired
together, sometimes slightly simplified so it runs without a real
cloud account. Where it differs from the book, a comment says so.

## Quick start

```bash
cd kes
npm ci                 # installs semver, yaml and zod
npm test               # 37 tests with the built-in node:test runner
node src/cli.js --help
npm link               # optional: makes the `kes` command available
```

Requires Node.js 22.13 or newer (the book uses 24 or 26 LTS).

## Commands you can try right away (no cloud needed)

| Command | What it does |
|---|---|
| `kes services list` | Lists the services in `services.yaml` |
| `kes config show --json` | Effective configuration after all layers (secrets redacted) |
| `kes health` | Checks every health URL. Start `node examples/demo-server.js` first; `inventory` fails on purpose |
| `kes deploy orders-api --env staging --sha abc1234` | Prints the deploy plan (dry run) |
| `kes kube audit deploy/orders-api.yaml` | Policy checks: one Deployment passes, one fails |
| `kes canary demo` / `kes canary demo --bad` | Simulated canary: promoted, or rolled back at 5% |
| `kes docker cleanup --from examples/docker-state.json` | Cleanup plan from a saved Docker state |
| `kes release` | Next version and release notes from Conventional Commits (run it inside a git repo with a `v*` tag) |
| `kes supply audit` | Lockfile check plus `npm audit` summary |
| `kes completion >> ~/.bashrc` | Bash completion |

Every command accepts `--json` for machine-readable output and
`--help` for its options.

## Commands that touch real systems

| Command | Needs |
|---|---|
| `kes deploy ... --apply` | `docker`, `kubectl` and a cluster context named like the environment |
| `kes docker cleanup --apply` | A local Docker daemon |
| `kes fleet exec "uptime" --hosts db,eu` | SSH access (key-based) to the hosts in `inventory.yaml` |
| `kes fleet disk` | Same as above |
| `kes certs check example.com` | Outbound TLS connections |

Changes are dry runs unless you pass `--apply`. With `--apply` the
CLI asks for confirmation, and refuses to continue without `--yes`
when no terminal is attached (CI). Production prints a red banner.
Practise against staging or local tools, never production.

## Configuration

Layers, lowest to highest priority: built-in defaults →
`kes.config.json` in the current folder → `~/.config/kes/config.json`
→ the profile chosen with `--profile` or `KES_PROFILE` → `KES_*`
environment variables → command-line flags. See
`src/config/load.js`.

## Layout

```
src/cli.js            entry point and command router
src/context.js        config, output and lazy catalogue for commands
src/commands/         one file per command (meta + run)
src/lib/              pool, retry, timeouts, run, output, errors...
src/config/           schema and layered loader
src/catalog/          service catalogue schema and loader
src/deploy/           plan (pure) and execute
src/canary/           analysis, controller, traffic routers
src/release/          git history, commit parsing, notes, image tags
src/fleet/            inventory, SSH, rolling runs, output grouping
src/kube/ src/docker/ rollout state, policy audit, cleanup plan
src/alerts/           alert model and SQLite deduplication state
test/                 node:test suites
```

## License

MIT, like the rest of this repository.
