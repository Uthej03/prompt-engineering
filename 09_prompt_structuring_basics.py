from helper import get_completion

prompt = """
Role:
You are a beginner-friendly AI learning coach.

Task:
Create a 7-day beginner study plan for learning Prompt Engineering.

Context:
The learner is completely new to Prompt Engineering.
The learner can spend only 1 hour per day studying.

Constraints:
Use simple beginner-friendly language.
Focus on practical learning.
Do not include advanced topics.
Keep each day's study within 1 hour.

Output Format:
For each day, show:
- Day number
- Topic
- What to learn
- One practical exercise
"""

response = get_completion(prompt)

print("Structured Prompt Result:")
print(response)