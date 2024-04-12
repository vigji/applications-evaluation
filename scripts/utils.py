import pandas as pd
from pathlib import Path
import random
import numpy as np
from tqdm import tqdm
import os

import requests

# Load wordlist to drawn keywords from:
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

def _get_word_sequence(seed, n_words=2):
    """Get random word sequence seeding from from number."""

    np.random.seed(seed)

    words = [WORDS[random.randint(0, len(WORDS))].decode() for _ in range(n_words)]

    return "-".join(words)


def _convert_to_word_sequence(seed_str, n_words=2):
    """String to word sequence with hash."""
    seed = hash(seed_str)

    return _get_word_sequence(seed, n_words=n_words)


def anonymize_df(df, seed_from="E-mail", drop_columns= ["Name", "Surname", "E-mail", "Affiliation (institution, laboratory)", "Position "],
              n_words=2):
    """Anonymization function; it seeds the generation from the email, and assign a random
    sequence of words that are easier to work with and remember than numbers.
    
    Function also drop columns with personal information.
    
    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to anonymize.
    seed_from : str
        The column to seed the generation from.
    drop_columns : list
        The columns to drop from the dataframe.
    n_words : int
        The number of words to generate.
        
        Returns
        -------
        
        pd.DataFrame
            The anonymized dataframe.
    """
    df = df.copy()
    df.index = (df[seed_from].apply(_convert_to_word_sequence, dict(n_words=n_words)))
    df.index.name = "code"
    return df.drop(drop_columns, axis=1)