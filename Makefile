all: thesis.dvi

thesis.dvi: thesis.tex atbeginend.sty iitmdiss.cls setspace.sty refs.bib \
            customdefs.tex frontmatter/*.tex chapters/*.tex images/* \
            appendices/*.tex
	latex thesis.tex
	bibtex thesis.aux
	latex thesis.tex
	latex thesis.tex

pdf: thesis.pdf

thesis.pdf: thesis.dvi
	dvipdf thesis.dvi

clean:
	rm -rf *.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg
	rm -rf chapters/*.aux frontmatter/*.aux appendices/*.aux
	rm -rf thesis.dvi thesis.pdf
