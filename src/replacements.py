"""
a dictionary of replacements
"""

replacements = {
    'central': 'Xentral',  # 'Xentral' is unknown to the neural net ^^
    'Central': 'Xentral',
}


def apply_replacements(text):
    """
    replace all keys in replacements with their values
    """
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text
