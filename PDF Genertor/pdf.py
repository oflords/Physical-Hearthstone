import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def process_images_to_pdf(input_folder, output_pdf):
    # Dimensions in points (1 inch = 72 points): 2.48" x 3.46"
    target_width = 2.48 * 72
    target_height = 3.46 * 72
    loop_itr = 0
    image_itr = 0

    # Create a PDF canvas
    c = canvas.Canvas(output_pdf, pagesize=letter)
    page_width, page_height = letter

    # Define the number of columns and rows on each page
    columns = 3
    rows = 3

    # Define space between images
    padding = 10
    
    print("Starting task, please wait...")

    # Loop through all PNG files in the folder
    for file_name in sorted(os.listdir(input_folder)):
        if file_name.lower().endswith(".png"):
                file_path = os.path.join(input_folder, file_name)

                # Open the image
                with Image.open(file_path) as img:
                    # Convert image to RGBA if it has transparency
                    if img.mode == 'RGBA':
                        # Create a white background
                        white_background = Image.new('RGB', img.size, (255, 255, 255))
                        # Paste the original image on top of the white background
                        white_background.paste(img, (0, 0), img)
                        img = white_background  # Now the image has no transparency
                
                    # Calculate the position of the image on the page
                    col = loop_itr % columns
                    row = loop_itr // columns

                    x = col * (target_width + padding) + padding
                    y = page_height - (row + 1) * (target_height + padding) - padding

                    # Save the temporary image with white background to a new path
                    temp_path = "temp_image" + str(image_itr) + ".jpg"
                    img.save(temp_path, 'JPEG')
                
                    image_itr += 1

                    # Draw the resized image on the PDF canvas
                    # todo: make temp image higher res
                    c.drawImage(temp_path, x, y, width=target_width, height=target_height)

                    loop_itr += 1

                    # If we've filled a page, add a new page
                    if loop_itr % (columns * rows) == 0:
                        print("Page completed, starting next.")
                        c.showPage()
                        loop_itr = 0

                    # Delete the temporary file
                    os.remove(temp_path)

    # Save the PDF
    c.save()
    print(f"PDF saved as {output_pdf}")

# Example usage
input_folder = "print all these"  # Replace with the folder containing PNGs
output_pdf = "output.pdf"  # Replace with the desired PDF file name
process_images_to_pdf(input_folder, output_pdf)
