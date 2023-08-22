UserPackagesDir := ~/.config/sublime-text/Packages/User

SnippetSources := $(wildcard $(UserPackagesDir)/*.trf.sublime-snippet)
SnippetTargets := $(notdir $(SnippetSources))

.PHONY : all
all : $(SnippetTargets)

%.trf.sublime-snippet : $(UserPackagesDir)/%.trf.sublime-snippet ; cp $< $@

.PHONY : clean reset
clean : ; rm -f *.trf.sublime-snippet
reset : | clean
