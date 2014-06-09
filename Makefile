all: thesis.dvi

thesis.dvi: thesis.tex atbeginend.sty iitmdiss.cls setspace.sty
	latex thesis.tex
	bibtex thesis.aux
	latex thesis.tex
	latex thesis.tex

clean:
	rm -rf *.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg thesis.dvi
	rm -rf chapters/*.aux
