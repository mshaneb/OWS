# getting b' ' strings in csv file, can't figure out why

import os
import sys
import csv
import os.path
import time
import datetime
from datetime import datetime


def main():
    temp = sys.stdout

    path_list = [os.path.normpath("S:")]

    write_mode = ["w+"]

    rfd = str(os.getcwd() + "/Reports/Program_Files/")
    reportdir = str(os.getcwd() + "/Reports/")

    def my_info(info):
        sys.stdout.close()
        sys.stdout = temp
        print(str(info))

    def file_dump_print(path_list):
        def write_path():
            print(os.path.join(root, file).encode("ascii", "ignore"))

        sys.stdout = open(rfd + "file dump.txt", w)
        for root, dirs, files in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    write_path()
                if file.endswith(".pptx"):
                    write_path()
                if file.endswith(".doc"):
                    write_path()
                if file.endswith(".docx"):
                    write_path()
                if file.endswith(".xlsx"):
                    write_path()

    def file_name_print(path_list):
        def write_name():
            print(str(os.path.splitext(file)[0].encode("ascii", "ignore")))

        sys.stdout = open(rfd + "file names.txt", w)
        for root, dirs, files in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    write_name()
                if file.endswith(".pptx"):
                    write_name()
                if file.endswith(".doc"):
                    write_name()
                if file.endswith(".docx"):
                    write_name()
                if file.endswith(".xlsx"):
                    write_name()

    def file_type_print(path_list):
        def write_type():
            print(os.path.splitext(file)[1])

        sys.stdout = open(rfd + "file type.txt", w)
        for root, dirs, files in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    write_type()
                if file.endswith(".pptx"):
                    write_type()
                if file.endswith(".doc"):
                    write_type()
                if file.endswith(".docx"):
                    write_type()
                if file.endswith(".xlsx"):
                    write_type()

    def file_rdcf_print(path_list):
        def write_rdcf():
            if "RDCF" in file:
                print("Yes")
            else:
                print("No")

        sys.stdout = open(rfd + "rdcf.txt", w)
        for root, dirs, files in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    write_rdcf()
                if file.endswith(".pptx"):
                    write_rdcf()
                if file.endswith(".doc"):
                    write_rdcf()
                if file.endswith(".docx"):
                    write_rdcf()
                if file.endswith(".xlsx"):
                    write_rdcf()

    def file_folder_print(path_list):
        def write_folder():
            print(os.path.join(root))

        sys.stdout = open(rfd + "folders.txt", w)
        for root, dirs, files in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    write_folder()
                if file.endswith(".pptx"):
                    write_folder()
                if file.endswith(".doc"):
                    write_folder()
                if file.endswith(".docx"):
                    write_folder()
                if file.endswith(".xlsx"):
                    write_folder()

    def file_policy(path_list):
        def write_policy():
            if "policy" in file:
                print("Yes")
            else:
                print("No")

        sys.stdout = open(rfd + "policy.txt", w)
        for root, dirs, files, in os.walk(a):
            for file in files:
                if file.endswith(".pdf"):
                    write_policy()
                if file.endswith(".pptx"):
                    write_policy()
                if file.endswith(".doc"):
                    write_policy()
                if file.endswith(".docx"):
                    write_policy()
                if file.endswith(".xlsx"):
                    write_policy()

    def file_date_created(path_list):
        def write_datecreated():
            filetimemod = datetime.fromtimestamp(
                os.path.getctime(os.path.join(root, file))
            )
            print(str(filetimemod)[:4])

        sys.stdout = open(rfd + "date created.txt", w)
        for root, dirs, files, in os.walk(a):
            for file in files:
                file_path = os.path.join(root, file)
                file_path.replace("\\\\", "/")  # tries to resolve "Error", doesn't work
                if os.path.exists(file_path):
                    if file.endswith(".pdf"):
                        write_datecreated()
                    if file.endswith(".pptx"):
                        write_datecreated()
                    if file.endswith(".doc"):
                        write_datecreated()
                    if file.endswith(".docx"):
                        write_datecreated()
                    if file.endswith(".xlsx"):
                        write_datecreated()
                else:
                    print("Error")

    def file_date_modified(path_list):
        def write_datemodified():
            if file.endswith(".pdf"):
                datemodified = datetime.fromtimestamp(
                    os.path.getmtime(os.path.join(root, file))
                )
                print(str(datemodified)[:4])
        sys.stdout = open(rfd + "date modified.txt", w)
        for root, dirs, files, in os.walk(a):
            for file in files:
                file_path = os.path.join(root, file)
                file_path.replace("\\\\", "/")
                if os.path.exists(file_path):
                    if file.endswith(".pdf"):
                        write_datemodified()
                    if file.endswith(".pptx"):
                        write_datemodified()
                    if file.endswith(".doc"):
                        write_datemodified()
                    if file.endswith(".docx"):
                        write_datemodified()
                    if file.endswith(".xlsx"):
                        write_datemodified()
                else:
                    print("Error")

    def run_report():
        file_dump_print(path_list)
        file_name_print(path_list)
        file_type_print(path_list)
        file_rdcf_print(path_list)
        file_folder_print(path_list)
        file_date_created(path_list)
        file_date_modified(path_list)
        file_policy(path_list)

    print("Running OWS ALL Report",
          "n/",
          os.getcwd()
          )

    for a, w in zip(path_list, write_mode):
        run_report()

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
    reportname = (reportdir + "OWS_All_Report_" + reporttimestamp + ".csv")

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
        sys.exit()


if __name__ == "__main__":
    main()
