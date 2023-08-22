
# trf - Tournament Report File

Here I will be working on [SublimeText](https://www.sublimetext.com/) support for FIDE's "Tournament Report File". Take a look at [TRFXSample.txt](http://www.rrweb.org/javafo/aum/TRFXSample.txt) or [TRFXSample2.txt](http://www.rrweb.org/javafo/aum/TRFXSample2.txt), the two example `*.trf` files from the [JaVaFo docs](http://www.rrweb.org/javafo/aum/JaVaFo2_AUM.htm).

## Syntax

For now, just a quick syntax highlighter. More things should be forthcoming to facilitate hand-editing.

The TRF specs can be found at the bottom of [C04 Appendix A](https://handbook.fide.com/chapter/C04A). You will find two versions, old and new, namely [TRF06](https://handbook.fide.com/files/handbook/fidexchg.txt) (from 2006) and [TRF16](https://handbook.fide.com/files/handbook/C04Annex2_TRF16.pdf) (from 2016).

Still lacking in the highlighter are the [extensions](http://www.rrweb.org/javafo/aum/JaVaFo2_AUM.htm#_Extensions_and_other_). I will need to take a look at the docs/sources of the [FIDE-approved](https://handbook.fide.com/files/handbook/C04Annex3_FEP19.pdf) tournament pairers which consume this format first. Currently there are just two approved: [JaVaFo](http://www.rrweb.org/javafo) (Java) and the more recent [bbpPairings](https://github.com/BieremaBoyzProgramming/bbpPairings) (C++).
