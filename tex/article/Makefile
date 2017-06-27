all:
	pdflatex *.tex
	bibtex scifile
	pdflatex *.tex
	pdflatex *.tex
	evince *.pdf

clean:
	rm -rf *.aux  *.nav *.log  *.out  *.snm  *.toc *.pdf *.bbl *.blg *.brf *.dvi *.idx *.lof *.lot *.ps

