import csv
import sys


def main():

    # Check for command-line usage
    if (len(sys.argv) != 3):
        sys.exit("Please include the 1) CSV file of individuals' STR counts   2) DNA Sequence")

    # Read database file into a variable
    List = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for elements in reader:
            List.append(elements)
            # list of dictionaries

    # Read DNA sequence file into a variable
    sequence = []
    with open(sys.argv[2]) as file:
        reader = csv.reader(file)
        for x in reader:
            sequence.append(x)

    # Find longest match of each STR in DNA sequence
    matches = []
    dict = List[0]
    for items in dict:
        subsequence = str(longest_match(sequence[0][0], items))
        matches.append(subsequence)

    # Check database for matching profiles
    count = 0
    matched = []
    for dicts in List:
        for items in dicts:
            if ((dicts[items] == matches[count]) and (count == 1)):
                matched.append(dicts["name"])
                count += 1
            elif ((dicts[items] != matches[count]) and (dicts["name"] in matched)):
                matched.remove(dicts["name"])
                count += 1
            else:
                count += 1
                continue
        count = 0

    if (len(matched) == 1):
        print(matched[0])
    else:
        print("No match")
    # sequence is a list containing a list with one element of a str
    # subsequence is a str
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
