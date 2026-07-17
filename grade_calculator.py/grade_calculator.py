# Grade Calculator
# Built by Bernice and Edith
# This program calculates students' average scores and assigns grades.
# Grade Calculator
# Built by Edith Oppong
# This program calculates students' average scores and assigns grades.


def get_scores():
    """
    Collect scores for multiple subjects.
    Returns a list of scores.
    """
    scores = []

    while True:
        score = input("Enter a score (or type 'done' to finish): ")

        if score.lower() == "done":
            break

        try:
            score = float(score)

            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    return scores


def calculate_average(scores):
    """
    Calculates and returns the average score.
    """
    if len(scores) == 0:
        return 0

    return sum(scores) / len(scores)


def get_grade(average):
    """
    Returns the letter grade based on the average.
    """
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def grade_message(grade):
    """
    Prints a message based on the student's grade.
    """
    messages = {
        "A": "Excellent work! Keep it up!",
        "B": "Very Good! You're doing well.",
        "C": "Good effort. Keep improving.",
        "D": "You passed, but you need more practice.",
        "F": "Failed. Study harder and try again."
    }

    return messages[grade]


def process_student():
    """
    Collects information for one student and displays the result.
    """
    name = input("\nEnter student name: ")

    print(f"Enter scores for {name}")

    scores = get_scores()

    if len(scores) == 0:
        print("No scores entered.")
        return

    average = calculate_average(scores)
    grade = get_grade(average)

    print("\n------ RESULT ------")
    print("Student:", name)
    print("Average Score:", round(average, 2))
    print("Grade:", grade)
    print(grade_message(grade))
    print("--------------------")


def main():
    """
    Main program loop.
    Allows multiple students to be processed.
    """
    print("=== Student Grade Calculator ===")

    while True:
        process_student()

        again = input("\nDo you want to calculate another student's grade? (yes/no): ")

        if again.lower() != "yes":
            print("\nThank you for using the Grade Calculator!")
            break


main()