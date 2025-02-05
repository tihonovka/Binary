import random
import hashlib
import os

def generate_binary_string(length):
    """Generál egy bináris stringet a megadott hosszal."""
    return "".join(random.choice(["0", "1"]) for _ in range(length))

def bin_to_dec(binary):
    """Bináris számot decimálisba vált."""
    return str(int(binary, 2))

def calculate_checksum(text):
  """Kiszámolja a szöveg SHA-256 checksumját"""
  return hashlib.sha256(text.encode()).hexdigest()[:8]

def generate_quiz(num_questions, min_bits=5, max_bits=10):
    """Generál egy kvízt a megadott paraméterekkel."""
    quiz_content = []
    for i in range(num_questions):
        binary_length = random.randint(min_bits, max_bits)
        binary_number = generate_binary_string(binary_length)
        decimal_value = bin_to_dec(binary_number)
        question = f"{i+1}.  Mi a {binary_number} bináris szám decimális értéke?"
        checksum = calculate_checksum(question)
        question_with_checksum = f"{question}  # {checksum}"
        quiz_content.append(question_with_checksum)
        #quiz_content.append(decimal_value)
        quiz_content.append('0')
    return "\n".join(quiz_content)

def save_quiz_to_file(filename, quiz_content):
  """Elmenti a kvízt egy fájlba, ha az még nem létezik."""
  if not os.path.exists(filename):
      with open(filename, "w") as file:
          file.write(quiz_content)

if __name__ == "__main__":
    num_questions = 30
    min_bits = 5
    max_bits = 9
    filename = "quiz.txt"
    quiz_content = generate_quiz(num_questions, min_bits, max_bits)
    save_quiz_to_file(filename, quiz_content)
    print(f"A kvíz ({filename}) sikeresen létrehozva.")
