"""
Batch Vector File Conversion with Inkscape
Travis Burrows

This script batch converts all files of a specified extension (extIn) into another file format (extOut)
in the specified directory dirConvert.   This requires that inkscape is installed, and the path to the
executable is specified in inkscapePath.  All supported output formats have been tested but not all
input formats.  In addition, there are many more formats that are supported that are not currently
explicitly listed as supported.  This script has only been tested on Windows, but it should work on other
OSes, except for support for the wmf file extension.

To use, Change extIn to the format desired for input.  Change extOut to the desired format for output.
Change dirConvert to the directory of the files desired to convert.  Change inkscapePath to the path
of your inkscape executable. 
"""

from subprocess import run
from os.path import join
from os import walk

#   Input file extension
extIn = 'wmf'

#   Output file extension
extOut = 'svg'

#   File directory
dirConvert = r'C:\path\to\directory'

#   Inkscape executable path
inkscapePath = r'C:\Program Files\Inkscape\inkscape.exe'

#   Supported formats for input (not nearly exhaustive)
supportedIn = ['svg','wmf','emf','ps','pdf','eps']

#   Supported formats for output
supportedOut = ['svg','wmf','emf','ps','pdf','eps','png']

#   Test for valid extensions
if (extIn not in supportedIn):
    raise ValueError("Requested input extension is not supported.  It must be one of the following:\n%s" % supportedIn)
if (extOut not in supportedOut):
    raise ValueError("Requested output extension is not supported.  It must be one of the following:\n%s" % supportedOut)

if extOut == 'svg':
    extOutArgument = '--export-plain-svg='
else:
    extOutArgument = '--export-%s=' % extOut

#   Find files with specified extension
files=next(walk(dirConvert))[2]
toConvert = [];
for file in files:
    if file.endswith(extIn):
        toConvert.append(file)
        
#   Convert applicable files
lenExt = len(extIn)
lenF = len(toConvert)
for i, file in enumerate(toConvert):
    print('Converting %d/%d:\t%s' % (i+1,lenF,file))
    inPath = join(dirConvert,file)
    outPath = inPath[:-lenExt] + extOut
    commandString = '"' + inkscapePath +   '" --file="' + inPath + '" ' + extOutArgument + '"' + outPath + '"'
    run(commandString)
