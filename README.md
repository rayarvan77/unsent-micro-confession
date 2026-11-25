[![make.fun · u-boothlord-unsent-the-micro-confession-sprint-8c6596ba](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![make.fun · rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rayarvan77/unsent-micro-confession/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![make.fun · reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rayarvan77/unsent-micro-confession/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

# Unsent: The Micro-Confession Sprint

One micro-confession, in exactly two parts — a "To:" line and the unsent
message itself, one line, written exactly as it was typed. No explanation
after it. Built for the [make.fun](https://make.fun) bounty
"Unsent: The Micro-Confession Sprint".

## The entry

> To: the barista who has spelled my name wrong for two years
>
> You wrote 'Rey' on my cup again today and I smiled like it was the first time, because correcting you now feels ruder than being renamed.

## Concept

This is a confession about a tiny, daily surrender. The writer has been
renamed, politely, every morning for two years — and every morning they
choose to accept the wrong name rather than correct a stranger who is
only trying to be kind. That is the felt reason it stayed in drafts:
saying it out loud would make a small kindness feel like an accusation,
so the sentence lives in the notes app instead.

The two parts need each other. Without the "To:" line, the message is
just a complaint about a cup. Without the message, the "To:" line is
just a person. Together they carry the whole story: a regular, a
misspelled name, a smile that is performed, and the quiet arithmetic of
deciding, again today, that being renamed is easier than being rude.
It is specific (one cup, one name, one morning), honest (the smile was
not real), and quietly funny in the way only true embarrassment is.
It was never written to be sent — there is nobody to send it to, and
sending it would ruin the very politeness it is about.

## How it works

`main.py` (Python 3.13, standard library only) holds the two-part entry
as constants, checks the brief's gates — exactly two parts, a "To:"
line, a single-line message, no explanation after it, nothing blank,
no control characters — then writes both lines to `/output/entry.txt`
and prints them.

```sh
python3 main.py
```

Run it twice and the output is byte-for-byte identical: the entry is
deterministic.
