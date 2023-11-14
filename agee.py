def get_age():
    age = input("input your age:")
    if age.isnumeric() and int(age)>=18:  # type error corrected by inserting int to age
        return int(age)
    else:
        return  None

def main():
    age =get_age()
    if age:
        print("you are {age} years old and eligible.")
    else:
        print("invalid input you must be at least 18 years old.")

if __name__=="__main__":
    main()