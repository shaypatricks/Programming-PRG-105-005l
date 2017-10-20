def main():
    # Start the file at zero
    total = 0

    try:
        # Open the file.
        infile = open('names.txt', 'r')

        # Read and display the file's contents.
        for line in infile:
            words = line.split()
            print(words)
            total += len(words)
            print(total)
        # Close the file.
        infile.close()
    except:
        print("Error cant get list of names from file")


main()
