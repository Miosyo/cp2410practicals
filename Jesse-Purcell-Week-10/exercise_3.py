import mnist
from PIL import Image
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors=3)


def predict(image):
    # convert image to greyscale
    image = image.convert('L')
    # resize image to 28x28
    image = image.resize((28, 28))
    # convert to nmumpy array
    image = np.array(image)
    # invert image
    image = 255 - image
    # flatten image
    image = image.reshape((1, 28 * 28))

    # predict the label
    return classifier.predict(image)[0], list(classifier.predict_proba(image)[0])


test_labels = mnist.test_labels()
test_images = mnist.test_images()
train_labels = mnist.train_labels()
train_images = mnist.train_images()

train_images = train_images.reshape((len(train_images), 28 * 28))
classifier.fit(train_images, train_labels)

# Test the classifier
test_images = test_images.reshape((len(test_images), 28 * 28))
print(classifier.score(test_images, test_labels))

if __name__ == '__main__':
    image = Image.open('digit.png')
    image = image.convert('L')
    print(predict(image))
