import random

RESPONSES = [
    "It is certain.",
    "Without a doubt",
    "Most likely",
    "Ask again later",
    "Can not predict now",
    "Do not count on it",
    "My reply is no",
    "Very Doubtful",

]

def get_eight_ball_response():
    return random.choice (RESPONSES)