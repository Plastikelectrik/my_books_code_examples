import { COMMANDS } from '../index.js';

export const meta = {
  name: 'completion',
  summary: 'Print a Bash completion script',
  usage: 'kes completion >> ~/.bashrc',
  options: {},
};

export async function run() {
  const words = [...new Set(Object.keys(COMMANDS)
    .map((k) => k.split(' ')[0]))].join(' ');
  console.log(`_kes() {
  local cur=\${COMP_WORDS[COMP_CWORD]}
  COMPREPLY=( $(compgen -W "${words}" -- "$cur") )
}
complete -F _kes kes`);
}
