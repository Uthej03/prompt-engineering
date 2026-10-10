from helper import get_completion

prompt = """
Classify the sentiment of the sentence
as Positive, Negative, or Neutral.

Example 1:

Sentence:
"The phone is excellent and I love using it."

Sentiment:
Positive

Example 2:

Sentence:
"The battery drains very quickly and the phone gets hot."

Sentiment:
Negative

Example 3:

Sentence:
"The package was delivered this afternoon."

Sentiment:
Neutral

Now classify this sentence:

Sentence:
"The camera quality is great, but the app crashes sometimes."

Return only the sentiment.
"""
response = get_completion(prompt)

print(response)