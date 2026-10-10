from helper import get_completion

prompt = """
Classify the sentiment of the sentence
as Positive, Negative, or Neutral.

Example 1:

Sentence:
"The phone is excellent and works perfectly."

Sentiment:
Positive

Example 2:

Sentence:
"I am very happy with the camera quality."

Sentiment:
Positive

Example 3:

Sentence:
"The battery drains very quickly."

Sentiment:
Negative

Example 4:

Sentence:
"I expected much better performance for this price."

Sentiment:
Negative

Example 5:

Sentence:
"The package arrived on Tuesday."

Sentiment:
Neutral

Example 6:

Sentence:
"The phone comes with a charger and a USB cable."

Sentiment:
Neutral

Now classify this sentence:

Sentence:
"The display looks beautiful, but the battery barely lasts half a day."

Return only the sentiment.
"""

response = get_completion(prompt)
print(response)
