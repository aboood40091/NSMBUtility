#! python3.5.1

import os
import urllib.request
import requests
import sys
import webbrowser
import easygui
import shutil
import zipfile
from subprocess import Popen

print("  ")
print("  ")
print("  ")
print("Welcome to NSMBUtility!")
print("  ")
print("  ")

def main_menu():
    while True:
        print("1    Create environment (some features won't work if you don't do this first!)")
        print("2    Create folder structure for Cafiine, to be able to load custom levels")
        print("3    Download the latest Reggie Next! with NSMBU support")
        print("4    Download the latest Spritedata")
        print("5    Convert .sarc into .szs (the file type your level has to be, when you want to load it with Cafiine)")
        print("6    Go to the NSMBU Hacking tutorials and information")
        print("7    Exit")
        print("  ")
        print("  ")
        
        task = input("What would you like to do? Enter a number        ")
        
        if task == "1" or task == "one" or task == "One" or task == "ONE":
        
            def create_environment():
                while True:
                    print("  ")
                    print("Environment will be created in the C:\ folder")
                    print("You might be able to change this directory in future releases")
                    print("  ")
            
                    createenvironment = input("Do you want to proceed? Enter y / n      ")
            
                    if createenvironment == "y" or createenvironment == "Y":
                        print("OK!")
                        print("  ")
                        print("Creating environment...")
                
                        main_path = "C:\Wii U"
                        reggie_path = "C:\Wii U\Reggie Next!"
                        newcafiine_path = "C:\Wii U\Cafiine"
                        compressed_level_path = "C:\Wii U\Compressed Levels"
                        
                        os.makedirs(main_path, exist_ok = True)
                        os.makedirs(reggie_path, exist_ok = True)
                        os.makedirs(newcafiine_path, exist_ok = True)
                        os.makedirs(compressed_level_path, exist_ok = True)
                
                        print("Done! Environment succesfully created")
                        print("  ")
                        
                        anykey = input("Enter any key to continue       ")
                        
                        if anykey == "crash" or anykey == "CRASH":
                            print("  ")
                            print("Gotcha, hacker!")
                            print("  ")
                            print("  ")
                            sys.exit("Goodbye!")
                            break
                            
                        else:
                            print("  ")
                            print("  ")
                            print("  ")
                            print("Would you like to do anything else?")
                            print("  ")
                            print("  ")
                            break
                
                    elif createenvironment == "n" or createenvironment == "N":
                        print("OK!")
                        print("  ")
                        print("  ")
                        print("  ")
                        print("Would you like to do anything else?")
                        print("  ")
                        print("  ")
                        break
                            
                    else:
                        print("  ")
                        print("Please answer the question with y / n !")
                        print("  ")
                        print("  ")
                    
            create_environment()
        
        elif task == "2" or task == "two" or task == "Two" or task == "TWO":
            
            def cafiine_environment():
                while True:
                    print("  ")
                    print("  ")
                    print("Let's go")
                    print("  ")
                    
                    #cafiine_path = easygui.diropenbox()
                    cafiine_path = "C:\Wii U\Cafiine"
                    
                    print("The structure will be created in this folder: %s " % (cafiine_path)) 
                    print("You can always copy the files to another folder whenever you want. Proceed?")
                    print(" ")
                    
                    cafiine_proceed = input("Enter y / n        ")
                    
                    if cafiine_proceed == "y" or cafiine_proceed == "Y":
                        print("OK!")
                        print("  ")
                        print("  ")
                        
                        print("1    New Super Mario Bros. U")
                        print("2    New Super Luigi U")
                        print("3    New Super Mario Bros. U + New Super Luigi U (use this if you have the 2 on 1 disc)")
                        print("  ")
                        
                        game = input("Choose the game the structure is for        ")
                        print("OK, Roger that!")
                        
                        if game == "1" or game == "one" or game == "One" or game == "ONE":
                            print("  ")
                            print("  ")
                            print("1    USA version")
                            print("2    EUR version")
                            print("3    JAP version")
                            print("  ")
                        
                            nsmbu_version = input("Now, what version of the NSMBU Disc do you have? Enter the number        ")
                            
                            if nsmbu_version == "1" or nsmbu_version == "one" or nsmbu_version == "One" or nsmbu_version == "ONE":
                                print("Perfect!")
                                print("  ")
                                print("  ")
                                print("Creating structure...")
                        
                                #cafiine_path1 = cafiine_path + "cafiine_root\00050000-10101D00\vol\content\Common\course_res_pack"
                                cafiine_path01 = cafiine_path + "\\cafiine_root"
                                cafiine_path02 = cafiine_path01 + "\\00050000-10101D00"
                                cafiine_path03 = cafiine_path02 + "\\vol"
                                cafiine_path04 = cafiine_path03 + "\\content"
                                cafiine_path05 = cafiine_path04 + "\\Common"
                                cafiine_path06 = cafiine_path05 + "\\course_res_pack"
                            
                                os.makedirs(cafiine_path01, exist_ok = True)
                                os.makedirs(cafiine_path02, exist_ok = True)
                                os.makedirs(cafiine_path03, exist_ok = True)
                                os.makedirs(cafiine_path04, exist_ok = True)
                                os.makedirs(cafiine_path05, exist_ok = True)
                                os.makedirs(cafiine_path06, exist_ok = True)
                            
                                print("Done! Structure succesfully created!")
                                print("  ")
                            
                                anykey2 = input("Enter any key to continue        ")
                        
                                if anykey2 == "crash" or anykey2 == "CRASH":
                                    print("  ")
                                    print("Gotcha, hacker!")
                                    print("  ")
                                    print("  ")
                                    sys.exit("Goodbye!")
                            
                                else:
                                    print("  ")
                                    print("  ")
                                    print("  ")
                                    print("Would you like to do anything else?")
                                    print("  ")
                                    print("  ")
                                    break
                            
                            elif nsmbu_version == "2" or nsmbu_version == "two" or nsmbu_version == "Two" or nsmbu_version == "TWO":
                                print("Perfect!")
                                print("  ")
                                print("  ")
                                print("Creating structure...")
                        
                                #cafiine_path1 = cafiine_path + "cafiine_root\00050000-10101E00\vol\content\Common\course_res_pack"
                                cafiine_path01 = cafiine_path + "\\cafiine_root"
                                cafiine_path02 = cafiine_path01 + "\\00050000-10101E00"
                                cafiine_path03 = cafiine_path02 + "\\vol"
                                cafiine_path04 = cafiine_path03 + "\\content"
                                cafiine_path05 = cafiine_path04 + "\\Common"
                                cafiine_path06 = cafiine_path05 + "\\course_res_pack"
                        
                                os.makedirs(cafiine_path01, exist_ok = True)
                                os.makedirs(cafiine_path02, exist_ok = True)
                                os.makedirs(cafiine_path03, exist_ok = True)
                                os.makedirs(cafiine_path04, exist_ok = True)
                                os.makedirs(cafiine_path05, exist_ok = True)
                                os.makedirs(cafiine_path06, exist_ok = True)
                            
                                print("Done! Structure succesfully created!")
                                print("  ")
                            
                                anykey2 = input("Enter any key to continue        ")
                            
                                if anykey2 == "crash" or anykey2 == "CRASH":
                                    print("  ")
                                    print("Gotcha, hacker!")
                                    print("  ")
                                    print("  ")
                                    sys.exit("Goodbye!")
                            
                                else:
                                    print("  ")
                                    print("  ")
                                    print("  ")
                                    print("Would you like to do anything else?")
                                    print("  ")
                                    print("  ")
                                    break
                            
                            elif nsmbu_version == "3" or nsmbu_version == "three" or nsmbu_version == "Three" or nsmbu_version == "THREE":
                                print("Perfect!")
                                print("  ")
                                print("  ")
                                print("Creating structure...")
                        
                                #cafiine_path1 = cafiine_path + "cafiine_root\00050000-10101C00\vol\content\Common\course_res_pack"
                                cafiine_path01 = cafiine_path + "\\cafiine_root"
                                cafiine_path02 = cafiine_path01 + "\\00050000-10101C00"
                                cafiine_path03 = cafiine_path02 + "\\vol"
                                cafiine_path04 = cafiine_path03 + "\\content"
                                cafiine_path05 = cafiine_path04 + "\\Common"
                                cafiine_path06 = cafiine_path05 + "\\course_res_pack"
                        
                                os.makedirs(cafiine_path01, exist_ok = True)
                                os.makedirs(cafiine_path02, exist_ok = True)
                                os.makedirs(cafiine_path03, exist_ok = True)
                                os.makedirs(cafiine_path04, exist_ok = True)
                                os.makedirs(cafiine_path05, exist_ok = True)
                                os.makedirs(cafiine_path06, exist_ok = True)
                            
                                print("Done! Structure succesfully created!")
                                print("  ")
                            
                                anykey2 = input("Enter any key to continue        ")
                        
                                if anykey2 == "crash" or anykey2 == "CRASH":
                                    print("  ")
                                    print("Gotcha, hacker!")
                                    print("  ")
                                    print("  ")
                                    sys.exit("Goodbye!")
                            
                                else:
                                    print("  ")
                                    print("  ")
                                    print("  ")
                                    print("Would you like to do anything else?")
                                    print("  ")
                                    print("  ")
                                    break
                            
                            else:
                                print("  ")
                                print("  ")
                                print("That's  not a valid number")
                                print("Restarting process...")
                                
                        elif game == "2" or game == "two" or game == "Two" or game == "TWO":
                            
                            print("  ")
                            print("  ")
                            print("1    USA version")
                            print("2    EUR version")
                            print("3    JAP version")
                            print("  ")
                        
                            nslu_version = input("Now, what version of the NSLU Disc do you have? Enter the number        ")
                            
                            if nslu_version == "1" or nslu_version == "one" or nslu_version == "One" or nslu_version == "ONE":
                                print("Perfect!")
                                print("  ")
                                print("  ")
                                print("Creating structure...")
                        
                                #cafiine_path1 = cafiine_path + "cafiine_root\00050000-10142300\vol\content\Common\course_res_pack"
                                cafiine_path01 = cafiine_path + "\\cafiine_root"
                                cafiine_path02 = cafiine_path01 + "\\00050000-10142300"
                                cafiine_path03 = cafiine_path02 + "\\vol"
                                cafiine_path04 = cafiine_path03 + "\\content"
                                cafiine_path05 = cafiine_path04 + "\\Common"
                                cafiine_path06 = cafiine_path05 + "\\course_res_pack"
                            
                                os.makedirs(cafiine_path01, exist_ok = True)
                                os.makedirs(cafiine_path02, exist_ok = True)
                                os.makedirs(cafiine_path03, exist_ok = True)
                                os.makedirs(cafiine_path04, exist_ok = True)
                                os.makedirs(cafiine_path05, exist_ok = True)
                                os.makedirs(cafiine_path06, exist_ok = True)
                            
                                print("Done! Structure succesfully created!")
                                print("  ")
                            
                                anykey2 = input("Enter any key to continue        ")
                        
                                if anykey2 == "crash" or anykey2 == "CRASH":
                                    print("  ")
                                    print("Gotcha, hacker!")
                                    print("  ")
                                    print("  ")
                                    sys.exit("Goodbye!")
                            
                                else:
                                    print("  ")
                                    print("  ")
                                    print("  ")
                                    print("Would you like to do anything else?")
                                    print("  ")
                                    print("  ")
                                    break
                            
                            elif nslu_version == "2" or nslu_version == "two" or nslu_version == "Two" or nslu_version == "TWO":
                                print("Perfect!")
                                print("  ")
                                print("  ")
                                print("Creating structure...")
                        
                                #cafiine_path1 = cafiine_path + "cafiine_root\00050000-10142400\vol\content\Common\course_res_pack"
                                cafiine_path01 = cafiine_path + "\\cafiine_root"
                                cafiine_path02 = cafiine_path01 + "\\00050000-10142400"
                                cafiine_path03 = cafiine_path02 + "\\vol"
                                cafiine_path04 = cafiine_path03 + "\\content"
                                cafiine_path05 = cafiine_path04 + "\\Common"
                                cafiine_path06 = cafiine_path05 + "\\course_res_pack"
                            
                                os.makedirs(cafiine_path01, exist_ok = True)
                                os.makedirs(cafiine_path02, exist_ok = True)
                                os.makedirs(cafiine_path03, exist_ok = True)
                                os.makedirs(cafiine_path04, exist_ok = True)
                                os.makedirs(cafiine_path05, exist_ok = True)
                                os.makedirs(cafiine_path06, exist_ok = True)
                            
                                print("Done! Structure succesfully created!")
                                print("  ")
                                
                                anykey2 = input("Enter any key to continue        ")
                            
                                if anykey2 == "crash" or anykey2 == "CRASH":
                                    print("  ")
                                    print("Gotcha, hacker!")
                                    print("  ")
                                    print("  ")
                                    sys.exit("Goodbye!")
                            
                                else:
                                    print("  ")
                                    print("  ")
                                    print("  ")
                                    print("Would you like to do anything else?")
                                    print("  ")
                                    print("  ")
                                    break
                            
                            elif nslu_version == "3" or nslu_version == "three" or nslu_version == "Three" or nslu_version == "THREE":
                                print("Perfect!")
                                print("  ")
                                print("  ")
                                print("Creating structure...")
                        
                                #cafiine_path1 = cafiine_path + "cafiine_root\00050000-10142200\vol\content\Common\course_res_pack"
                                cafiine_path01 = cafiine_path + "\\cafiine_root"
                                cafiine_path02 = cafiine_path01 + "\\00050000-10142200"
                                cafiine_path03 = cafiine_path02 + "\\vol"
                                cafiine_path04 = cafiine_path03 + "\\content"
                                cafiine_path05 = cafiine_path04 + "\\Common"
                                cafiine_path06 = cafiine_path05 + "\\course_res_pack"
                        
                                os.makedirs(cafiine_path01, exist_ok = True)
                                os.makedirs(cafiine_path02, exist_ok = True)
                                os.makedirs(cafiine_path03, exist_ok = True)
                                os.makedirs(cafiine_path04, exist_ok = True)
                                os.makedirs(cafiine_path05, exist_ok = True)
                                os.makedirs(cafiine_path06, exist_ok = True)
                            
                                print("Done! Structure succesfully created!")
                                print("  ")
                            
                                anykey2 = input("Enter any key to continue        ")
                        
                                if anykey2 == "crash" or anykey2 == "CRASH":
                                    print("  ")
                                    print("Gotcha, hacker!")
                                    print("  ")
                                    print("  ")
                                    sys.exit("Goodbye!")
                            
                                else:
                                    print("  ")
                                    print("  ")
                                    print("  ")
                                    print("Would you like to do anything else?")
                                    print("  ")
                                    print("  ")
                                    break
                                    
                            else:
                                print("  ")
                                print("  ")
                                print("That's  not a valid number")
                                print("Restarting process...")
                                    
                        elif game == "3" or game == "three" or game == "Three" or game == "THREE":
                            print("  ")
                            print("  ")
                            print("1    USA version")
                            print("2    EUR version")
                            print("  ")
                        
                            nsmbu_nslu_version = input("Now, what version of the NSMBU + NSLU Disc do you have? Enter the number        ")
                            
                            if nsmbu_nslu_version == "1" or nsmbu_nslu_version == "one" or nsmbu_nslu_version == "One" or nsmbu_nslu_version == "ONE":
                                print("Perfect!")
                                print("  ")
                                print("  ")
                                print("Creating structure...")
                        
                                #cafiine_path1 = cafiine_path + "cafiine_root\00050000-1014B700\vol\content\Common\course_res_pack"
                                cafiine_path01 = cafiine_path + "\\cafiine_root"
                                cafiine_path02 = cafiine_path01 + "\\00050000-1014B700"
                                cafiine_path03 = cafiine_path02 + "\\vol"
                                cafiine_path04 = cafiine_path03 + "\\content"
                                cafiine_path05 = cafiine_path04 + "\\Common"
                                cafiine_path06 = cafiine_path05 + "\\course_res_pack"
                            
                                os.makedirs(cafiine_path01, exist_ok = True)
                                os.makedirs(cafiine_path02, exist_ok = True)
                                os.makedirs(cafiine_path03, exist_ok = True)
                                os.makedirs(cafiine_path04, exist_ok = True)
                                os.makedirs(cafiine_path05, exist_ok = True)
                                os.makedirs(cafiine_path06, exist_ok = True)
                            
                                print("Done! Structure succesfully created!")
                                print("  ")
                            
                                anykey2 = input("Enter any key to continue        ")
                        
                                if anykey2 == "crash" or anykey2 == "CRASH":
                                    print("  ")
                                    print("Gotcha, hacker!")
                                    print("  ")
                                    print("  ")
                                    sys.exit("Goodbye!")
                            
                                else:
                                    print("  ")
                                    print("  ")
                                    print("  ")
                                    print("Would you like to do anything else?")
                                    print("  ")
                                    print("  ")
                                    break
                            
                            elif nsmbu_nslu_version == "2" or nsmbu_nslu_version == "two" or nsmbu_nslu_version == "Two" or nsmbu_nslu_version == "TWO":
                                print("Perfect!")
                                print("  ")
                                print("  ")
                                print("Creating structure...")
                        
                                #cafiine_path1 = cafiine_path + "cafiine_root\00050000-1014B800\vol\content\Common\course_res_pack"
                                cafiine_path01 = cafiine_path + "\\cafiine_root"
                                cafiine_path02 = cafiine_path01 + "\\00050000-1014B800"
                                cafiine_path03 = cafiine_path02 + "\\vol"
                                cafiine_path04 = cafiine_path03 + "\\content"
                                cafiine_path05 = cafiine_path04 + "\\Common"
                                cafiine_path06 = cafiine_path05 + "\\course_res_pack"
                            
                                os.makedirs(cafiine_path01, exist_ok = True)
                                os.makedirs(cafiine_path02, exist_ok = True)
                                os.makedirs(cafiine_path03, exist_ok = True)
                                os.makedirs(cafiine_path04, exist_ok = True)
                                os.makedirs(cafiine_path05, exist_ok = True)
                                os.makedirs(cafiine_path06, exist_ok = True)
                            
                                print("Done! Structure succesfully created!")
                                print("  ")
                                
                                anykey2 = input("Enter any key to continue        ")
                            
                                if anykey2 == "crash" or anykey2 == "CRASH":
                                    print("  ")
                                    print("Gotcha, hacker!")
                                    print("  ")
                                    print("  ")
                                    sys.exit("Goodbye!")
                            
                                else:
                                    print("  ")
                                    print("  ")
                                    print("  ")
                                    print("Would you like to do anything else?")
                                    print("  ")
                                    print("  ")
                                    break
                                    
                            else:
                                print("  ")
                                print("  ")
                                print("That's  not a valid number")
                                print("Restarting process...")
                                    
                        else:
                            print("  ")
                            print("  ")
                            print("Hmmm, that seems not to be a valid number")
                            print("Restarting process...")

                    elif cafiine_proceed == "n" or cafiine_proceed == "N":
                        print("  ")
                        print("Cancelling...")
                        print("Generating data structure succesfully cancelled!")
                        print("  ")
                        
                        anykey2 = input("Enter any key to continue        ")
                        
                        if anykey2 == "crash" or anykey2 == "CRASH":
                            print("  ")
                            print("Gotcha, hacker!")
                            print("  ")
                            print("  ")
                            sys.exit("Goodbye!")
                            
                        else:
                            print("  ")
                            print("  ")
                            print("  ")
                            print("Would you like to do anything else?")
                            print("  ")
                            print("  ")
                            break
                    
                    else:
                        print("  ")
                        print("Please answer with y / n !")
                        print("  ")
                    
            cafiine_environment()
        
        elif task == "3" or task == "three" or task == "Three" or task == "THREE":
            
            def download_reggie():
                while True:
                    print("  ")
                    print("  ")
                    print("Do you want to download the latest Reggie Next! with NSMBU support?")
                    
                    reggie_proceed = input("Enter y / n        ")
                    
                    if reggie_proceed == "y" or reggie_proceed == "Y":
                        print("   ")
                        print("   ")
                        print("Connecting to the download page...")
                        
                        response = requests.get('https://github.com/MrRean/ReggieNext-NSMBU/releases/latest')
                        
                        if (int(response.status_code)) == 200:
                            print("Connected to the download page!")
    
                        else:
                            print("   ")
                            print("Can't connect to download page! Doing another test...")
        
                            response = requests.get('https://google.com')
                            if (int(response.status_code)) == 200:
                                print("   ")
                                print("It seems that the download page is down. Try restarting NSMBUtility and check if '3' still doesn't work.")
        
                            else:
                                print("   ")
                                print("It looks like you don't have a working internet connection. Connect to another network, or solve the connectionproblem.")
                                
                                
                        print("   ")
                        print("Downloading...")
                        urllib.request.urlretrieve("https://github.com/MrRean/ReggieNext-NSMBU/releases/download/v5.0/reggieversion5point0.zip", "Reggie_Next!_NSMBU_V5.0.zip")
                        print("Download completed!")
                        print("  ")
                        
                        if os.path.exists("C:\Wii U\Reggie Next!\Reggie_Next!_NSMBU_V5.0.zip"):
                            os.remove("C:\\Wii U\\Reggie Next!\\Reggie_Next!_NSMBU_V5.0.zip")
                        
                        print("Moving file to C:\Wii U\Reggie_Next ...")
                        
                        source = "C:\\Wii U\\\Reggie_Next!_NSMBU_V5.0.zip"
                        destination = "C:\\Wii U\\Reggie Next!"
                        
                        shutil.move(source, destination)
                        
                        print("Completed!")
                        print("  ")
                        print("Removing old versions...")
                        
                        if os.path.exists("C:\Wii U\Reggie Next!\dist"):
                            shutil.rmtree("C:\Wii U\Reggie Next!\dist")
                        
                        print("Old versions succesfully removed!")
                        print("  ")
                        print("Unzipping...")
                        
                        #zipfile.extract("Reggie_Next!_NSMBU_V5.0.zip", path = "C:\Wii U\Reggie Next!", pwd=None)
                        
                        zip = zipfile.ZipFile(r'c:\Wii U\Reggie Next!\Reggie_Next!_NSMBU_V5.0.zip')  
                        zip.extractall(r'C:\Wii U\Reggie Next!')
                        
                        print("File succesfully unzipped!")
                        print("  ")
                        #print("You now can delete Reggie_Next!_NSMBU_V5.0.zip, stored in c:\Wii U\Reggie Next!")
                        print("Removing old copy...")
                        
                        zip.close()
                        os.remove("C:\\Wii U\\Reggie Next!\\Reggie_Next!_NSMBU_V5.0.zip")
                        
                        print("Old copy succesfully removed!")
                        print("  ")
                        print("  ")
                        
                        anykey7 = input("Enter any key to continue        ")
                            
                        if anykey7 == "crash" or anykey7 == "CRASH":
                            print("  ")
                            print("Gotcha, hacker!")
                            print("  ")
                            print("  ")
                            sys.exit("Goodbye!")
                            
                        else:
                            print("  ")
                            print("  ")
                            print("  ")
                            print("Would you like to do anything else?")
                            print("  ")
                            print("  ")
                            break
                            
                    elif reggie_proceed == "n" or reggie_proceed == "N":
                            print("  ")
                            print("  ")
                            print("  ")
                            
                            anykey3 = input("Enter any key to continue        ")
                            
                            if anykey3 == "crash" or anykey3 == "CRASH":
                                print("  ")
                                print("Gotcha, hacker!")
                                print("  ")
                                print("  ")
                                sys.exit("Goodbye!")
                            
                            else:
                                print("  ")
                                print("  ")
                                print("  ")
                                print("Would you like to do anything else?")
                                print("  ")
                                print("  ")
                                break
                            
                    else:
                        print("  ")
                        print("Please answer with y / n")
                        print("  ")
                        
            download_reggie()
        
        elif task == "4" or task == "four" or task == "Four" or task == "FOUR":
            print("   ")
            print("   ")
            print("Connecting to download page...")
    
            response = requests.get('https://github.com/MrRean/ReggieNext-NSMBU/releases/latest')
            if (int(response.status_code)) == 200:
                print("Connected to download page!")
    
            else:
                print("   ")
                print("Can't connect to download page! Doing another test...")
        
                response = requests.get('https://google.com')
                if (int(response.status_code)) == 200:
                    print("   ")
                    print("It seems that the download page is down. Try restarting NSMBUtility and check if '2' still doesn't work.")
                    
                else:
                    print("   ")
                    print("It looks like you don't have a working internet connection. Connect to another network, or solve the connectionproblem.")
    
            print("   ")
            print("Downloading...")
    
            symbol = "SpriteDB"
            url = 'http://rhcafe.us.to/spritexml.php'.format(symbol)
            data = requests.get(url)

            with open("spritedata.xml".format(symbol), "w") as out_f:
                out_f.write(data.text)
    
            print("Download completed!")
            print("  ")
            print("Removing old copy...")
            
            os.remove('C:\\Wii U\\Reggie Next!\\dist\\reggiedata\\spritedata.xml')
           
            print("Old copy removed!")
            print("  ")
            print("Moving file to proper directory...")
            
            os.rename("C:\\Wii U\\spritedata.xml", "C:\\Wii U\Reggie Next!\\dist\\reggiedata\\spritedata.xml")
            
            print("Completed! Now, you can use the latest spritedata!")
            print("  ")
            print("  ")
            
            anykey4 = input("Enter any key to continue        ")
                            
            if anykey4 == "crash" or anykey4 == "CRASH":
                print("  ")
                print("Gotcha, hacker!")
                print("  ")
                print("  ")
                sys.exit("Goodbye!")
                            
            else:
                print("  ")
                print("  ")
                print("  ")
                print("Would you like to do anything else?")
                print("  ")
                print("  ")
        
        elif task == "5" or task == "five" or task == "Five" or task == "FIVE":
            
            def converter():
                while True:
                    print("  ")
                    print("  ")
                    print("OK! Let's go!")
                    
                    SZS_Tools = input("Do you already have the program 'Wiimms SZS Tool'? Enter y / n      ")
            
                    if SZS_Tools == "y" or SZS_Tools == "Y":
                        print("  ")
                        print("  ")
                        print("OK! Good")
                        print("  ")
                        print("Install the program, if you haven't already")
                        print("Install sendto-install.bat too!")
                        print("Restart your PC, after installing both programs")
                        print("  ")
                        
                        opened_sendto = input("Did you succesfully install both programs? Enter y / n       ")
                        
                        if opened_sendto == "y" or opened_sendto == "Y":
                            print("   ")
                            print("Good!")
                            print("  ")
                            print("  ")
                            print("Now, select the 'Wiimms SZS Tool' folder")
                        
                            SZS_path = easygui.diropenbox()
                            print("Cool!")
                            print("  ")
                            print("  ")
                            print("Now, select your level.sarc")
                    
                            path = easygui.fileopenbox()
                
                            print("Great!")
                            print("  ")
                            
                            levelname = input("Now, what is the level you'd like to replace? (Don't add .szs, ex. :  1-1)      ")
                            completelevelname = levelname + ".szs"
                            
                            print("  ")
                            print("  ")
                            print("Generating file...")
                                
                
                            f = open('comp.bat','w')
                
                            line = 'wszst compress %s --dest %s' % (path, completelevelname)
                            f.write(line)
                        
                            SZS_path1 = SZS_path + "\\comp.bat"
                            
                            f.close()
                            
                            if os.path.exists("%s" %(SZS_path1)):
                                os.remove("%s" %(SZS_path1))
                            
                            os.rename("C:\\Wii U\\comp.bat", "%s" %(SZS_path1))

                            print("File succesfully generated!")
                            print("  ")
                            print("  ")
                            
                            print("Compressing...")
                            print("  ")
                            print("  ")
                            
                            os.system("%s" % (SZS_path1))
                            
                            print("  ")
                            print("  ")
                            print("Done! Moving file to 'Compressed Levels'... ")
                            
                            levelname2 = levelname + ".szs"
                            
                            shutil.move("C:\Wii U\%s" % (levelname2), "C:\Wii U\Compressed Levels")
                            
                            print("Level succesfully moved to 'C:\Wii U\Compressed Levels'!")
                            print("  ")
                            print("  ")
                            
                            anykey5 = input("Enter any key to continue        ")
                            
                            if anykey5 == "crash" or anykey5 == "CRASH":
                                print("  ")
                                print("Gotcha, hacker!")
                                print("  ")
                                print("  ")
                                sys.exit("Goodbye!")
                            
                            else:
                                print("  ")
                                print("  ")
                                print("  ")
                                print("Would you like to do anything else?")
                                print("  ")
                                print("  ")
                                break
                                
                        else:
                            print("  ")
                            print("  ")
                            print("Install both programs and restart your PC afterwards")
                            print("  ")
                            print("  ")
                            print("  ")
                            print("Would you like to do anything else?")
                            print("  ")
                            print("  ")
                            break
                    
                    elif SZS_Tools == "n" or  SZS_Tools == "N":
                        print("  ")
                        print("  ")
                        print("Than download it from the page that has opened in your webbrowser.")
                        print("Be sure to download and install the right version!")
                        print("  ")
                        print("  ")
                        
                        szs_url = "http://szs.wiimm.de/download.html"
                        webbrowser.open(szs_url, new = 0, autoraise = True)
                
                        exitnow = input("Enter a key to return to the menu        ")
                        if exitnow == "crash" or exitnow == "CRASH":
                        
                            print("  ")
                            print("Gotcha, hacker!")
                            print(" ")
                            print(" ")
                            sys.exit("Goodbye!")
                            
                        else:
                            print("  ")
                            print("  ")
                            print("  ")
                            print("Would you like to do anything else?")
                            print("  ")
                            print("  ")
                            break
                            
                    else:
                        print("  ")
                        print("  ")
                        print("Please answer the question next time with y / n")
                 
            converter()
        
        elif task == "6" or task == "six" or task == "Six" or task == "SIX":
            print("  ")
            print("  ")
            print("Opening webbrowser...")
            
            url_help = "http://rhcafe.us.to/?page=f&id=9"
            webbrowser.open(url_help, new = 0, autoraise = True)
            
            print("Hopefully you've found what you were looking for!")
            print("  ")
            print("  ")
            
            exitnow6 = input("Enter a key to return to the menu        ")
            if exitnow6 == "crash" or exitnow6 == "CRASH":
                        
                print("  ")
                print("Gotcha, hacker!")
                print(" ")
                print(" ")
                sys.exit("Goodbye!")
                            
            else:
                print("  ")
                print("  ")
                print("  ")
                print("Would you like to do anything else?")
                print("  ")
            
        elif task == "7" or task == "seven" or task == "Seven" or task == "SEVEN":
            print("  ")
            print("  ")
            sys.exit("See you next time!")
                
                



main_menu()