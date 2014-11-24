Minor Source is a group of python programs that download scans of eTextbooks from VitalSource, a popular eTextbook hosting site. These scripts are meant to facilitate learning and not piracy, and should only be used to read with leisure. 

Usage: vital.py [-h] [-p PASSWORD] [-e EMAIL] [-b BOOK] [-l LIMIT] [-r] [-a PATH] [-q PREFIX] [-w WAIT] [-s START]

Options for downloading scans

Arguments:<br>
  -h, --help            		Show this help message and exit <br>
  -p PASSWORD, --password PASSWORD	Login Password <br>
  -e EMAIL, --email EMAIL		Login Email <br>
  -b BOOK, --book BOOK  		Book value <br>
  -l LIMIT, --limit LIMIT		When to stop downloading pages <br>
  -r, --roman           		Use roman charecters instead of normal numbers <br>
  -a PATH, --path PATH  		Path to save files to <br>
  -q PREFIX, --prefix PREFIX		Prefix to add to pages (Example: A1, A2, ... ) <br>
  -w WAIT, --wait WAIT  		Time to wait in between pages. Default: 250 (in milliseconds) <br>
  -s START, --start START		Page to start at. Default: 1 <br>

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
