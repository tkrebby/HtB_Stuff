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

## Manual Analysis

With the variable baud rates, I figured the analyzers would be no help and decided to move on to a manual analysis.  So, where can we get data from? What about the length of each burst?

![Manual measurements](https://raw.githubusercontent.com/tkrebby/HtB_Stuff/master/CA2022/images/space-pulse4.png)

This looks promising!! After traversing through the entire signal, we get the following burst lengths:

`68 112 112 115 101 106 111 98 117 102 116 33 46 33 83 66 33 50 58 105 33 54 57 110 33 51 51 116 33 125 33 69 102 100 33 44 52 54 43 33 50 51 40 33 55 40 40 33 46 33 87 98 109 106 101 98 117 106 112 111 33 116 102 100 115 102 117 33 100 112 101 102 59 33 73 85 67 124 113 118 50 54 52 54 96 110 49 101 118 50 53 56 50 111 58 96 50 111 96 54 113 53 100 52 34 54 51 38 126 1 1 1 1`

## Deciphering the Code

Tried converting the data directly to ASCII, but got garbage results:

``Dppsejobuft!.!SB!2:i!69n!33t!}!Efd!,46+!23(!7((!.!Wbmjebujpo!tfdsfu!dpef;!IUC|qv2646`n1ev2582o:`2o`6q5d4"63&~....``

Off to Rumkin's [Cipher Identifier](https://www.dcode.fr/cipher-identifier) to see if there are any clues on how to move forward with this possibility. The cipher identifier suggested this could be an [ASCII Shift Cipher](https://www.dcode.fr/ascii-shift-cipher).  Let's check it out.

![ASCII shift cipher](https://raw.githubusercontent.com/tkrebby/HtB_Stuff/master/CA2022/images/space-pulse5.png)

`Coordinates - RA 19h 58m 22s | Dec +35* 12' 6'' - Validation secret code: HTB{pu1535_m0du1471n9_1n_5p4c3!52%}`

And there's our flag: `HTB{pu1535_m0du1471n9_1n_5p4c3!52%}`
