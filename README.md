Seems most bindings use a DLL file to do the actual parsing. (see: xdrk, xrk, pyxrk-dev)

Since AIM provides this, it begs the question-- is that better than their CSV?

Binary analysis of the xrk files:

Using some pattern matching, it seems XRK also contain computed fields the AIM device shows:

Field Names
Ref Lap Diff
Prev Lap Diff
Best Today Diff
Predictive Time
Best Time
Master Clk
Distance Lap Int
MClk
Roll Time
Best Run Diff
Distance Lap
Lap Time
Best Lap of Today. Valid.


But, this doesn't seem to make up for the massive file size difference, unless the device checkpoints these values.
.... That might be the cleanest explanation.

Napkin math: 6mb vs 8.6mb. 13 fields to checkpoint with a 4 byte float vs 36 fields.

roughly 1/3 more? 33% more space ~~ 8.6mb? Checkpointing is a clean guess but more probing is needed. 



<b>06/03/2024 Progress</b>
Can make good pandas out of csv with pretty units in column names.
Can compare two 