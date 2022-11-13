from pdflatex import PDFLaTeX

pdfl = PDFLaTeX.from_texfile('C:/Users/ali_b/Desktop/LinalHWGen/HW1/tasks/221_var1.tex')
pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file = True, keep_log_file=True)