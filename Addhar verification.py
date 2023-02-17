print("\t \t \t============================================================================")
print("\t \t \t% If you want to give the ADDHAR NUMBER of student then press Y/y          %")    #ADDHAR NUMBER
print("\t \t \t% If you did not want to give the ADDHAR NUMBER of student then press N/n  %")
print("\t \t \t============================================================================")
ao=input("Enter your choice = ")
while(ao.isalpha()==True):
    if(ao=="Y" or ao=="y"):
        an=input("Enter your addhar number = ")
        if(an.isdigit()==True):
            if(len(an)==16):
                break
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given less or higher digit then 16 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                pass
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used alphabets or sing in Addhar Number which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            pass
    elif(ao=="N" or ao=="n"):
        break
    else:
        print("\t \t \t============================================================================")
        print("\t \t \t% If you want to give the ADDHAR NUMBER of student then press Y/y          %")
        print("\t \t \t% If you did not want to give the ADDHAR NUMBER of student then press N/n  %")
        print("\t \t \t============================================================================")
        ao=input("Enter your choice = ")
        if(ao.isalpha()==True):
            if(ao=="Y" or ao=="y"):
                an=input("Enter your addhar number = ")
                if(an.isdigit()==True):
                    if(len(an)==16):
                        break
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given less or higher digit then 16 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                        pass
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used alphabets or sing in Addhar Number which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    pass
            if(ao=="N" or ao=="n"):
                break
while(ao.isalpha()!=True):
    print("\t \t \t============================================================================")
    print("\t \t \t% If you want to give the ADDHAR NUMBER of student then press Y/y          %")
    print("\t \t \t% If you did not want to give the ADDHAR NUMBER of student then press N/n  %")
    print("\t \t \t============================================================================")
    ao=input("Enter your choice = ")
    pass
    if(ao=="Y" or ao=="y"):
        an=input("Enter your addhar number = ")
        if(an.isdigit()==True):
            if(len(an)==16):
                break
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given less or higher digit then 16 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                pass
        else:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used alphabets or sing in Addhar Number which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
            pass
    elif(ao=="N" or ao=="n"):
        break
    else:
        print("\t \t \t============================================================================")
        print("\t \t \t% If you want to give the ADDHAR NUMBER of student then press Y/y          %")
        print("\t \t \t% If you did not want to give the ADDHAR NUMBER of student then press N/n  %")
        print("\t \t \t============================================================================")
        ao=input("Enter your choice = ")
        if(ao.isalpha()==True):
            if(ao=="Y" or ao=="y"):
                an=input("Enter your addhar number = ")
                if(an.isdigit()==True):
                    if(len(an)==16):                            
                       break
                    else:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You given less or higher digit then 16 which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                        pass
                else:
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^YOU GIVEN THE WRONG INPUT ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^You used alphabets or sing in Addhar Number which is invalid^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    print("---------------------------------------------PLEASE TRY AGAIN-------------------------------------------------------------------")
                    pass
            if(ao=="N" or ao=="n"):
                break