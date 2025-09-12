# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
"I am a high school student with a background in java programming, but have no prior experience with python. Create a problem set of 5-7 questions that cover the basics of python a beginner needs to know. Assume knowledge of programming concepts, but not how concepts are applied to python."

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Variables & Types
 Write a Python program that declares the following:
    A string variable name set to "Alice",
    An integer age set to 17,
    A float gpa set to 3.8,
    A boolean is_honor_student set to True.

Then, print all of them in a formatted sentence.
🧪 Test: Output should be:
 "Alice is 17 years old, has a GPA of 3.8, and honor student status is True."

PROBLEM 2: Conditionals
 Write a Python function grade_level(age) that returns:
    "Elementary" if age < 11,
    "Middle" if 11 <= age < 14,
    "High School" if 14 <= age < 18,
    "College" otherwise.
"""
def grade_level(age: int): #-> str :
    if age < 11:
        return("Elementary")
    elif 11<= age < 14:
        return("Middle") 
    elif 14<= age < 18:
        return("High School")
    else:
        return ("College")

"""
🧪 Test Cases:
 grade_level(10) → "Elementary"
 grade_level(13) → "Middle"
 grade_level(17) → "High School"
 grade_level(19) → "College"

PROBLEM 3: Loops and Ranges 
 Write a function sum_even_numbers(n) that returns the sum of all even numbers from 0 to n (inclusive).
💡 Use a for loop and range()
 🧪 Example: sum_even_numbers(10) should return 30 (0+2+4+6+8+10)
 """

def sum_even_numbers(n: int):
    total = 0
    # for num in range(n+1):
    #     total


    return total

"""
PROBLEM 4: Lists and Slicing
Given a list of test scores: scores = [88, 92, 79, 93, 85] 
Write Python code to: 
Print the last score,
Print the top 3 scores,
Add a new score 90, 
Sort the list in descending order.
🧪 Output should reflect proper list indexing, slicing, append(), and sort() usage.

PROBLEM 5: Functions and String Manipulation
Write a function reverse_words(sentence) that:
    Takes a string sentence,
    Splits it into words,
    Reverses the order of words,
    Returns the new sentence.
🧪 Example:
    reverse_words("I love Python") → "Python love I"
 
PROBLEM 6: 
    
Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
assert grade_level(10) == "Elementary", "grade_level of 10 failed"
assert grade_level(13) == "Middle", "grade_level of 13 failed"
assert grade_level(17) == "High School", "grade_level of 17 failed"
assert grade_level(19) == "College", "grade_level of 19 failed"

print("\nTesting Problem 2:")
assert sum_even_numbers(10) == 30, "sum_even_numbbers of 10 failed"

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


