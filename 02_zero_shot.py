from helper import get_completion

prompt = """
Classify the sentiment of the following sentence
as Positive, Negative, or Neutral.

Sentence:
"The laptop performance is good, but the battery life could be better."

Return only the sentiment.
"""

result = get_completion(prompt)

print(result)