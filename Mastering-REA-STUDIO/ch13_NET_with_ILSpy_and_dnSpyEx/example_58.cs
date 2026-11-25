using Kettle.Core;

string tea = args.Length > 0 ? args[0] : "green";
int strength = args.Length > 1 ? int.Parse(args[1]) : 3;
int secs = Brew.Time(tea, strength);
if (secs < 0)
{
    Console.WriteLine($"error: unknown tea '{tea}'");
    return 3;
}
Console.WriteLine(
    $"{tea} {secs}s check={Brew.Checksum(tea)}");
return 0;
