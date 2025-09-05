def gradding_text(text):
    letters = sum(1 for char in text if char.isalpha())
    words = len(text.split())
    sentences = sum(1 for char in text if char in '.!?')
    
    L = (letters / words) * 100
    S = (sentences / words) * 100
    
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)

result = gradding_text(input("Text: "))
print(f"Grade {result}" if 1 <= result < 16 else "Before Grade 1" if result < 1 else "Grade 16+")