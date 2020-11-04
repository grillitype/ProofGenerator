# ProofGenerator
![](data/PG-bw-small.gif)

 A tool to automatically generate Kerning Proofs with predefined sample strings in InDesign. 
 
 The ProofGenerator is based on SpecimenDropper, by Alphabet Type:
 https://github.com/AlphabetType/SpecimenDropper/releases/tag/1.0
 
 ### Setup and Usage of the ProofGenerator
- Download and unpack "ProofGenerator.app.zip"
- Drop ProofGenerator.app into Applications folder
- drag and drop on, or more font files (.otf, .ttf) into ProofGenerator

 ### Resources 
(right click on ProofGenerator app > Show package contents > Resources)

- template_proof.idml: Layout Template for the InDesign Proof.
- sort-samplestrings.py: A python script to sort and split the GT-Sample-Strings.txt into seperate text files. 
- other .txt files (latin-basic.txt, latin-kerning.txt, etc.) are exported from "GT-Sample-Strings.txt" via the sort-samplestrings.py script and are being linked in the idml Layout template

### Customisation
You can customise the layout and content of the template_proof.idml to fit all your proofing needs and edit/add to the sample text. Make sure to run sort-samplestrings.py script, after you made changes to the Sample Text and update the link to the txt files in InDesign. You currently have to use a non-standard font in the layout document, so the program understands what text will be displayed with your font. Also you have to align the text to the grid manually after re-linking the txt files, because paragraph styles are not working (yet).  
Check out Alphabet Types SpecimenDropper if you want to generate type specimens https://github.com/AlphabetType/SpecimenDropper


 
# GT-SampleStrings
 The GT-Sample-Strings.txt file can be used in the Font Editor to display and check the proportions, spacing, kerning etc. of your font

 Structure of GT-Sample-Strings.txt: 
 
 0-1) basics to check proportions in UC and LC latin, spacing of glyphs/numerals/”special” characters
 
 2-3) latin spacing, lating kerning 
 
 4-5) cyrillic spacing, cyrillic kerning 
 
 6-7) greek spacing, greek kerning 
 
 8-x) additional things to check  (kerning exceptions, lc+UC kerning strings for Latin, language specific details, etc.)
 
 The GT-Sample-Strings.txt currently supports following Charactersets:
 
 - Latin Plus, by underware https://underware.nl/latin_plus/character_set/
 - Adobe Cyrillic 2 https://github.com/adobe-type-tools/adobe-cyrillic-charsets
 - Adobe Greek 1 https://github.com/adobe-type-tools/adobe-greek-charsets
 

## Setup and Usage of GT-Sample-Strings.txt in Glyphs App

 In Glyphs App: Preferences > Sample Strings > Open File > select GT-Sample-Strings.txt
 
 Switch to glyph-view and use cmd + alt + f to select sample text
 



