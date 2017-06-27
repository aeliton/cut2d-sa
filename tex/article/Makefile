all:
	pdflatex scifile.tex
	bibtex scifile
	pdflatex scifile.tex
	pdflatex scifile.tex
	evince scifile.pdf

clean:
	rm -rf *.aux  *.nav *.log  *.out  *.snm  *.toc *.pdf *.bbl *.blg *.brf *.dvi *.idx *.lof *.lot *.ps

