import xlwings as xw

wb = xw.Book(r"D:\OWS\Reports\OHRF_Report_Tue Jun 18 10_05_24 2019.csv")

wb.macro(r"PERSONAL!OHRF_Report")

print("done")
