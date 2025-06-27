#!/bin/bash
# This script is used to convert a statement size pdf into a side by side letter document.
# This is useful for the communication's team can then make copies and use the paper cutter
# to create 2 bulletins per page.
#
# Known dependencies on a ARCH Linux System:
#   - texlive-binextra
#   - texlive-latexrecommended

[[ -z "${1}" ]] && echo "[ERROR]: input pdf file is required" && exit 1
[[ ! -f "${1}" ]] && echo "[ERROR]: ${1} doesn't exist" && exit 1
source_pdf_statement="${1}"

# The scale is set to 0.99 to make sure the content fits within the
# printable margins
pdfjam "${source_pdf_statement}" '1,1' \
  "${source_pdf_statement}" '2,2' \
  --paper letterpaper,landscape \
  --scale 0.99 \
  --offset '0cm 0cm' \
  --clip false \
  --nup 2x1 \
  --outfile "${source_pdf_statement%.*}-print.pdf"

