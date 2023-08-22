UserPackagesDir := ~/.config/sublime-text/Packages/User

SnippetSources := $(wildcard $(UserPackagesDir)/*.trf.sublime-snippet)
SnippetTargets := $(notdir $(SnippetSources))

# This magically works for symlinked sources. But probably
#	only so long as the symlink isn't 'touch'-ed! :)
# TODO: Remove the symlinks from the UserPackageDir. Put
#	*all* the originals, the editable sources there.
OtherSources := $(wildcard $(UserPackagesDir)/SublimeTRF*.*)
OtherTargets := $(notdir $(OtherSources))

.PHONY : all
all : $(SnippetTargets) $(OtherTargets)

SublimeTRF% : $(UserPackagesDir)/SublimeTRF% ; cp $< $@
%.trf.sublime-snippet : $(UserPackagesDir)/%.trf.sublime-snippet ; cp $< $@

.PHONY : clean reset
clean : ; rm -f *.trf.sublime-snippet
reset : | clean
