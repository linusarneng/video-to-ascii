import cv2

# ASCII density characters
density = "Ñ@#W$9876543210?!abc;:+=-,._          "

# Initialize video capture
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 64)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 48)

while True:
    # Capture frame-by-frame
    ret, frame = video.read()
    
    # Flip frame horizontally
    frame = cv2.flip(frame, 1)
    
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Resize frame to match ASCII size
    gray_frame = cv2.resize(gray_frame, (64, 48))
    
    # Convert pixels to ASCII characters
    ascii_image = ""
    for row in gray_frame:
        for pixel in row:
            char_index = int(pixel / 255 * (len(density) - 1))
            ascii_image += density[char_index]
        ascii_image += '\n'
    
    # Display ASCII image
    print(ascii_image)
    
    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
video.release()
cv2.destroyAllWindows()
