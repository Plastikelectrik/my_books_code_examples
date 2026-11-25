D=~/studio/targets/kettle-dotnet/Kettle.Core.dll
rea inspect-managed-artifact "$D"
rea inspect-managed-members "$D" --json \
  > ~/studio/evidence/kettle-dotnet/members.json
