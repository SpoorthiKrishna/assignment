def read_and_write_file(filename):

    try:            #indentation error

        with open(filename,'r')as file:

            content=file.read()
        with open(filename,'w')as file:
            file.write(content.upper())
        print(f"file'{filename}'processed successfully")
    except Exception as e:
        print(f"an error occurred: {str(e)}")

def main():
    filename="sample.txt"
    read_and_write_file(filename)

if __name__=="__main__":
    main()