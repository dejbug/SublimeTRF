
# ST4 Integration for Tournament Report Format (TRF)

Here I will be working on [Sublime Text](https://www.sublimetext.com/) support for FIDE's "Tournament Report File". Take a look at [TRFXSample.txt](http://www.rrweb.org/javafo/aum/TRFXSample.txt) or [TRFXSample2.txt](http://www.rrweb.org/javafo/aum/TRFXSample2.txt), the two example `.trf` files from the [JaVaFo docs](http://www.rrweb.org/javafo/aum/JaVaFo2_AUM.htm).

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


# Notes To Self

All of this for `Sublime Text Build 4152`.

## Symbolic Links

With `.sublime-syntax` files it's enough to have a symlink in the User Packages folder. This **is not the case** with `.sublime-snippet` files!

## Snippets - Multiple Triggers with Trigger Insertion

There is a way for snippets to use [multiple triggers](https://forum.sublimetext.com/t/multiple-tabtrigger-tags-in-a-snippet/1409) but this was obviously a quick hack, [not a design decision](https://docs.sublimetext.io/guide/extensibility/snippets.html#snippets-file-format). For example: I want '^042' and '^052' to trigger the same snippet but re-insert the trigger text which obviously varies between invocations. The snippet fields start with `$1`, as in a shell script, but unlike a shell script `$0` has a different meaning. It seems that `$TM_CURRENT_WORD` was inteded for this but it only works with a single trigger; with multiple triggers it inserts a space. I went through the trouble to write a [bug report](https://github.com/sublimehq/sublime_text/issues/6113) for this.

This means **we need a snippet for every single trigger** no matter how similar they are.

## Snippets - Trigger Bug

Sometimes I [need to trigger the snippet twice](https://forum.sublimetext.com/t/tab-completion-for-snippets-with-unexpected-behavior/22564/3). I know this is a **bug** (and it wasn't solved, let alone properly understood in this forum thread) because when I enable command logging it works as expacted. Basically, when you observe it you collapse the waveform...

Edit: I've played around with it and here's the problem. SublimeText keeps the state of the snippet too long. You enter the snippet, you trigger it, fine. But if it has fields **you are expected to complete the snippet** rather than just delete it and start over. So it seems that [MrRobato](https://forum.sublimetext.com/t/tab-completion-for-snippets-with-unexpected-behavior/22564/6) was the only one who understood the issue even though their solution doesn't work.

Here's a way to reproduce it and see it in action.

Trigger a snippet with fields but don't complete the snippet, just press END and RETURN to insert a linebreak at the end of the current line. Write and trigger the snippet again but now try to complete the snippet (by cycling through its fields). The focus will jump to the fields of the previous, uncompleted snippet.

Edit: I was about to file a bug report but thankfully [somebody beat me to it](https://github.com/sublimehq/sublime_text/issues/5651).
