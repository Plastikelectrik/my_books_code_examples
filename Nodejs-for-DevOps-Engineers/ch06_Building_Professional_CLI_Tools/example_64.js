// Book: Node.js for DevOps Engineers — Example 64
// src/commands/completion.js
export const meta = {
  name: 'completion',
  summary: 'Print shell completion script',
  usage: 'kes completion bash >> ~/.bashrc',
  options: {},
};

export async function run({ positionals }) {
  const words = [
    'version', 'health', 'certs', 'deploy', 'completion',
  ].join(' ');
  console.log(`_kes() {
  local cur=\${COMP_WORDS[COMP_CWORD]}
  COMPREPLY=( $(compgen -W "${words}" -- "$cur") )
}
complete -F _kes kes`);
}
