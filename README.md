OWS File Index Utility

INTRODUCTION:
-------------

The OHRF File Index Utility was developed to allow for an efficient way to view, organize, and export an index of all files
on the OWS shared drive that are relevant to the Office of High-Risk Facilities, in order to aid the OWS/OCGR Communications 
Effort and facilitate identification of files with the potential to be hosted on the NIAID Intranet. It is designed to be an
easily-accessible .EXE program located on the OWS Shared Drive (S:\) and needing no special permissions to access or use. 
Using the already-generated metadata embedded in every file, it will export into a spreadsheet information such as the 
filename, dates created/modified, file type, folder, or if the document relates to the RDCF or OWS/OHRF policy.
The resulting spreadsheet is a normal Microsoft Excel file that can be modified, edited, and shared just as any other 
document.

"OHRF" currently searches the following directories (can be amended as needed):
	1. S:\\HIGH RISK FACILITIES\
	2. S:\\FACILITY PROJECTS\FACILITY OPERATIONS - 5601\RDCF\

"OWS ALL" currently searches the following directories:
    1. S:\\

"SRAMB" currently searches the following directories:
    1. S:\SRAMB

"OMA" currently searches the following directores:
    1. S:\Office of Management and Analytics (OMA)


INSTRUCTIONS:
-------------

	1. Click "OHRF Report" button on right side of program window underneath "OrChoose Report:"
	2. Wait as report runs - it takes several minutes for each report to run ("OWS ALL" takes several hours)
	4. Report will open automatically in Excel

Currently, the report generated will be presented in an unformatted manner so that technical writers can sort and filter as
they see fit. If desired, auto-formatting can be incorporated into a future update.

It is important to note that some columns/cells will appear to be BLANK upon initial opening of the document due to the way
Excel imports CSV files. In order to display all content with no additional formatting, highlight all cells, then click and 
un-click WRAP TEXT button.


KNOWN BUGS AND ISSUES:
----------------------

 * In some instances the "Date Created" and "Last Modified" fields are not able to be populated, and are
	set to return "Error"for those fields. Unsure why this is.


FUTURE IMPROVEMENTS:
--------------------

Please send suggestions and comments to Matthew Brown (brownms2@mail.nih.gov).

 * Custom, one-off report generation
 * Automatic highlighting/other demarcation of newly added files


VERSION HISTORY:
----------------

 * v1.0 - 4/15/19


MAINTAINER:
------------

	- Matthew Brown, NIAID/OWS -- brownms2@mail.nih.gov
