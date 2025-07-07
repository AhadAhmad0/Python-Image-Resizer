import cv2

# Configurable Parameters
source = "335934.jpg"
destination = 'newImage.png'
scale_percent = 50

src = cv2.imread("335934.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)

# Percent by which the image is resized

# Calculate the 50 percent of the original dimensons
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# Resize image
output = cv2.resize(src , (new_width , new_height))

cv2.imwrite('newImage.png' , output)
cv2.waitKey(0)