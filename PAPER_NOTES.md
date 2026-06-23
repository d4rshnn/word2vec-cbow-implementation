# PAPER_NOTES

## Paper

Efficient Estimation of Word Representations in Vector Space  
Tomas Mikolov et al. (2013)

---

## 1. What is the paper claiming?

The main claim of this paper is that useful word embeddings can be learned using much simpler architectures than previous neural language models.

Earlier models such as NNLM and RNNLM could learn good word representations, but they required a large amount of computation and training time.

The authors argue that simpler models can learn embeddings of similar quality while being significantly faster to train.

The two architectures proposed in the paper are:

- CBOW (Continuous Bag of Words)
- Skip-Gram

The paper shows that these models are able to capture meaningful relationships between words while reducing computational cost.

---

## 2. What architecture needs to be implemented?

For this task, I chose to implement the CBOW architecture.

### CBOW Idea

CBOW predicts a target word using its surrounding context words.

Example:

Context words:

king is ____ man

Target word:

a

The surrounding words are converted into embeddings, combined together, and then used to predict the missing word.

### Why CBOW?

I selected CBOW because:

- It is simpler to understand and implement.
- It trains faster than many older language models.
- It is one of the main contributions of the paper.
- It still learns useful word embeddings despite its simplicity.

### Main Components Used

- Vocabulary creation
- Context-target pair generation
- Embedding layer
- Linear output layer
- Cross-entropy loss
- Adam optimizer

The implementation follows the overall CBOW idea presented in the paper, but uses a much smaller dataset and model size because of limited compute resources.

---

## 3. Dataset, Evaluation Metric and Baseline

### Dataset

The original paper was trained on the Google News corpus containing billions of words.

For this reproduction task, I used a small custom text corpus stored in `corpus.txt`.

The goal was not to match the paper's accuracy, but to reproduce the core CBOW learning process.

### Evaluation

I evaluated the learned embeddings using:

1. Similarity tests

Examples:

- king
- queen
- student
- teacher
- city

The model checks which words are closest in the embedding space.

2. Analogy tests

Examples:

man : king :: woman : ?

boy : prince :: girl : ?

These tests are inspired by the word relationship experiments described in the paper.

### Baselines Mentioned in the Paper

The paper compares CBOW and Skip-Gram against older language models such as:

- NNLM (Neural Network Language Model)
- RNNLM (Recurrent Neural Network Language Model)

The authors show that the newer architectures achieve strong results while requiring less computation.

---

## My Understanding

My biggest takeaway from this paper is that model simplicity can sometimes be more important than model complexity.

The authors showed that CBOW and Skip-Gram can learn meaningful word relationships without requiring extremely complicated architectures.

This idea later became the foundation of Word2Vec and influenced many later NLP models.

While my implementation is a simplified version, it helped me understand how embeddings are learned and how semantic relationships can be represented using vectors.