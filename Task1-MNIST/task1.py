
import tensorflow as tf
from tensorflow import keras
import numpy as np

print("="*55)
print("  CCS 2226 - MNIST Digit Recognition")
print("="*55)


print("\nStep (a): Downloading MNIST Dataset...")

# Keras downloads MNIST automatically on first run
# Dataset contains 70,000 images of handwritten digits (0-9)
# 60,000 for training and 10,000 for testing
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print(f"Dataset downloaded successfully!")
print(f"Training images : {x_train.shape[0]}")
print(f"Testing images  : {x_test.shape[0]}")
print(f"Image size      : {x_train.shape[1]}x{x_train.shape[2]} pixels")
print(f"Digit classes   : 0 to 9")


print("\nStep (b): Building model to distinguish digits 0 to 9...")

# Normalize pixel values from 0-255 to 0-1
# This helps the model learn faster and more accurately
x_train = x_train / 255.0
x_test  = x_test  / 255.0

print("Pixel values normalized from 0-255 to 0-1")


model = keras.Sequential([
    # Flatten: convert 28x28 image into a 784 length array
    keras.layers.Flatten(input_shape=(28, 28)),

    # Hidden layer 1: 128 neurons with ReLU activation
    # ReLU helps the model learn complex patterns
    keras.layers.Dense(128, activation='relu'),

    # Dropout: randomly turn off 20% of neurons during training
    # This prevents the model from memorizing the training data
    keras.layers.Dropout(0.2),

    # Output layer: 10 neurons, one for each digit 0-9
    # Softmax converts outputs to probabilities that sum to 1
    keras.layers.Dense(10, activation='softmax')
])

print("\nModel Architecture:")
model.summary()


model.compile(
    optimizer='adam',             # Adam optimizer adjusts learning rate automatically
    loss='sparse_categorical_crossentropy',  # Loss for multi-class classification
    metrics=['accuracy']          # Track accuracy during training
)



print("\nTraining the model on MNIST data...")
print("Epochs: 5 (each epoch = one full pass through training data)")
print("-"*55)

history = model.fit(
    x_train, y_train,
    epochs=5,           # Train for 5 rounds
    batch_size=32,      # Process 32 images at a time
    validation_split=0.1,  # Use 10% of training data for validation
    verbose=1
)


print("\nEvaluating model on test data...")
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)

print(f"\nTest Accuracy : {test_accuracy * 100:.2f}%")
print(f"Test Loss     : {test_loss:.4f}")



print("\nSample Predictions (first 10 test images):")
print("-"*55)

# Get predictions for the first 10 test images
predictions = model.predict(x_test[:10], verbose=0)

print(f"{'Image':<8} {'Actual Digit':<15} {'Predicted Digit':<18} {'Confidence'}")
print("-"*55)

for i in range(10):
    actual    = y_test[i]
    predicted = np.argmax(predictions[i])  # Pick digit with highest probability
    confidence = np.max(predictions[i]) * 100
    status = "CORRECT" if actual == predicted else "WRONG"
    print(f"{i+1:<8} {actual:<15} {predicted:<18} {confidence:.1f}%  {status}")



print("\nAccuracy per digit (0-9):")
print("-"*55)

all_predictions = np.argmax(model.predict(x_test, verbose=0), axis=1)

for digit in range(10):
    # Find all test images that are this digit
    digit_indices = np.where(y_test == digit)[0]
    digit_predictions = all_predictions[digit_indices]
    correct = np.sum(digit_predictions == digit)
    total = len(digit_indices)
    accuracy = correct / total * 100
    print(f"Digit {digit}: {correct}/{total} correct  ({accuracy:.1f}%)")

print("\n" + "="*55)
print("MNIST Task Complete")
print(f"Overall Test Accuracy: {test_accuracy * 100:.2f}%")
print("The model can successfully distinguish digits 0 to 9")
print("="*55)
