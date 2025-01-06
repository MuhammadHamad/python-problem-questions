# Customer Feedback Analysis
# You are working for a company that collects customer feedback from an online survey. The survey responses are stored as a single string containing multiple sentences. Your task is to:

# Clean the responses: Remove unnecessary punctuation and spaces at the beginning and end of the feedback.
# Identify customer sentiment: Count how many times the words "good," "great," "excellent," or "bad" appear in the feedback to gauge overall sentiment.
# Extract key feedback: Split the responses into individual sentences for further analysis.
# Highlight key details: Capitalize each sentence to make the feedback more readable.
# Create a report: Format the cleaned and capitalized sentences back into a readable paragraph for your manager.

# ? SOLUTION 1

# Input feedback string
import re
feedback = "    the service was good! the food was excellent. However, the wait time was too long. overall, a good experience!  "

# Clean the responses
cleaned_feedback = feedback.strip()

# Identify customer sentiment
sentiment_words = ["good", "great", "excellent", "bad"]
sentiment_count = {word: cleaned_feedback.lower().count(word)
                   for word in sentiment_words}

# Extract key feedback (split into sentences)
sentences = cleaned_feedback.split(". ")

# Highlight key details (capitalize sentences)
capitalized_sentences = [sentence.capitalize() for sentence in sentences]

# Create a formatted report
formatted_report = ". ".join(capitalized_sentences) + "."
print(f"Formatted Report:\n{formatted_report}")


# ? SOLUTION 2

# Input feedback string
feedback = "    the service was good! the food was excellent. However, the wait time was too long. overall, a good experience!  "

# Clean the responses
# Remove unnecessary spaces and punctuations explicitly
cleaned_feedback = feedback.strip().rstrip("! ")

# Identify customer sentiment
# Manually find all sentiment words using a loop and count occurrences
sentiment_words = ["good", "great", "excellent", "bad"]
sentiment_count = {}
for word in sentiment_words:
    sentiment_count[word] = cleaned_feedback.lower().count(word)

# split into sentences
# Use punctuation marks ('.' or '!') to split into sentences
sentences = re.split(r'[.!?]\s*', cleaned_feedback)

# Remove any empty strings that might result from splitting
sentences = [sentence for sentence in sentences if sentence]

# capitalize sentences
# Handle the capitalization by iterating through each sentence
capitalized_sentences = [sentence.strip().capitalize()
                         for sentence in sentences]

# Create a formatted report
# Join the sentences with '. ' but ensure the last sentence ends with a period
formatted_report = ". ".join(capitalized_sentences) + "."
print("\nFormatted Report:")
print(formatted_report)
