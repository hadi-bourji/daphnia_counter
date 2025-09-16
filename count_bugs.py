import cv2
import numpy as np

def count(start_file, end_file):
    # Load the first and last frames
    start_img = cv2.imread(start_file)
    end_img = cv2.imread(end_file)

    # Convert to grayscale
    start_gray = cv2.cvtColor(start_img, cv2.COLOR_BGR2GRAY)
    end_gray = cv2.cvtColor(end_img, cv2.COLOR_BGR2GRAY)

    # Compute absolute difference
    diff = cv2.absdiff(start_gray, end_gray)

    # Pixels with difference > 25 are set to 255 (white), otherwise set to 0 (black)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel) #opening removes small noise
    thresh = cv2.dilate(thresh, kernel, iterations=2) #enlarges remaining non noise white regions

    # Find contours of moving objects
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Can tune min/max area depending on bug size
    min_area = 10
    max_area = 200
    moving_bugs = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if min_area < area < max_area:
            moving_bugs += 1

    print(f"Estimated living bugs: {moving_bugs}")

if __name__ == "__main__":
    count("start00.png", "end00.png")