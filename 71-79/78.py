"""
Question:

Please write a program to generate all sentences where 
- subject is in ["I", "You"] and 
- verb is in ["Play", "Love"] and 
- the object is in ["Hockey","Football"].
"""

def func78():
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey","Football"]

    for s in subjects:
        for v in verbs:
            for o in objects:
                print(f'{s} {v} {o}')

func78()