import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from collections import Counter


# Small corpus for testing
with open("corpus.txt", "r", encoding="utf-8") as f:
    text = f.read()


# Tokenize
words = text.lower().split()

# Build vocabulary
vocab = sorted(set(words))
word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for word, idx in word_to_idx.items()}

print("Vocabulary Size:", len(vocab))
print(vocab)

# Create CBOW training pairs
window_size = 2
data = []

for i in range(window_size, len(words) - window_size):
    context = []

    for j in range(i - window_size, i + window_size + 1):
        if j != i:
            context.append(word_to_idx[words[j]])

    target = word_to_idx[words[i]]

    data.append((context, target))

print("\nNumber of training samples:", len(data))

# Show first 5 examples
for context, target in data[:5]:
    context_words = [idx_to_word[idx] for idx in context]

print("\nContext:", context_words)
print("Target :", idx_to_word[target])

# CBOW Model
class CBOW(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()

        self.embeddings = nn.Embedding(vocab_size, embedding_dim)

        self.linear = nn.Linear(embedding_dim, vocab_size)

    def forward(self, inputs):

        embeds = self.embeddings(inputs)

        embeds = embeds.mean(dim=0)

        out = self.linear(embeds)

        return out
    
# Model setup
embedding_dim = 10

model = CBOW(len(vocab), embedding_dim)

loss_function = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(), lr=0.01)

print("\nModel Created Successfully!")

# Training Loop
epochs = 100

for epoch in range(epochs):

    total_loss = 0

    for context, target in data:

        context_tensor = torch.tensor(context, dtype=torch.long)

        target_tensor = torch.tensor([target], dtype=torch.long)

        optimizer.zero_grad()

        output = model(context_tensor)

        loss = loss_function(
            output.unsqueeze(0),
            target_tensor
        )

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    if (epoch + 1) % 10 == 0:
        print(
            f"Epoch [{epoch+1}/{epochs}], Loss: {total_loss:.4f}"
        )

print("\nTraining Complete!")

# Extract learned embeddings
embeddings = model.embeddings.weight.data

print("\nLearned Embeddings Shape:")
print(embeddings.shape)

# Find most similar words

def most_similar(word, top_k=5):

    if word not in word_to_idx:
        print(f"{word} not in vocabulary")
        return

    word_idx = word_to_idx[word]

    word_embedding = embeddings[word_idx]

    similarities = []

    for i in range(len(vocab)):

        if i == word_idx:
            continue

        similarity = F.cosine_similarity(
            word_embedding.unsqueeze(0),
            embeddings[i].unsqueeze(0)
        ).item()

        similarities.append(
            (idx_to_word[i], similarity)
        )

    similarities.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print(f"\nMost similar to '{word}':")

    for similar_word, score in similarities[:top_k]:
        print(
            f"{similar_word:10s} {score:.4f}"
        )


most_similar("king")
most_similar("queen")
most_similar("boy")
most_similar("girl")
most_similar("student")
most_similar("teacher")
most_similar("computer")
most_similar("city")

def analogy(word1, word2, word3, top_k=5):

    if (
        word1 not in word_to_idx or
        word2 not in word_to_idx or
        word3 not in word_to_idx
    ):
        print("Word not found")
        return

    vec = (
        embeddings[word_to_idx[word2]]
        - embeddings[word_to_idx[word1]]
        + embeddings[word_to_idx[word3]]
    )

    similarities = []

    for i in range(len(vocab)):

        word = idx_to_word[i]

        if word in [word1, word2, word3]:
            continue

        score = F.cosine_similarity(
            vec.unsqueeze(0),
            embeddings[i].unsqueeze(0)
        ).item()

        similarities.append((word, score))

    similarities.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print(
        f"\n{word1} : {word2} :: {word3} : ?"
    )

    for word, score in similarities[:top_k]:
        print(word, round(score, 4))

analogy("man", "king", "woman")
analogy("boy", "prince", "girl")