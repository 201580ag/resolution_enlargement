import cv2
import os

def upscale_image(input_image, scale_factor):
    image = cv2.imread(input_image)
    height, width = image.shape[:2]
    new_height, new_width = int(height * scale_factor), int(width * scale_factor)
    new_dim = (new_width, new_height)
    resized_image = cv2.resize(image, new_dim, interpolation=cv2.INTER_LINEAR)
    return resized_image

if __name__ == "__main__":
    input_image_path = input("Enter image file path: ")

    if not os.path.isfile(input_image_path):
        print("Invalid file path.")
    else:
        options = {
            "4k": 2.0,
            "8k": 4.0,
            "16k": 8.0,
            "32k": 16.0,
            "64k": 32.0
        }

        print("Select one of the following options:")
        for option in options:
            print(f"- {option}")

        selected_option = input("choice: ")

        scale_factor = options.get(selected_option.lower())

        if scale_factor is None:
            print("Invalid option selection.")
        else:
            upscaled_image = upscale_image(input_image_path, scale_factor)

            _, file_extension = os.path.splitext(input_image_path)

            output_file_path = f"upscaled_{selected_option.lower()}{file_extension}"
            cv2.imwrite(output_file_path, upscaled_image)
            print(f"Image zoomed in successfully. Storage Path: {output_file_path}")
