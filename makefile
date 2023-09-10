UserPackagesDir := $(HOME)/.config/sublime-text/Packages/User

CopySources := $(wildcard SublimeTRF*.*)
CopyTargets := $(CopySources:%=$(UserPackagesDir)/%)

SnippetSources := $(wildcard $(UserPackagesDir)/*.trf.sublime-snippet)
SnippetTargets := $(notdir $(SnippetSources))

.PHONY : all
all : $(CopyTargets) $(SnippetTargets)

$(CopyTargets) : $(UserPackagesDir)/SublimeTRF% : SublimeTRF% ; cp $< $@

.PHONY : clean reset
clean : ; rm -f *.trf.sublime-snippet
reset : | clean
