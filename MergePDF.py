from PyPDF2 import PdfFileMerger
from glob import glob
import os

def merge_pdf(**kwargs):
    '''
    Merge group of pdf files to a single pdf.
    Arguments:
        Source          - The source path of the pdf files
        target_folder   - The target folder to copy the merged pdf
        target_filename - The target file name of the merged pdf
    Returns:
        None
    '''
    merger = PdfFileMerger()
    for pdf_path in glob(kwargs['source'] + "\\*.pdf"):
        merger.append(pdf_path)
    os.makedirs(kwargs['target_folder'], exist_ok=True)
    merger.write(os.path.join(kwargs['target_folder'], kwargs['target_filename'] + ".pdf"))
    merger.close()
    return
