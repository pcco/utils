#!/bin/bash
# This script requires having the texlive-binextra and texlive-latexrecommended packages installed on ARCH

[[ -z "${1}" ]] && echo "[ERROR]: input pdf file is required" && exit 1
[[ ! -f "${1}" ]] && echo "[ERROR]: ${1} doesn't exist" && exit 1

source_pdf_statement="${1}"
pdfjam "${source_pdf_statement}" '1,1' \
  "${source_pdf_statement}" '2,2' \
  --paper letterpaper,landscape \
  --nup 2x1 \
  --outfile "${source_pdf_statement%.*}-print.pdf"

