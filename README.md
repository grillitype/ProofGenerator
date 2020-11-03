# ProofGenerator
![](data/PG-bw-small.gif)

 A tool to automatically generate Proofs, with predefined sample strings InDesign. 
 Based on SpecimenDropper, by Alphabet Type:
 https://github.com/AlphabetType/SpecimenDropper/releases/tag/1.0
 
 # Setup and Usage of the ProofGenerator
- Download and unpack "ProofGenerator.app.zip"
- Drop ProofGenerator.app into Applications folder
- drag and drop on, or more font files (.otf, .ttf) into ProofGenerator

# GT Sample Strings
 This .txt file can be used in the Font Editor to display and check the proportions, spacing, kerning etc. of your font

 General structure of GT-Sample-Strings.txt: 
 1) basics to check proportions in UC and LC latin, spacing of glyphs/numerals/”special” characters
 2-3) latin spacing, lating kerning (latin plus, by underware) 
 4-5) cyrillic spacing, cyrillic kerning (adobe cyrillic 2)
 6-7) greek spacing, greek kerning (adobe greek 1)
 8) additional things to check  (kerning exceptions, lc+UC kerning strings for Latin, language specific details, etc.)
 

 ## Resources 
(right click on ProofGenerator app > Show package contents > Resources)
- template_proof.idml: 

 Layout Template for the InDesign Proof, contains kerning strings for latin, cyrillic and greek languages (to be expanded).

- sort-samplestrings.py:

 A python script to sort and split the GT-Sample-Strings.txt into seperate text files. Takes the lines starting with

- other .txt files (latin-basic.txt, latin-kerning.txt, etc.)

 are exported from "GT-Sample-Strings.txt" via the sort-samplestrings.py script and are being linked in the idml Layout template

- ProofGenerator.py

 A python script 

 
 Comes with a kerning sample text latin, cyrillic and greek kerning (to be expanded with more languages). 
 
 
 ... explain sample strings, characterset etc.
 



## Customisation
