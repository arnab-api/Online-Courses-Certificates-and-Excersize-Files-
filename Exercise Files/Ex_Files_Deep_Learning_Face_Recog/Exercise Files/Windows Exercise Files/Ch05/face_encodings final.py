import face_recognition

# Load the jpg files into numpy arrays
image = face_recognition.load_image_file("/home/arnab/my_codes/Ex_Files_Deep_Learning_Face_Recog/Exercise Files/Windows Exercise Files/Ch05/person.jpg")

# Generate the face encodings
face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0:
    # No faces found in the image.
    print("No faces were found.")

else:
    # Grab the first face encoding
    first_face_encoding = face_encodings[0]

    # Print the results
    print(first_face_encoding)
