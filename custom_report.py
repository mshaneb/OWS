## ! python3
##
## some dates are not able to be populated
## set up to return error for those values
## otherwise this seems good to go 4/16/19

import os, os.path
import sys
import csv
import os.path
import time
import datetime
from __init__ import *
from datetime import datetime


def main():
    temp = sys.stdout

    pathList = [os.path.normpath(str(path1.get())),
                os.path.normpath(str(path2.get())),
                os.path.normpath(str(path3.get())),
                os.path.normpath(str(path4.get())),
                os.path.normpath(str(path5.get())),
                os.path.normpath(str(path6.get()))
                ]

#this is going to have to be changed based on amount of file paths
    writeMode = ["w+",
                 "a",
                 "a",
                 "a",
                 "a",
                 "a"
                 ]

    rfd = str(os.getcwd() + "/Reports/Program_Files/")
    reportdir = str(os.getcwd() + "/Reports/")

    def my_info(info):
        sys.stdout.close()
        sys.stdout = temp
        print(str(info))

    def file_dump_print(pathList):
        sys.stdout = open(rfd + "file dump.txt", w)
        for root, dirs, files in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    print(os.path.join(root, file))
                if file.endswith(".pptx"):
                    print(os.path.join(root, file))
                if file.endswith(".doc"):
                    print(os.path.join(root, file))
                if file.endswith(".docx"):
                    print(os.path.join(root, file))
                if file.endswith(".xlsx"):
                    print(os.path.join(root, file))

    def file_name_print(pathList):
        sys.stdout = open(rfd + "file names.txt", w)
        for root, dirs, files in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    print(os.path.splitext(file)[0])
                if file.endswith(".pptx"):
                    print(os.path.splitext(file)[0])
                if file.endswith(".doc"):
                    print(os.path.splitext(file)[0])
                if file.endswith(".docx"):
                    print(os.path.splitext(file)[0])
                if file.endswith(".xlsx"):
                    print(os.path.splitext(file)[0])

    def file_type_print(pathList):
        sys.stdout = open(rfd + "file type.txt", w)
        for root, dirs, files in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    print(os.path.splitext(file)[1])
                if file.endswith(".pptx"):
                    print(os.path.splitext(file)[1])
                if file.endswith(".doc"):
                    print(os.path.splitext(file)[1])
                if file.endswith(".docx"):
                    print(os.path.splitext(file)[1])
                if file.endswith(".xlsx"):
                    print(os.path.splitext(file)[1])

    def file_rdcf_print(pathList):
        sys.stdout = open(rfd + "rdcf.txt", w)
        for root, dirs, files in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    if "RDCF" in file:
                        print("Yes")
                    else:
                        print("No")
                if file.endswith(".pptx"):
                    if "RDCF" in file:
                        print("Yes")
                    else:
                        print("No")
                if file.endswith(".doc"):
                    if "RDCF" in file:
                        print("Yes")
                    else:
                        print("No")
                if file.endswith(".docx"):
                    if "RDCF" in file:
                        print("Yes")
                    else:
                        print("No")
                if file.endswith(".xlsx"):
                    if "RDCF" in file:
                        print("Yes")
                    else:
                        print("No")

    def file_folder_print(pathList):
        sys.stdout = open(rfd + "folders.txt", w)
        for root, dirs, files in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    print(os.path.join(root))
                if file.endswith(".pptx"):
                    print(os.path.join(root))
                if file.endswith(".doc"):
                    print(os.path.join(root))
                if file.endswith(".docx"):
                    print(os.path.join(root))
                if file.endswith(".xlsx"):
                    print(os.path.join(root))

    def file_policy(pathList):
        sys.stdout = open(rfd + "policy.txt", w)
        for root, dirs, files, in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    if "policy" in file:
                        print("Yes")
                    else:
                        print("No")
                if file.endswith(".pptx"):
                    if "policy" in file:
                        print("Yes")
                    else:
                        print("No")
                if file.endswith(".doc"):
                    if "policy" in file:
                        print("Yes")
                    else:
                        print("No")
                if file.endswith(".docx"):
                    if "policy" in file:
                        print("Yes")
                    else:
                        print("No")
                if file.endswith(".xlsx"):
                    if "policy" in file:
                        print("Yes")
                    else:
                        print("No")

    def file_date_created(pathList):
        sys.stdout = open(rfd + "date created.txt", w)
        for root, dirs, files, in os.walk(a):
            for file in files:
                file_path = os.path.join(root, file)
                file_path.replace("\\\\", "/")  # tries to resolve "Error", doesn't work
                if os.path.exists(file_path):
                    if file.endswith(".pdf"):
                        filetimemod = datetime.fromtimestamp(
                            os.path.getctime(os.path.join(root, file))
                        )
                        print(str(filetimemod)[:4])
                    if file.endswith(".pptx"):
                        filetimemod = datetime.fromtimestamp(
                            os.path.getctime(os.path.join(root, file))
                        )
                        print(str(filetimemod)[:4])
                    if file.endswith(".doc"):
                        filetimemod = datetime.fromtimestamp(
                            os.path.getctime(os.path.join(root, file))
                        )
                        print(str(filetimemod)[:4])
                    if file.endswith(".docx"):
                        filetimemod = datetime.fromtimestamp(
                            os.path.getctime(os.path.join(root, file))
                        )
                        print(str(filetimemod)[:4])
                    if file.endswith(".xlsx"):
                        filetimemod = datetime.fromtimestamp(
                            os.path.getctime(os.path.join(root, file))
                        )
                        print(str(filetimemod)[:4])
                else:
                    print("Error")

    def file_date_modified(pathList):
        sys.stdout = open(rfd + "date modified.txt", w)
        for root, dirs, files, in os.walk(a):
            for file in files:
                file_path = os.path.join(root, file)
                file_path.replace("\\\\", "/")
                if os.path.exists(file_path):
                    if file.endswith(".pdf"):
                        datemodified = datetime.fromtimestamp(
                            os.path.getmtime(os.path.join(root, file))
                        )
                        print(str(datemodified)[:4])
                    if file.endswith(".pptx"):
                        datemodified = datetime.fromtimestamp(
                            os.path.getmtime(os.path.join(root, file))
                        )
                        print(str(datemodified)[:4])
                    if file.endswith(".doc"):
                        datemodified = datetime.fromtimestamp(
                            os.path.getmtime(os.path.join(root, file))
                        )
                        print(str(datemodified)[:4])
                    if file.endswith(".docx"):
                        datemodified = datetime.fromtimestamp(
                            os.path.getmtime(os.path.join(root, file))
                        )
                        print(str(datemodified)[:4])
                    if file.endswith(".xlsx"):
                        datemodified = datetime.fromtimestamp(
                            os.path.getmtime(os.path.join(root, file))
                        )
                        print(str(datemodified)[:4])
                else:
                    print("Error")

    def run_report():
        file_dump_print(pathList)
        file_name_print(pathList)
        file_type_print(pathList)
        file_rdcf_print(pathList)
        file_folder_print(pathList)
        file_date_created(pathList)
        file_date_modified(pathList)
        file_policy(pathList)

    print("Running Custom Report",
          "/n",
          pathList
          ##           "Path \"S:\\HIGH RISK FACILITIES\"",
          ##           "\n",
          ##           "Path \"S:\\FACILITY PROJECTS\FACILITY OPERATIONS - 5601\RDCF\"",
          ##           "\n"
          )

    for a, w in zip(pathList, writeMode):
        run_report()

    ##    my_info("Logged Files For Path " + a + "\n")
    # import files as list

    file_dump = open(rfd + "file dump.txt")
    listfiledump = file_dump.readlines()

    file_names = open(rfd + "file names.txt")
    listfilenames = file_names.readlines()

    file_type = open(rfd + "file type.txt")
    listfiletype = file_type.readlines()

    file_rdcf = open(rfd + "rdcf.txt")
    listrdcf = file_rdcf.readlines()

    file_folders = open(rfd + "folders.txt")
    listfolders = file_folders.readlines()

    file_date_created = open(rfd + "date created.txt")
    listdatecreated = file_date_created.readlines()

    file_date_modified = open(rfd + "date modified.txt")
    listdatemodified = file_date_modified.readlines()

    file_policy = open(rfd + "policy.txt")
    listpolicy = file_policy.readlines()

    textFileList = [rfd + "file dump.txt",
                    rfd + "file names.txt",
                    rfd + "file type.txt",
                    rfd + "rdcf.txt",
                    rfd + "folders.txt",
                    rfd + "date created.txt",
                    rfd + "date modified.txt",
                    rfd + "policy.txt"
                    ]

    print(listfilenames,
          listfiletype,
          listrdcf,
          listdatecreated,
          listdatemodified,
          listfolders,
          listfiledump,
          listpolicy
          )

    # writes lists to csv
    # and headers

    rows = zip(listfilenames,
               listfiletype,
               listrdcf,
               listdatecreated,
               listdatemodified,
               listfolders,
               listfiledump,
               listpolicy
               )

    headers = ["File",
               "Extension",
               "RDCF?",
               "Date Created",
               "Last Modified",
               "Folder",
               "Path/ Link",
               "Policy?"
               ]

    reporttimestamp = str(time.ctime(int(time.time()))).replace(":", "_")
    reportname = (reportdir + "Custom_Report_" + reporttimestamp + ".csv")
    #runmacrofile = str(rfd + "Master.xlsm")

    with open(reportname, "w+", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
    with open(reportname, "r", newline="") as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        lines[0] = headers
    with open(reportname, "w", newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

    if os.path.exists(reportname):
        os.startfile(reportname)
        # test of autorun macro below
        #os.startfile(runmacrofile)
        sys.exit()


if __name__ == "__main__":
    main()

