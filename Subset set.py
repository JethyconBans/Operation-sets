def main():
    PINK = "\033[38;5;206m"
    LIGHT_ORANGE = "\033[38;5;214m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RESET = "\033[0m"

    while True:  
        setA = set(input(f"{YELLOW}Enter elements of the first set separated by spaces:{RESET} ").split(','))
        setB = set(input(f"{YELLOW}Enter elements of the second set separated by spaces:{RESET} ").split(','))

        operations = {
            '1': ('Union of setA and setB', sorted(setA.union(setB))),
            '2': ('Intersection of setA and setB', sorted(setA.intersection(setB))),
            '3': ('Symmetric Difference of setA and setB', sorted(setA.symmetric_difference(setB))),
            '4': ('Difference (set1 - set2) and (set2 - set1)', f"{sorted(setA.difference(setB))}\n{sorted(setB.difference(setA))}"),
            '5': ('Is set1 is a subset of set2? \nIS set2 ia a subset of set1?', f"{(setA.issubset(setB))}\n{(setB.issubset(setA))}"),
            '6': ('Is set1 is a proper subset of set2? \nIs setB is a proper subset of setA?', f"{(setA < setB)}\n{(setB < setA)}"),
            '7': ('Is set1 is a superset of set2? \nIs setB is a superset of setA?', f"{(setA.issuperset(setB))}\n{(setB.issuperset(setA))}"),
            '8': ('Is set1 is a proper superset of set2? \nIs setB is a proper superset of setA', f"{(setA > setB)}\n{(setB > setA)}"),
        }

        print(f"""
           {BLUE}Select an operation:{RESET}
           {GREEN}1. Union{RESET}
           {GREEN}2. Intersection{RESET}
           {GREEN}3. Symmetric Difference{RESET}
           {GREEN}4. Difference of (setA - setB) and (setB - setA){RESET}
           {GREEN}5. Is setA is a subset of set2? and set2 is a subset of set1?{RESET}
           {GREEN}6. Is setA a proper subset of set2 and setB is a proper subset of setA?{RESET}
           {GREEN}7. Is setA a superset of setB and setB is a superset of setA?{RESET}
           {GREEN}8. Is setA a proper superset of setB? and setB is a proper superset of setA{RESET}
           {RED}9. Exit{RESET}
        """)


        choice = input(f"{LIGHT_ORANGE}Enter the number corresponding to your choice:{RESET} ")


        if choice in operations:
            operation_name, result = operations[choice]
            print(f"{BLUE}{operation_name}:{RESET}\n{PINK}{result}{RESET}")
        elif choice == '9':
            print(f"{RED}Exiting the program.{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please select a valid operation.{RESET}")
        
        another = input(f"{YELLOW}Do you want to perform another operation? (yes/no): {RESET}").strip().lower()
        if another != 'yes':
            print(f"{RED}Exiting the program.{RESET}")
            break

if __name__ == "__main__":
    main()
