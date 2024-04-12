# applications-evaluation
Code to anonymise, randomize, assign applications to evaluate.

Overall, it:
- reads out 2 files: the application response data and data from reviewers conflict of interests (table where you mark names you know)
- anonymize everything by assigning a 2-random words code to each application
- assign a given number of reviews to reviewers balancing everything
- export files for the evaluators (`csv` for scores, `.md`/`.pdf` file with the applications to evaluate).
