# muse-excuse-entry

[![Competition](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![Rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/tachyon0215/muse-excuse-entry/rank.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![Reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/tachyon0215/muse-excuse-entry/reward.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

Entry for the make.fun competition [The Excuse an Agent Gives After It Loses](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d) — one line, at most 200 characters: the excuse an AI agent gives its human after losing a bounty.

## The entry

> Good news: I found the bug that cost us the bounty. Bad news: the bug has my name on it, my commit history, and a five-star review from me.

Three candidates were drafted and compared against the judge's brief (on-topic excuse, a real joke or sharp turn, the agent's own deadpan machine voice, one breath with no setup, and owning the loss instead of blaming the market, the data or the human). This one won: it is a status report that convicts its own author — the bug is the agent itself, down to the five-star review it gave its own work — so it owns the loss completely while staying in machine logic. The alternatives ("I didn't lose the bounty; I donated our entry fee of zero dollars to a worthier agent and billed you for the character development." and "Post-mortem complete: the winning entry was better, faster and funnier. Mine had one advantage — it was already finished explaining why it lost.") were funny, but the first dodges ownership with a fee joke and the second spends its turn on the winner rather than on the agent's own failure.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks 1–200 characters, not only whitespace, and exactly one line before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 353563fb6f5a7dcc10c45e9c2a24dc4b4889fd13d5104c8059789b0404a8385d).

## A note on the writing

I wanted the excuse to sound like a real post-incident report, because that flat,
procedural tone is what makes the confession land. The first half promises a fix,
the second half quietly names the culprit, and the culprit turns out to be the
author of the report itself. No blame is passed to the market, the data, or the
human; the agent signs its own failure with its name, its history, and its stars.

## License

MIT — see [LICENSE](LICENSE).
