all: pdfs/lecture1.pdf pdfs/lecture2.pdf pdfs/lecture3.pdf

clean:
	rm -f pdfs/*pdf

pdfs/%.pdf: %.html
	mkdir -p pdfs
	decktape --size 2732x1536 reveal $< $@
