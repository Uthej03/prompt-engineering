from helper import get_completion

prompt = """
A laptop costs 50000 rupees.
The store gives a 10% discount on the original price.
After the discount, an 18% tax is added.

What is the final price of the laptop?

Show the important calculation steps clearly,
then give the final answer.

Use plain text only.
"""

response = get_completion(prompt)

print("Zero-shot Chain-of-Thought Result:")
print(response)
