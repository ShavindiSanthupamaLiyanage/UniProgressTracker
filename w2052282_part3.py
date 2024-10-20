# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other sources referenced within my code solution
# Student ID: W2052282,20234042
# Date: 11.12.2023

import graphics
from graphics import *

print("PART 01:")
total = 0

progress_LIST = []
module_trailer_LIST = []
module_retriever_LIST = []
exclude_LIST = []

# Identifying whether a staff member or a student
while True:
    option = int(input("Calculating the progress outcome\n"
                       "  01.Staff Member\n  02.Student\nPlease enter the option to start: "))
    if option == 1 or option == 2:
        break
    else:
        print('')
        print("Enter a valid option to continue")

# Only staff members can input more than one set of data
def progression_outcome(pass_credit, defer_credit, fail_credit):
    total_credit = (pass_credit + defer_credit + fail_credit)
    if total_credit == 120:  #validation of total credits equal to 120 or not
        if pass_credit == 120:
            print("Progress")
            if option == 1:
                progress_LIST.append((pass_credit, defer_credit, fail_credit))

        elif pass_credit == 100:
            print("Progress (module trailer)")
            if option == 1:
                module_trailer_LIST.append((pass_credit, defer_credit, fail_credit))

        elif fail_credit >= 80:
            print("Exclude")
            if option == 1:
                exclude_LIST.append((pass_credit, defer_credit, fail_credit))

        else:
            print("Module retriever")
            if option == 1:
                module_retriever_LIST.append((pass_credit, defer_credit, fail_credit))

    else:
        print("Total incorrect")

# Create_histogram
def create_histogram():
    win_width = 400
    win_height = 400
    win = GraphWin("HISTOGRAM", win_width, win_height)
    label = Text(Point(x=85, y=24), text="Histogram Results")
    label.draw(win)

    # Progress_bar
    progress = Rectangle(Point(x=25, y=280), Point(x=100, y=280 - len(progress_LIST) * 20))
    progress.setFill("#aef8a1")
    progress.draw(win)

    progress_name = Text(Point(x=63, y=290), text="Progress")
    progress_name.draw(win)

    progress_count_text = Text(Point(x=63, y=260 - len(progress_LIST) * 20), text=str(len(progress_LIST)))
    progress_count_text.draw(win)

    # Trailer_bar
    trailer = Rectangle(Point(x=110, y=280), Point(x=185, y=280 - len(module_trailer_LIST)*20))
    trailer.setFill("#a0c689")
    trailer.draw(win)

    trailer_name = Text(Point(x=150, y=290), text="Trailer")
    trailer_name.draw(win)

    trailer_count_text = Text(Point(x=150, y=260 - len(module_trailer_LIST) * 20), text=str(len(module_trailer_LIST)))
    trailer_count_text.draw(win)

    # Retriever_bar
    retriever = Rectangle(Point(x=195, y=280), Point(x=270, y=280 - len(module_retriever_LIST)*20))
    retriever.setFill("#a7bc77")
    retriever.draw(win)

    retriever_name = Text(Point(x=233, y=290), text="Retriever")
    retriever_name.draw(win)

    retriever_count_text = Text(Point(x=233, y=260 - len(module_retriever_LIST) * 20), text=str(len(module_retriever_LIST)))
    retriever_count_text.draw(win)

    # Exclude_bar
    exclude = Rectangle(Point(x=280, y=280), Point(x=355, y=280 - len(exclude_LIST)*20))
    exclude.setFill("#d2b6b5")
    exclude.draw(win)

    retriever_name = Text(Point(x=320, y=290), text="Exclude")
    retriever_name.draw(win)

    retriever_count_text = Text(Point(x=320, y=260 - len(exclude_LIST) * 20), text=str(len(exclude_LIST)))
    retriever_count_text.draw(win)

    # Total Outcome
    total_outcome = len(progress_LIST) + len(module_trailer_LIST) + len(module_retriever_LIST) + len(exclude_LIST)
    total_outcome = Text(Point(x=100, y=330), text=str(total_outcome) + ", outcomes in total")
    total_outcome.draw(win)

    # Draw the x-axis
    x_axis = Line(Point(20, 280), Point(360, 280))
    x_axis.setWidth(2)
    x_axis.draw(win)

    return win

if option == 1:
    def progression_data():

        try:
            with open('progression_data.txt', 'a') as file:
                for marks in progress_LIST:
                    file.write(f"Progress - {marks[0]}, {marks[1]}, {marks[2]}\n")
                for marks in module_trailer_LIST:
                    file.write(f"Module Trailer - {marks[0]}, {marks[1]}, {marks[2]}\n")
                for marks in module_retriever_LIST:
                    file.write(f"Module Retriever - {marks[0]}, {marks[1]}, {marks[2]}\n")
                for marks in exclude_LIST:
                    file.write(f"Exclude - {marks[0]}, {marks[1]}, {marks[2]}\n")
        except FileNotFoundError:
            print("Progression data not found.")

# Staff Member
if option == 1:
    while True:
        try:
            print('')
            pass_credit = int(input("Please enter your credits at pass: "))
            if pass_credit not in range(0, 121, 20):
                print("Out of range")
                continue

            defer_credit = int(input("Please enter your credits at defer: "))
            if defer_credit not in range(0, 121, 20):
                print("Out of range")
                continue

            fail_credit = int(input("Please enter your credits at fail: "))
            if fail_credit not in range(0, 121, 20):
                print("Out of range")
                continue

            progression_outcome(pass_credit, defer_credit, fail_credit)

        except ValueError:
            print("Integer required")

        while True:
            select_preferance = str(input("\nWould you like to enter another set of data?"
                                          "\nEnter 'y' for yes or 'q' to quit and view results: "))
            if select_preferance == 'y':
                break
            elif select_preferance == 'q':
                histogram = create_histogram()
                progression_data()

                print("\nPART 02:")
                for marks in progress_LIST:
                    print("Progress -", marks[0], ",", marks[1], ",", marks[2])
                for marks in module_trailer_LIST:
                    print("Module trailer -", marks[0], ",", marks[1], ",", marks[2])
                for marks in module_retriever_LIST:
                    print("Module retriever -", marks[0], ",", marks[1], ",", marks[2])
                for marks in exclude_LIST:
                    print("Exclude -",  marks[0], ",", marks[1], ",", marks[2])

                file = open('progression_data.txt', 'r')
                print('')
                print("PART 03:")
                print(file.read())
                file.close()

                while True:
                    if histogram.isOpen():
                        try:
                            histogram.getMouse()
                        except graphics.GraphicsError:
                            pass  #Igmore and skip the error and do nothing if window is closed
                    else:
                        break
                exit()
            else:
                print("Valid input required")

# Student
elif option == 2:
    total_credit = 0
    while total_credit != 120:
        try:
            print('')
            pass_credit = int(input("Please enter your credits at pass: "))
            if pass_credit not in range(0, 121, 20):
                print("Out of range")
                continue

            defer_credit = int(input("Please enter your credits at defer: "))
            if defer_credit not in range(0, 121, 20):
                print("Out of range")
                continue

            fail_credit = int(input("Please enter your credits at fail: "))
            if fail_credit not in range(0, 121, 20):
                print("Out of range")
                continue

            progression_outcome(pass_credit, defer_credit, fail_credit)
            total_credit = pass_credit + defer_credit + fail_credit

        except ValueError:
            print("Integer required")