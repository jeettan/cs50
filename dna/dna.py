import csv
import sys


def main():

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:
        print("Please only two arguments")
        exit()

    # TODO: Read database file into a variable

    filename = sys.argv[1]
    filename2 = sys.argv[2]

    # TODO: Read database file into a variable

     #TODO: Read DNA sequence file into a variable

    dictionary = []
    dictionary2 = {}
    comparison = []

    try:
        with open(filename, 'r') as file:
            csvreader = csv.reader(file)
            row1 = next(csvreader)
            for i in row1[1:]:
                dictionary2[i] = 0


        with open(filename2, 'r') as file:
            lines = str(file.readlines())

    except:
        print("You didn't enter a correct filename")

    # TODO: Find longest match of each STR in DNA sequence

    for dna in dictionary2:
        y = longest_match(lines, dna)
        dictionary2[dna] = y
        dictionary.append(y)

    # TODO: Check database for matching profiles

    match = 0
    counter = 0

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for data in reader:
            for x in data[1:]:
                comparison.append(int(x))
            if (comparison == dictionary):
                match = 1
                break
            else:
                comparison = []
                counter = counter + 1

    if (match != 1):
        print("No match")
        return

    counter = counter+1

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if(i == counter):
                answer = row[0]

    print(answer)

    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()


#    with open(filename , 'r') as file:
#       csvreader = csv.reader(file)
#        for j in csvreader:
#            for k in j[1:]:
#                print(k)

