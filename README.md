## Clock


### Requirements

OS X

    brew install homebrew/science/opencv
    ln -s /usr/local/Cellar/opencv/2.4.12/lib/python2.7/site-packages/cv.py cv.py
    ln -s /usr/local/Cellar/opencv/2.4.12/lib/python2.7/site-packages/cv2.so cv2.so
    mkvirtualenv clock --python=python2.7 --system-site-packages
    workon clock
    pip install numpy --upgrade


