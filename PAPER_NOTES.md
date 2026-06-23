# PAPER_NOTES.md

# Efficient Estimation of Word Representations in Vector Space

**Authors:** Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean
**Year:** 2013

---

# 1. Central Claim of the Paper

The main claim of this paper is that high-quality word embeddings can be learned using much simpler architectures than the neural language models that were commonly used at the time.

The authors introduce two models, **CBOW (Continuous Bag of Words)** and **Skip-Gram**, and show that these models can learn meaningful word representations while requiring significantly less computational cost and training time.

Even though the architectures are simpler, the learned word vectors are still able to capture useful semantic and syntactic relationships between words.

---

# 2. Problem Being Solved

Traditional NLP systems usually treat words as independent symbols. Because of this, they do not naturally understand relationships between words.

For example, a traditional system does not know that:

* King and Queen are related
* Paris and France are related
* Big and Bigger are related

The goal of this paper is to learn vector representations of words so that words with similar meanings or relationships are located close to each other in the vector space.

---

# 3. Previous Approaches

Before introducing CBOW and Skip-Gram, the paper discusses older neural language models.

### NNLM (Neural Network Language Model)

* Learns useful word vectors
* Uses hidden layers and many parameters
* Computationally expensive
* Slow to train on large datasets

### RNNLM (Recurrent Neural Network Language Model)

* Uses information from previous words
* Can model longer context
* Produces good results
* Requires even more computation and training resources

The authors observed that these models worked well but were difficult to train efficiently on very large datasets.

---

# 4. Proposed Method

The paper introduces two new architectures for learning word embeddings.

## CBOW (Continuous Bag of Words)

The CBOW model predicts the current word using the surrounding context words.

Example:

Context words:

I, love, programming

Target word:

competitive

The model uses the surrounding words as input and tries to predict the missing word in the middle.

### Advantages

* Simple architecture
* Fast training
* Efficient on large datasets
* Produces useful word embeddings

---

## Skip-Gram

The Skip-Gram model works in the opposite direction.

Instead of predicting the current word from the context, it predicts the surrounding context words from the current word.

Example:

Input word:

competitive

Predicted context:

I, love, programming

### Advantages

* Learns high-quality embeddings
* Performs well on semantic tasks
* Works better with rare words

---

# 5. Dataset Used in the Paper

The original paper trained its models on a very large Google News corpus containing approximately **6 billion words**.

Because reproducing this setup requires significant computational resources, my implementation uses a much smaller custom corpus for demonstration purposes.

The goal of my implementation was to understand and reproduce the core CBOW architecture rather than match the exact scale of the original paper.

---

# 6. Evaluation Method

The paper evaluates word embeddings using semantic and syntactic analogy tasks.

The idea is to check whether relationships between words are preserved inside the learned vector space.

Some examples used in the paper include:

### Semantic Relationships

* Paris : France
* Berlin : Germany
* King : Queen
* Man : Woman

### Syntactic Relationships

* Big : Bigger
* Small : Smaller
* Walk : Walked
* Work : Works

The paper uses vector arithmetic to test these relationships.

A famous example shown in the paper is:

King - Man + Woman ≈ Queen

If the model learns good embeddings, these relationships can be recovered from the vector space.

---

# 7. Key Findings from the Paper

Some important findings reported by the authors are:

* Increasing training data improves performance.
* Larger embedding dimensions improve performance.
* CBOW trains very quickly while maintaining good accuracy.
* Skip-Gram generally learns stronger semantic relationships.
* Word embeddings can capture meaningful relationships between words.

The paper demonstrates that simple architectures can achieve strong results without requiring extremely complex neural networks.

---

# 8. Learned Relationships

One of the most interesting observations from the paper is that word embeddings capture relationships between words.

Examples include:

* Paris - France + Italy ≈ Rome
* King - Man + Woman ≈ Queen
* Big - Bigger + Small ≈ Smaller

These examples show that semantic and syntactic information is encoded inside the vector space learned by the model.

---

# 9. My Implementation

For this task, I implemented a **simplified CBOW model using PyTorch**.

The implementation performs the following steps:

1. Reads a text corpus.
2. Creates context-target training pairs.
3. Builds a vocabulary.
4. Learns word embeddings using the CBOW architecture.
5. Trains the model using cross-entropy loss and gradient descent.
6. Extracts the learned word embeddings.
7. Uses cosine similarity to inspect relationships between words.

Due to limited time and computational resources, I used a small custom dataset instead of the original Google News corpus used in the paper.

Although the results are not directly comparable to the paper's large-scale experiments, the implementation successfully demonstrates the core idea behind CBOW and how word embeddings can be learned from surrounding context.

---

# 10. Personal Understanding

My main takeaway from this paper is that useful word representations do not necessarily require very deep or complex neural networks.

The CBOW and Skip-Gram architectures are relatively simple, but they are still capable of learning meaningful relationships between words. This paper also helped me understand the basic idea of word embeddings and how vector representations can capture semantic information in natural language.
