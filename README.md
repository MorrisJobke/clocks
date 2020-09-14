## Clock

Adds a little clock in the lower right corner based on the EXIF date of an image. The new image is then stored under the same name with the prefix `-clock`.

### Requirements

OS X

    brew install opencv
    ln -s /usr/local/Cellar/opencv/4.4.0_2/lib/python3.8/site-packages/cv2/python-3.8/cv2.cpython-38-darwin.so cv2.so
    pipenv install
    pipenv shell
    cd path/with/many/images
    python path/to/clock.py


