from helper import get_completion

direct_prompt = """
A shirt costs 1200 rupees.
The shop gives a 25% discount.

What is the final price after the discount?

Return only the final answer.
"""

direct_response = get_completion(direct_prompt)

print("Direct Prompt Result:")
print(direct_response)

step_prompt = """
A shirt costs 1200 rupees.
The shop gives a 25% discount.

What is the final price after the discount?

Show the important calculation steps clearly,
then give the final answer.
"""

step_response = get_completion(step_prompt)

print("\nStep-by-Step Prompt Result:")
print(step_response)