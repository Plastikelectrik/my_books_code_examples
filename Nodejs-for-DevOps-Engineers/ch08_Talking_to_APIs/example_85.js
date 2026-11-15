// Book: Node.js for DevOps Engineers — Example 85
// examples/graphql.js
const query = `
  query($org: String!) {
    organization(login: $org) {
      repositories(first: 50, isArchived: false) {
        nodes { name defaultBranchRef { name } }
      }
    }
  }`;

const res = await fetch('https://api.github.com/graphql', {
  method: 'POST',
  headers: {
    Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    query,
    variables: { org: 'kestrel' },
  }),
  signal: AbortSignal.timeout(10_000),
});
const { data, errors } = await res.json();
if (errors) throw new Error(errors[0].message);
console.log(data.organization.repositories.nodes);
