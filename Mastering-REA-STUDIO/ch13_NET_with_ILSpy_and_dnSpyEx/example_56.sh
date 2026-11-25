mkdir -p ~/studio/targets/kettle-dotnet && cd "$_"
dotnet new classlib -n Kettle.Core
dotnet new console -n Kettle.Cli
dotnet add Kettle.Cli reference Kettle.Core
