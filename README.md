# Paper to Code: Word2Vec CBOW

## Overview

This project was completed as part of Project X 2026 Task 3 (Paper → Code Research Implementation Challenge).

The paper I selected was:

**Efficient Estimation of Word Representations in Vector Space (2013)**
by Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean.

The goal of this project was to understand the core idea of the paper and implement one of its proposed architectures from scratch.

For this implementation, I chose the **CBOW (Continuous Bag of Words)** model because it is simpler and faster to train while still demonstrating the main concepts introduced in the paper.

---

## Paper Summary

Traditional NLP systems treat words as independent symbols and do not naturally understand relationships between words.

The paper proposes two efficient architectures:

* CBOW (Continuous Bag of Words)
* Skip-Gram

These models learn vector representations (embeddings) for words by using surrounding context information.

One of the most interesting findings from the paper is that the learned embeddings capture meaningful relationships such as:

King - Man + Woman ≈ Queen

The paper shows that these simple architectures can learn high-quality word representations while requiring much less computation than previous neural language models.

---

## What I Implemented

This project contains a simplified implementation of the CBOW architecture using PyTorch.

The implementation performs the following steps:

1. Reads a text corpus from `corpus.txt`
2. Tokenizes the text
3. Builds a vocabulary
4. Creates CBOW context-target training pairs
5. Trains a CBOW neural network
6. Learns word embeddings
7. Performs similarity searches using cosine similarity
8. Performs simple analogy tests

---

## Project Structure

```text
word2vec-project/

├── PAPER_NOTES.md
├── README.md
├── corpus.txt

├── src/
│   └── cbow.py

└── results/
    ├── training_log.png
    ├── similarity_results.png
    └── analogy_results.png
```

---

## Model Architecture

The implemented CBOW model follows the basic structure described in the paper:

```text
Context Words
      ↓
Embedding Layer
      ↓
Average Embeddings
      ↓
Linear Layer
      ↓
Predict Target Word
```

The model uses surrounding words as input and predicts the target word in the middle.

---

## Dataset

The original paper trained on a Google News corpus containing approximately 6 billion words.

Due to limited computational resources and project scope, I used a much smaller custom corpus (`corpus.txt`) to demonstrate the architecture and learning process.

The objective of this project was to reproduce the core idea of CBOW rather than match the original training scale.

---

## How to Run

### Install PyTorch

```bash
pip install torch
```

### Run the Program

```bash
python src/cbow.py
```

---

## Output

The program produces:

### Training Logs

The loss is displayed during training so that learning progress can be observed.

### Similarity Search

Examples:

```text
Most similar to 'king'
Most similar to 'queen'
Most similar to 'student'
Most similar to 'computer'
```

### Analogy Tests

Examples:

```text
man : king :: woman : ?
boy : prince :: girl : ?
```

---

## Results

The model successfully:

* Learned word embeddings from the training corpus
* Reduced training loss over time
* Produced similarity scores between words
* Performed simple analogy testing

Because the training corpus is very small compared to the original paper, the results are not directly comparable to the published results. However, the implementation demonstrates the core idea behind CBOW and word embeddings.

Screenshots of the outputs can be found in the `results` folder.

---

## Limitations

This implementation is intentionally simplified.

Some differences from the original paper include:

* Small custom corpus instead of billions of words
* Small embedding size
* Limited training time
* No large-scale distributed training
* No attempt to reproduce the exact accuracy reported in the paper

These simplifications were made to keep the implementation understandable and manageable within the scope of the task.

---

## What I Learned

Through this project I learned:

* What word embeddings are
* Why Word2Vec became important in NLP
* The difference between CBOW and Skip-Gram
* How context can be used to learn word representations
* How embeddings can capture semantic relationships
* How to implement and train a simple neural network using PyTorch

Overall, this project helped me understand how a relatively simple model can learn meaningful information about language from text data.
