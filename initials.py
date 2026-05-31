# File: initials.py
# Description: Print out my initials T, E, G in stylized large block letters.
# Each letter is 12 characters wide by 10 characters high and is
#composed of the capital letter it represents. Each letter is
# followed by a large period (2x2 asterisks). Three periods border
#the left and right of each letter. No trailing spaces on any line.
# Assignment Number: 1

# Name: Tawfiq Eliasu
# STUDENT ID:2425402864
# Email:2425402864@live.gctu.edu.gh
# Grader:Augustus Buckman
# On my honor,Tawfiq Eliasu, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    # Print initials "TEG" in small form, then as large 12x10 block letters.
    # Initials: T (Tawfiq), E (Eliasu), G .
    # Layout per row: ...LETTER(12)...PERIOD(2) repeated for each of the 3 initials.
    # Total width = (3+12+3+2) * 3 = 60 characters (trailing spaces stripped).
    # The large period appears as two "**" rows at rows 8 and 9 (0-indexed).

    # --- Large T: 12 wide x 10 tall, made of 'T' characters ---
    T = [
        "TTTTTTTTTTTT",
        "     TT     ",
        "     TT     ",
        "     TT     ",
        "     TT     ",
        "     TT     ",
        "     TT     ",
        "     TT     ",
        "     TT     ",
        "     TT     ",
    ]

    # --- Large E: 12 wide x 10 tall, made of 'E' characters ---
    E = [
        "EEEEEEEEEEEE",
        "EE          ",
        "EE          ",
        "EE          ",
        "EEEEEEEE    ",
        "EEEEEEEE    ",
        "EE          ",
        "EE          ",
        "EE          ",
        "EEEEEEEEEEEE",
    ]

    # --- Large G: 12 wide x 10 tall, made of 'G' characters ---
    G = [
        " GGGGGGGGGG ",
        "GG          ",
        "GG          ",
        "GG          ",
        "GG   GGGGGGG",
        "GG        GG",
        "GG        GG",
        "GG        GG",
        "GG        GG",
        " GGGGGGGGGG ",
    ]

    # --- Large period: 2 wide, asterisks at rows 8 and 9 only ---
    period = [
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "**",
        "**",
    ]

    letters = [T, E, G]

    # Print blank line, small initials, blank line
    print()
    print("...TEG")
    print()

    # Print the 10 rows of large block letters
    for row in range(10):
        line = ""
        for letter in letters:
            line += "..."          # three-period left border
            line += letter[row]   # 12-character letter row
            line += "..."          # three-period right border
            line += period[row]   # 2-character large period column
        # Strip trailing spaces (period cols are blank on rows 0-7)
        print(line.rstrip())

    # Final blank line
    print()


main()



