import fitz
import os
import shutil
from pathlib import Path

def tiff_to_pdf(source):
    '''
    Convert files from tiff to pdf from the source path
    Arguments:
        Source          - The list of source path of the tiff files
    Returns:
        tiff_result     - The list of destination path of the pdf files
    '''
    tiff_result = []
    for idx, dest_path in enumerate(source):
        try:
            pdf_doc = fitz.open(os.path.join(dest_path["staging"], dest_path['file_name'].split(".tiff")[0]+".pdf"))
            for page in pdf_doc:
                pix=page.get_pixmap(dpi=200)
                img_filename = dest_path["staging"] + "\\page-%04i.tiff" % page.number
                pix.pil_save(img_filename, format="TIFF", compression="tiff_adobe_deflate")
            tiff_result.append(dest_path)
        except Exception as err:
            #logging
            continue
    return tiff_result
