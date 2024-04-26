from tkinter import Tk, Canvas, PhotoImage, Button
from PIL import Image, ImageTk
import random
import os

class Wheel:
    def __init__(self, root) -> None:
        self.current_angle = 0
        self.end_angle = 0
        self.after_id = None

        self.wheel_image_tk = None

        # Images
        self.wheel_image_path = os.path.join(os.path.dirname(__file__), "Wheel.png")
        self.arrow_image_path = os.path.join(os.path.dirname(__file__), "Arrow.png")

        self.wheel_image = PhotoImage(file=self.wheel_image_path)
        self.arrow_image = PhotoImage(file=self.arrow_image_path)

        self.root = root

        # Now create the canvas and add the wheel image to it
        self.canvas = Canvas(self.root, width=self.arrow_image.width(), height=self.arrow_image.height())
        self.canvas.pack()

        self.wheel = self.canvas.create_image(0, 0, anchor='nw', image=self.wheel_image)
        self.arrow = self.canvas.create_image(0, 0, anchor='nw', image=self.arrow_image)
        self.canvas.coords(self.arrow, 0, 0)

    def UpdateRotation(self, angle):
        # Open the original image with Pillow
        original_img = Image.open(self.wheel_image_path)
        
        # Rotate the image by the given angle
        rotated_img = original_img.rotate(angle)

        # Convert the Pillow image to a Tkinter PhotoImage
        self.wheel_image_tk = ImageTk.PhotoImage(rotated_img)

        # Update the canvas with the new rotated image
        self.canvas.itemconfig(self.wheel, image=self.wheel_image_tk)

    def AnimateRotation(self, end_angle, step=9, speed=1, counter=0):
        if self.current_angle < end_angle:
            if counter % 20 == 0:
                speed += 1
            self.current_angle += step
            self.UpdateRotation(self.current_angle)
            self.after_id = self.root.after(speed, self.AnimateRotation, end_angle, step, speed)
        else:
            # Reset the angle for the next spin
            self.current_angle = 0

    def RotateWheel(self):
        # If there is an ongoing animation, stop it
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        # Calculate a new angle to rotate to
        # You can add logic here to ensure that the end_angle is different each time
        self.end_angle = int(random.uniform(0, 360)) + self.current_angle + 1080
        
        # Start the animation
        self.AnimateRotation(self.end_angle)

    def GetBonus(self, angle):
        right_angle = angle % 360
        if 0 <= right_angle < 45:
            return "$200"
        elif 45 <= right_angle < 90:
            return "$100"
        elif 90 <= right_angle < 135:
            return "$10"
        elif 135 <= right_angle < 180:
            return "$500"
        elif 180 <= right_angle < 225:
            return "Backruptcy"
        elif 225 <= right_angle < 270:
            return "$100"
        elif 270 <= right_angle < 315:
            return "$200"
        elif 315 <= right_angle < 360:
            return "$10"
