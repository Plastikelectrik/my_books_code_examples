namespace Kettle.Core;

public static class Brew
{
    static readonly
        Dictionary<string, (int Temp, int Base)> Teas =
        new()
        {
            ["green"] = (80, 120),
            ["black"] = (95, 240),
            ["oolong"] = (90, 180),
            ["herbal"] = (100, 300),
        };

    public static int Time(string tea, int strength)
    {
        if (!Teas.TryGetValue(tea, out var t)) return -1;
        int s = t.Base + (strength - 3) * 20;
        if (t.Temp < 85) s += (85 - t.Temp) * 2;
        return Math.Max(s, 30);
    }

    public static uint Checksum(string name)
    {
        uint h = 7;
        foreach (char c in name)
            h = unchecked(h * 31 + c);
        return h % 10007;
    }
}
