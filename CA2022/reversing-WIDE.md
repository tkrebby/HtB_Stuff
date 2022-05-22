# WIDE (Reversing)

## Initial Look

As with any reversing challenge, first things first... find out what you're working with.  Run the `file` command on the binary to find out.

`wide: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=13869bb7ce2c22f474b95ba21c9d7e9ff74ecc3f, not stripped`

Next usual step, check for any interesting strings using `string`.  In this case, nothing too interesting; gonna have to look deeper.

## Ghidra

