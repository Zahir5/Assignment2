from PIL import Image

import time
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0: 
    generated_number += 10
print(generated_number)


def new_image_generator():
    # Load the original image
    original_image_path = 'chapter1.jpg'
    original_image = Image.open(original_image_path)

    # Defining the generated number
    n = generated_number

    # Get the dimensions of the image
    width, height = original_image.size

    # Create a new image object with the same size
    new_image = Image.new('RGB', (width, height))

    # Initialize a variable to store the sum of red pixel values
    sum_of_red_pixels = 0

    # Iterate through each pixel and apply the modification
    for x in range(width):
        for y in range(height):
            # Get the original pixel value
            original_pixel = original_image.getpixel((x, y))

            # Modify the pixel values using the generated number
            modified_pixel = tuple(value + n for value in original_pixel)

            # Add the red pixel value to the sum
            sum_of_red_pixels += modified_pixel[0]

            # Set the modified pixel value in the new image
            new_image.putpixel((x, y), modified_pixel)

    # Save the new image
    new_image_path = 'chapter1out.jpg'
    new_image.save(new_image_path)

    # Output the sum of red pixel values
    print(f"Sum of red pixel values in the new image: {sum_of_red_pixels}")
    print("Image modification completed. New image saved as 'chapter1out.jpg'")


# Call the new_image_generator function to create image and get the sum of red fixels
new_image_generator()

