
# trf - Tournament Report File

Here I will be working on [SublimeText](https://www.sublimetext.com/) support for FIDE's "Tournament Report File". Take a look at [TRFXSample.txt](http://www.rrweb.org/javafo/aum/TRFXSample.txt) or [TRFXSample2.txt](http://www.rrweb.org/javafo/aum/TRFXSample2.txt), the two example `.trf` files from the [JaVaFo docs](http://www.rrweb.org/javafo/aum/JaVaFo2_AUM.htm).

## Syntax

For now, just a quick syntax highlighter. More things should be forthcoming to facilitate hand-editing.

The TRF specs can be found at the bottom of [C04 Appendix A](https://handbook.fide.com/chapter/C04A). You will find two versions, old and new, namely [TRF06](https://handbook.fide.com/files/handbook/fidexchg.txt) (from 2006) and [TRF16](https://handbook.fide.com/files/handbook/C04Annex2_TRF16.pdf) (from 2016).

Still lacking in the highlighter are the [extensions](http://www.rrweb.org/javafo/aum/JaVaFo2_AUM.htm#_Extensions_and_other_). I will need to take a look at the docs/sources of the [FIDE-approved](https://handbook.fide.com/files/handbook/C04Annex3_FEP19.pdf) tournament pairers which consume this format first. Currently there are just two approved: [JaVaFo](http://www.rrweb.org/javafo) (Java) and the more recent [bbpPairings](https://github.com/BieremaBoyzProgramming/bbpPairings) (C++).

## Odds and Ends

The current standard (2016) has a couple design oddities which I did not attempt to remedy or discourage in the syntax file:

There are three different date formats: DD/MM/YYYY (tournament start/end), YYYY/MM/DD (player birthdate), and YY/MM/DD (round start).

Player's gender is binary. This can be easily remedied.

If a player's FIDE title exceeds two letters (i.e. WGM, WIM, WFM, WCM) then there is no space left for a field separator between 'gender' and 'title'. A workaround could be to simply imply the 'W' in 'WGM' from the previous field.

Team names may touch the first player ID. The only workaround is to keep the team names shorter than the allowable space.
