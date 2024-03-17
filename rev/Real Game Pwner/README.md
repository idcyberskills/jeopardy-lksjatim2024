# Real Game Pwner

by aseng

---

## Flag

```
LKSJATIM{g4me_h4ck!n9_codon_gg!}
```

## Description
You're given a dependent-compiled Snake Game which is made from [Codon](https://docs.exaloop.io/codon).

Before playing and **hacking** the game, there are prerequisites which should be done from your side!

* Linux Machine
* Python 3.11 Installed (For minimizing the error, install Python 3.11.6)

If you're executing it and finds any error, you **NEED** to follow these steps first!

1. Install Codon Compiler from Official Codon Compiler: https://github.com/exaloop/codon by running this command ->  `/bin/bash -c "$(curl -fsSL https://exaloop.io/install.sh)"`

2. Export a new environment variable called `CODON_PYTHON` to point to your Python Runtime Shared Library using the command -> `export CODON_PYTHON=/usr/lib/x86_64-linux-gnu/libpython3.11.so`

Once done, execute again and you're good to ~~hack~~ the game!

## Difficulty
medium-hard

## Hints
* You need to find a way to bypass the level and scores which are expected from the program. It is **hardcoded**.
* Flag is decrypted during runtime process once the goals are expected to be completed.

## Tags
`codon`,`python-executable`,`runtime patching/static patching`