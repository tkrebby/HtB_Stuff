# WIDE (Reversing)

## Initial Look

As with any reversing challenge, first things first... find out what you're working with.  Run the `file` command on the binary to find out.

`wide: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=13869bb7ce2c22f474b95ba21c9d7e9ff74ecc3f, not stripped`

Next usual step, check for any interesting strings using `string`.  In this case, nothing too interesting; gonna have to look deeper.

## Ghidra

![Signal overview](https://raw.githubusercontent.com/tkrebby/HtB_Stuff/master/CA2022/images/wide1.png)

In Ghidra, take a look at the `menu` function.  We can see there's a comparison between the user input and the string, `sup3rs3cr3tw1d3` being made. This is likely our password to 'decrypt' the one 'encrypted' database.

## Binary Execution

Lets execute the ELF binary and see if the password we found in Ghidra works.

![Binary execution](https://raw.githubusercontent.com/tkrebby/HtB_Stuff/master/CA2022/images/wide2.png)

There's your flag: `HTB{str1ngs_4r3nt_4lw4ys_4sc11}`
