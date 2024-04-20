# Twin Key

by steven

---

## Flag

```
LKS{EcD5A_iS_4bSoLut3Ly_S1mPl3}
```

## Description

Welcome to our humble encryptor. Unfortunately, it seems that something wrong with our encryptor, as someone can still decrypt our encryption even without knowing all the required data. Can someone figure it out what's wrong with our encryption? we are giving out a big prize for someone that can crack our encryptor with limited information!!

```bash
nc <HOST> <12000>
```

## Difficulty

medium-hard

## Hints

* Hint 1: Do you know any vulnerability on ECDSA
* Hint 2: ECDSA is a signing algorithm, find the one who responsible for encrypting

## Deployment

* Run the container using:

```bash
    docker-compose up --build --detach
```

## Tags

`private key`, `cryptography`,  `ecdsa`
