package com.example.kettle

object BrewCalculator {
    private val teas = mapOf(
        "green" to Pair(80, 120),
        "black" to Pair(95, 240),
        "oolong" to Pair(90, 180),
        "herbal" to Pair(100, 300),
    )

    fun brewTime(tea: String, strength: Int): Int {
        val (temp, base) = teas[tea] ?: return -1
        var t = base + (strength - 3) * 20
        if (temp < 85) t += (85 - temp) * 2
        return maxOf(t, 30)
    }

    fun checksum(s: String): Int {
        var h = 7L
        for (c in s) {
            h = (h * 31 + c.code) and 0xFFFFFFFFL
        }
        return (h % 10007).toInt()
    }
}
