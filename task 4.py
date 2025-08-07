import re
import math
import pandas as pd

# Step 1: Create Dataset
data = {
    'text': [
        'Congratulations! You have won a lottery. Claim now!',
        'Reminder: Meeting at 10 AM tomorrow',
        'Get free entry into our contest. Click here!',
        'Are we still on for lunch?',
        'Urgent! Your account has been compromised. Update password.'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam']
}

df = pd.DataFrame(data)

# Step 2: Preprocess text
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

df['tokens'] = df['text'].apply(preprocess)

# Step 3: Split into train and test (manual split)
train_data = df.iloc[:4]
test_data = df.iloc[4:]

# Step 4: Build vocabulary and word counts
def build_word_counts(data):
    spam_words = {}
    ham_words = {}
    spam_count = 0
    ham_count = 0

    for _, row in data.iterrows():
        label = row['label']
        for word in row['tokens']:
            if label == 'spam':
                spam_words[word] = spam_words.get(word, 0) + 1
                spam_count += 1
            else:
                ham_words[word] = ham_words.get(word, 0) + 1
                ham_count += 1
    return spam_words, ham_words, spam_count, ham_count

spam_words, ham_words, spam_total, ham_total = build_word_counts(train_data)

# Step 5: Calculate prior probabilities
spam_docs = len(train_data[train_data['label'] == 'spam'])
ham_docs = len(train_data[train_data['label'] == 'ham'])
total_docs = len(train_data)

p_spam = spam_docs / total_docs
p_ham = ham_docs / total_docs

# Step 6: Prediction function using Naive Bayes
def predict(text):
    words = preprocess(text)
    spam_score = math.log(p_spam)
    ham_score = math.log(p_ham)
    vocab = set(list(spam_words.keys()) + list(ham_words.keys()))

    for word in words:
        spam_score += math.log((spam_words.get(word, 0) + 1) / (spam_total + len(vocab)))
        ham_score += math.log((ham_words.get(word, 0) + 1) / (ham_total + len(vocab)))

    return 'spam' if spam_score > ham_score else 'ham'

# Step 7: Test model
correct = 0
for _, row in test_data.iterrows():
    prediction = predict(row['text'])
    print(f"Text: {row['text']} -> Predicted: {prediction}, Actual: {row['label']}")
    if prediction == row['label']:
        correct += 1

accuracy = correct / len(test_data)
print(f"\nAccuracy: {accuracy * 100:.2f}%")
