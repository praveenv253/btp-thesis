all: thesis.dvi

thesis.dvi: thesis.tex atbeginend.sty iitmdiss.cls setspace.sty \
            customdefs.tex frontmatter/*.tex chapters/*.tex
	latex thesis.tex
	bibtex thesis.aux
	latex thesis.tex
	latex thesis.tex

pdf: thesis.pdf

thesis.pdf: thesis.dvi
	dvipdf thesis.dvi

clean:
	rm -rf *.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg chapters/*.aux
	rm -rf thesis.dvi thesis.pdf
