# Task: Write a function called is_spam_email that takes an email subject line and 
# body as input and determines whether it is likely to be spam based on certain keywords. 
# The function should return True if the email is classified as spam and False otherwise.

def is_spam_email(subject: str, body: str) -> bool:
    # List of common spam keywords
    spam_keywords: list[str] = ["win", "free", "click here",
                                "urgent", "prize", "lottery", "money", "offer"]

    # Normalize the subject and body to lowercase
    subject = subject.lower()
    body = body.lower()

    # Check for keywords in the subject and body
    for keyword in spam_keywords:
        if keyword in subject or keyword in body:
            return True  # Found a spam keyword

    return False  # No spam keywords found
