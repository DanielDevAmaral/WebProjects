import csv

def main():
    ID_INDEX = input("Please enter an I-Number (xxxxxxxxx): ")

    # Read the contents of the students.csv into a
    # compound dictionary named students_dict. Use
    # the ID numbers as the keys in the dictionary.
    students_dict = read_dictionary("C:\\Users\\Danie\\OneDrive\\Área de Trabalho\\BYUI\\cse111\\Week 9\\students.csv")

    if ID_INDEX in students_dict:
        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        name = students_dict[ID_INDEX]

        # Print the student's name.
        print(name)
    else:
        print("No such student")


def read_dictionary(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename: the name of the CSV file to read.

    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current row to the dictionary.
            if len(row_list) != 0:
                key = row_list[0]  # Assuming the ID is in the first column
                value = row_list[1]  # Assuming the name is in the second column
                dictionary[key] = value

    # Return the dictionary.
    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()
