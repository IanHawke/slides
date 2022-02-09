lectures: *.html
	make $(patsubst %.html,pdfs/%.pdf,$?)

pdfs/%.pdf: %.html
	decktape -s 3072x1920 reveal "$<?fragments=true" $@
