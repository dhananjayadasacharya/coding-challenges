# Challenge 007: Check salary for tax eligibility
# Accept name and salary. Check if their salary is >3L and display if they must pay tax

def main():
    name = input("Enter name: ")
    salary = float(input("Enter annual salary: "))

    if salary > 300000:
        print(name, "must pay tax")
    else:
        print(name, "does not need to pay tax")


if __name__ == "__main__":
    main()
