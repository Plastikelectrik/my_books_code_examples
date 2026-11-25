package com.example.kettle

import android.app.Activity
import android.os.Bundle
import android.widget.TextView

class MainActivity : Activity() {
    override fun onCreate(state: Bundle?) {
        super.onCreate(state)
        val tea = "green"
        val secs = BrewCalculator.brewTime(tea, 3)
        val check = BrewCalculator.checksum(tea)
        val view = TextView(this)
        view.text = "$tea ${secs}s check=$check"
        setContentView(view)
    }
}
