from helper import get_completion

prompt = """
Classify the sentiment of the following sentence
as Positive, Negative, or Neutral.

Example:

Sentence:
"The phone is excellent and I love using it."

Sentiment:
Positive

Now classify this sentence:

Sentence:
"The laptop is extremely slow and freezes frequently."

Return only the sentiment.
"""
response = get_completion(prompt)

print(response)