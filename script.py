'''Automation Script  Absolute path - C://Home/Desktop/Demo
Relative path - ./Desktop/Demo '''
from sys import *
import os

def DirectoryWatcher(path):
    # isabs is used to check if path is absolute path
    #if it is not absolute path then convert it into absolute path
    flag = os.path.isabs(path)
    #here convert relative path to absolute path
    if flag==False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)
    if exists:
        for foldername,subfolder,filename in os.walk(path):
            print("Current folder is:",foldername)
            for subf in subfolder:
                print("Current folder:",foldername,"Current subfolder is:",subf)
            for filen in filename:
                print("File inside:",foldername,"File is:",filen)
            print(' ')
    else:
        print("Error:Invalid path")

def main():
    print("Application name:",argv[0])
    # Provide only one argument
    if(len(argv)!=2):
        print("Error:Invalid number of arguments")
        exit()
    # -h and -H are used in help message
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("The script is used to transverse a specific directory")
        exit()
    # it display following message for absolute path
    if (argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage: ApplicationName:Absolute path of the directory")
        exit()
    try:
        DirectoryWatcher(argv[1])
    except ValueError:
        print("Error:Invalid datatype of input")

    except Exception:
        print("Error:Invalid Input")

if __name__ == "__main__":
    main()








