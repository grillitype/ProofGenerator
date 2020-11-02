import os
#input sample string text
fin = open("GT-Sample-Strings.txt", "rt")
#output files, seperated in scripts
flbasic = open("latin-basic.txt", "wt")
fl = open("latin-kerning.txt", "wt")
fcbasic = open("cyrillic-basic.txt", "wt")
fc= open("cyrillic-kerning.txt", "wt")
fgbasic = open("greek-basic.txt", "wt")
fg= open("greek-kerning.txt", "wt")
#for each line in the input file
for line in fin:
	#sort lines into scripts and format for InDesign
    if line.startswith("2.1") or line.startswith("2.2"):
        flbasic.write(line.replace('\\n', '\r\n'))
    elif line.startswith("3."):
         fl.write(line.replace('\\n', '\r\n'))
    elif  line.startswith("4.1") or line.startswith("4.2"):
        fcbasic.write(line.replace('\\n', '\r\n'))
    elif line.startswith("5."):
        fc.write(line.replace('\\n', '\r\n'))
    elif  line.startswith("6.1") or line.startswith("6.2"):
        fgbasic.write(line.replace('\\n', '\r\n'))
    elif line.startswith("7."):
        fg.write(line.replace('\\n', '\r\n'))
#close input and output files
print("done sorting the sample strings")
fin.close()
flbasic.close()
fl.close()
fcbasic.close()
fc.close()
fgbasic.close()
fg.close()