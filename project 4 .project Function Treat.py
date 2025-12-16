print("Welcome to the Data Analyzer and Transformer Program")


data = []


while True:
    print("\n Welcome to the Data Analyzer and Transformer Program ")
    print("Main Menu")
    print("1.Input Data")
    print("2.Display Data Summary (Built-in Functions)")
    print("3.Calculate Factorial (Recursion)")
    print("4.Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6.Display Dataset Statistics (Return multiple values )")
    print("7.Exit program")


    choice = input("Please Enter your choice(1-7):") 

    # Input Data
    
    if choice == "1":
        data = list(map(int, input("\nEnter data for a 1D array (separated by spaces):").split()))
        print("Data has been stored successfully")

    # Display Data Summary (Built-in-Functions)
    
    elif choice == "2":
        print("Display Data Summary")
        print("Total element:",len(data))
        print("Minimum value:",min(data))
        print("Maximum value:",max(data))
        print("Sum of all value:",sum(data))
        print("Average value:",round(sum(data)/ len(data),2))

    # Calculate Factorial (Recursion)
    
    elif choice == "3":
        def Factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * Factorial(n-1)
        print(Factorial(5))
        
    # Filter Data by Threshold (Lambda Function)
    
    elif choice == "4":
        threshold = int(input("\nEnter a threshold value to filter out data above this value:"))
        filtered = list(filter(lambda x : x >= threshold,data))
        print(f"\n Filtered Data (values >= {threshold}):")
        print(", ".join(map(str, filtered)))

    # sort Data
    
    elif choice == "5":
        print("\nChoose sorting option:")
        print("1.Ascending")
        print("2.Descending")
        sort_choice = int(input("Enter your choice"))

        if sort_choice == 1:
            print("sorted Data in Ascending order:")
            print(", ".join(map(str, sorted(data))))
        else:
            print("sorted Data in Descending order:")
            print(", ".join(map(str, sorted(data , reverse=True))))
            
    # Display Dataset Statistics (Return Multiple Values)
    
    elif choice == "6":
        def Dataset_statistics(data):
             minimum = min(data)
             maximum = max(data)
             total = sum(data)
             avg = total / len(data)
             return minimum, maximum, total, avg

        min_val, max_val, total, avg = Dataset_statistics([12, 56,54,23])

        print("Minimum:", min_val)
        print("Maximum:", max_val)
        print("Total:", total)
        print("Average:", avg)

    # Exit program
    
    elif choice == "7":
        print("Exiting program ....Good bye")
        break

    else:
        print("Invalid choice please try again ")
                  
                            


            
        
              
              
                      
        
