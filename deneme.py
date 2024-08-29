import random
from collections import defaultdict

def markov_chain(text, state_size=2):
    """Builds a Markov chain model from the given text."""
    words = text.split()
    model = defaultdict(list)
    
    for i in range(len(words) - state_size):
        state = tuple(words[i:i + state_size])
        next_word = words[i + state_size]
        model[state].append(next_word)
    
    return model

def generate_sentence(model, state_size=2, length=15):
    """Generates a random sentence from a Markov chain model."""
    state = random.choice(list(model.keys()))
    sentence = list(state)
    
    for _ in range(length - state_size):
        next_words = model.get(state)
        if not next_words:
            break
        next_word = random.choice(next_words)
        sentence.append(next_word)
        state = tuple(sentence[-state_size:])
    
    return ' '.join(sentence)

# Example usage
sample_text = """Artificial intelligence is the simulation of human intelligence processes by machines, 
especially computer systems. These processes include learning, reasoning, and self-correction."""
markov_model = markov_chain(sample_text, state_size=2)

# Generate a random sentence
random_sentence = generate_sentence(markov_model, state_size=2, length=10)
print("Generated Sentence:", random_sentence)
