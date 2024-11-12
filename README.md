# Identity Card Tampering Detection with Computer Vision

This project leverages computer vision techniques to detect tampering in identity cards, assisting organizations in verifying the authenticity of ID cards provided by employees, customers, and other individuals. By employing image processing tools, this project identifies subtle differences in card images, aiding in the detection of potential forgeries or alterations.

---

## Project Overview

Using several key libraries for image processing, this project can determine if an identity card is genuine or tampered with by examining structural similarities and differences. The approach relies on advanced techniques such as Structural Similarity Index (SSIM), contour analysis, and thresholding to identify visual discrepancies in ID images.

---

## Libraries Used

This project utilizes a set of libraries essential for image analysis and tampering detection. Here’s a breakdown of each library's role:

- **`skimage.metrics` (Structural Similarity - SSIM)**
  - **Library**: scikit-image
  - **Functionality**: The `structural_similarity` function (SSIM) provides a metric for comparing similarity between two images by analyzing luminance, contrast, and structure.
  - **Usage**: SSIM is crucial for detecting subtle differences, making it ideal for tampering detection, as it can quantify even slight alterations in images.

- **`imutils`**
  - **Library**: imutils
  - **Functionality**: A set of helper functions simplifying basic image processing tasks, especially when using OpenCV, including resizing, rotating, and adjusting image orientation.
  - **Usage**: Optimizes image processing by streamlining tasks, reducing code requirements, and enhancing code readability when working with images in OpenCV.

- **`cv2` (OpenCV)**
  - **Library**: OpenCV
  - **Functionality**: A comprehensive computer vision library that supports image and video processing, including reading, editing, and analyzing images.
  - **Usage**: OpenCV, alongside SSIM, plays a vital role in tampering detection by highlighting visual differences and supporting advanced tasks like feature extraction and image comparison.

- **`PIL` (Python Imaging Library) / Pillow**
  - **Library**: Pillow (a modern fork of PIL)
  - **Functionality**: Enables fundamental image manipulations, such as loading, saving, and basic image modifications.
  - **Usage**: Integrates seamlessly with OpenCV, allowing for efficient handling of various image formats and simplifying conversion tasks between libraries.

- **`requests`**
  - **Library**: requests
  - **Functionality**: Provides an easy interface for sending HTTP requests, commonly used to fetch data from online sources.
  - **Usage**: Used to retrieve images from URLs, enabling remote image handling, which is particularly useful for accessing and processing images stored on online platforms.

---

## Methodology

The following steps are used to detect tampering in ID cards:

### Structural Similarity (SSIM)
1. **SSIM Calculation**: This step calculates the similarity between an original image and a test image, identifying differences in shape, contrast, or luminance.
2. **Tampering Detection**: Lower SSIM scores often indicate tampered images.

### Thresholding and Contour Detection
1. **Image Conversion**: Convert images to grayscale and apply thresholding to create a binary format.
2. **Contour Analysis**: Identify contours to analyze the structure and shape of the ID, revealing visual discrepancies or anomalies that could indicate tampering.

---

## Practical Applications

This project can be applied in various organizations where ID verification is required, such as:
- Businesses
- Government agencies
- Institutions

By automating tampering detection, organizations can improve security and streamline the verification process, useful for verifying ID types such as voter IDs, employee badges, and national ID cards.

---

## Results Interpretation

In one test case, the **SSIM value was approximately 69%**, indicating a high likelihood of tampering. Visualization techniques, including displaying contours, differences, and thresholded images, were used to highlight discrepancies clearly.

---

## Example Dashboard View

The following dashboard provides a visual analysis of ID tampering:

![Screenshot of Dashboard View 1](screenshots/Capture%20d'écran%202024-11-12%20194057.png)
![Screenshot of Dashboard View 2](screenshots/Capture%20d'écran%202024-11-12%20194154.png)
![Screenshot of Dashboard View 2](screenshots/Capture%20d'écran%202024-11-12%20194109.png)

---



