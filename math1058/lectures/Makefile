lectures: *.html
	make $(patsubst %.html,%.pdf,$?)

%.pdf: %.html
	decktape -s 3072x1920 reveal $< $@
