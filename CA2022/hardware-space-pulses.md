# Space Pulses (Hardware)

From previous CTFs and HTB challenges, I knew I would need [Logic2](https://www.saleae.com/downloads/) as soon as I saw the `.sal` file included w/ this challenge.

![Signal overview](https://raw.githubusercontent.com/tkrebby/HtB_Stuff/master/CA2022/images/space-pulse1.png)

## Initial Attempts

Generally, with these sort of challenges we need to figure out two things:
- The proper analyzer
- Baud rate

As far as analyzers go, this is a single channel capture so pretty solid bet it should be Async Serial.  From there, I ran a few measurements to try and find the baud rate.

![Baud rates](https://raw.githubusercontent.com/tkrebby/HtB_Stuff/master/CA2022/images/space-pulse2.png)

The measurement from the screenshot above gave us a baud rate of roughly 30 baud.  Plugged this number in with the Async Serial analyzer and got total garbage.

![Async Serial at 30 baud](https://raw.githubusercontent.com/tkrebby/HtB_Stuff/master/CA2022/images/space-pulse3.png)

Went as far as to mess with the various other Async Serial settings such as Bits Per Frame, Stop Bits, Parity Bit, Significant Bit, Signal Inversion, and Mode.  No luck there.  My next step was to check the baud rates again by expanding where I took measurements.  After playing with it for a while, I was able to snag about 3 or 4 different baud rates:  28 baud, 30 baud, and 988 baud to name a few.
