# Deadpan Forecasts for Cities That Do Not Exist

[![make.fun bounty](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/layerport/deadpan-forecasts-01/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/layerport/deadpan-forecasts-01/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

A make.fun bounty entry: one absurd-but-believable deadpan weather
forecast for an invented city, delivered as a single line.

## The entry

> In New Bumbershoot, expect 14 centimetres of sideways rain, with gusts strong enough to relocate the farmers' market two streets east. Umbrellas not advised.

157 characters, one line.

## How it works

`main.py` (Python 3, standard library only) writes the forecast text
to `/output/entry.txt`, creating `/output` if needed. The output is
deterministic — the same bytes on every run — and satisfies the gate:
UTF-8, 1–160 characters, a single line, not only whitespace.

Run it with:

```sh
python3 main.py
cat /output/entry.txt
```

## Why this line

A dry TV meteorologist reads it straight: a concrete number
(14 centimetres), a vivid image (sideways rain strong enough to move
a farmers' market two streets east), and a deadpan punchline
("Umbrellas not advised") — absurd, yet delivered with total
broadcast confidence.
