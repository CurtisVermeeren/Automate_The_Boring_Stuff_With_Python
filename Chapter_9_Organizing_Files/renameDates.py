#! python3
# Renames wiles with American MM-DD-YYYY date formate to European DD-MM-YYYY

import shutil, os, re

#Create a regex to match files with the American Date format.
datePattern = re.compile(r"""^(.*?))    # all text before the date
                        ((0|1)?d)-      # one or two digits for the month
                        ((0|1|2|3)?\d)- # one or two digits for the day
                        ((19|20)\d\d)   # four digits for the year
                        (.*?)$          # all text after the date
                        """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    #Skip files without a date.
    if mo == None:
        continue

    #Get the parts of the filename
    beforePart  = mo.group(1)
    monthPart   = mo.group(2)
    dayPart     = mo.group(4)
    yearPart    = mo.group(6)
    afterPart   = mo.group(8)

# Form the European filename
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# Get the full absolute file path.
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)

#Rename the files
print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
shutil.move(amerFilename, euroFilename)
