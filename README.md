# What-sThat
A project that allows the user to choose or upload and image, and returns the image with boxes around objects it recognizes.


-----------------------------


The current MVP is here in the object_detection.py file:
This file takes in a picture from your current working directory and then tries to find items inside of the picture.
**NOTE: In order for this to work, you still need the file provided above inside of your current working directory



Installation Steps:
1.) Download and install Python3 from: https://python.org

2.) Install the following dependencies: 

pip3 install tensorflow

pip3 install opencv-python

pip3 install keras

pip3 install imageai --upgrade

3.) 
In order to use this, you need to download this binary file:
https://drive.google.com/file/d/1o3TvjNBINHsBQC6VNSFs_Oghn47SIv9U/view?usp=sharing

Once downloaded, place it inside of your What-sThat/Flask/static/images   
folder (or for our MVP, place it in the folder where your pictures you want to test are)

Your folder should look a little something like this:
https://imgur.com/a/h56zk4S

4.) run the script using:
python3 object_detection.py

Screenshots of the script working:
Running the code, asking for you to input the image. (REMINDER, image needs to be inside of your cwd)
https://drive.google.com/file/d/1aJ7HtyFcRg6UQLcpLkmCFRO3YrE7GEFZ/view?usp=sharing

Terminal results:
https://drive.google.com/file/d/1X9nhTB0dmykA4hDlHzJtwh-_UTqgrYVv/view?usp=sharing

What your current working directory should look like:
https://drive.google.com/file/d/1v1Okc_VcGbAtRDaJYNyOayxrLkorD51m/view?usp=sharing

New image showing what the script found:
https://drive.google.com/file/d/1TbVVj_p_N9_3qJA8uUvlJTnyYE2Z5GJL/view?usp=sharing

If your're curious, you can also check the new.jpeg-objects folder out, where the folder compiles snippets of the picture where it found something, this is what the folder looks like:
https://drive.google.com/file/d/1uhV6-2DJf9CQAboUCKgV3gt5gb1UX5j4/view?usp=sharing

What one of the pictures looks like:
https://drive.google.com/file/d/17AJL0PBwV0xEUVM5YjvZh-_ehKvpWVHl/view?usp=sharing


