// Book: Node.js for DevOps Engineers — Example 13
// scripts/maintenance-window.js
const start = Temporal.ZonedDateTime.from(
  '2026-12-06T02:00:00[Europe/Madrid]',
);
const end = start.add({ hours: 2 });

for (const zone of ['UTC', 'America/New_York']) {
  const local = start.withTimeZone(zone);
  console.log(zone.padEnd(18), local.toString());
}
console.log('duration', start.until(end).toString());
