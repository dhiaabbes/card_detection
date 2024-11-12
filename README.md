# card_detection

This project aims to detect identity cards using computer vision. It will assist organizations in verifying the authenticity of identity cards provided by employees, customers, or others.
## Screenshots
Libraries Overview in python 
This notebook uses several essential libraries for image processing and comparison to detect tampering in images. Here’s an overview of each library and its purpose in this project:

1. skimage.metrics (Structural Similarity - SSIM)
Library: scikit-image
Function: structural_similarity (SSIM) is used to measure the similarity between two images, taking into account luminance, contrast, and structure.
Usage: It’s particularly helpful for detecting subtle differences between images, which is valuable in tampering or quality detection tasks.
2. imutils
Library: imutils
Function: Provides helper functions that simplify basic image processing tasks with OpenCV, such as resizing, rotating, and adjusting image orientation.
Usage: By using imutils, we can streamline certain operations that would otherwise require additional code in OpenCV, making image processing more efficient.
3. cv2 (OpenCV)
Library: OpenCV
Function: A comprehensive library for computer vision tasks that supports image and video processing, including reading, modifying, and analyzing images.
Usage: Here, OpenCV works alongside structural_similarity to detect tampering by identifying visual differences in images, supporting tasks like feature extraction and image comparison.
4. PIL (Python Imaging Library) / Pillow
Library: Pillow (an updated fork of PIL)
Function: Enables image manipulation, such as loading, saving, and performing basic modifications on images.
Usage: PIL/Pillow integrates well with other image libraries like OpenCV, allowing for simplified handling of different image formats and conversion tasks.
5. requests
Library: requests
Function: Allows sending HTTP requests in Python, commonly used for fetching data from online sources.
Usage: In this project, requests can retrieve images from URLs, making it versatile for handling and processing images from remote sources with OpenCV or PIL.


Finding out structural similarity of the images helped us in finding the difference or similarity in the shape of the images. Similarly, finding out the threshold and contours based on those threshold for the images converted into grayscale binary also helped us in shape analysis and recognition. 

This project can be used in different organizations where customers or users need to provide any kind of id in order to get themselves verified. The organization can use this project to find out whether the ID is original or fake. Similarly this can be used for any type of ID like, voter id, etc.

#### As, our SSIM is ~69% we can say that the image user provided is fake or tampered.
#### Finally we visualized the differences and similarities between the images using by displaying the images with contours, difference and threshold.  
### Dashboard View
![Download](./screenshot/dash.png)
![Download](./screenshot/login.png)
![Download](./screenshot/profile.png)
![Download](./screenshot/project.png)
![Download](./screenshot/search.png)
![Download](./screenshot/tasks.png)
![Download](./screenshot/users.png)
