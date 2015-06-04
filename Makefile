# How to run Python.
PYTHON = python3

# where generated content lands
OUTPUT_DIR = output

all : commands

## commands     : show all commands.
commands : Makefile
	@sed -n 's/^## //p' $<

## serve        : launch acrylamid in autocompile mode
serve :
	acrylamid autocompile

## clean        : remove files generated by acrylamid
clean :
	rm -rf ${OUTPUT_DIR}

## copystatic   : copy CNAME, .nojekyll and other static files to the ${OUTPUT_DIR}
copystatic :
	mkdir -p ${OUTPUT_DIR}
	cp CNAME ${OUTPUT_DIR}
	cp .nojekyll ${OUTPUT_DIR}
	cp LICENSE ${OUTPUT_DIR}
	cp README.rst ${OUTPUT_DIR}

## compile      : compile to the output
compile :
	acrylamid compile

## deploy       : deploy everything to the GitHub pages
deploy :
	make clean
	make copystatic
	make compile
	ghp-import -b master -p "${OUTPUT_DIR}"
