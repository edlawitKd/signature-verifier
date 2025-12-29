import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
from verify import verify_signature

class SignatureVerifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Signature Verification System")
        self.root.geometry("500x600")

        # Title
        self.label_title = Label(root, text="Signature Verification", font=("Arial", 18, "bold"))
        self.label_title.pack(pady=10)

        # Image display
        self.image_label = Label(root)
        self.image_label.pack(pady=10)

        # Result display
        self.result_label = Label(root, text="", font=("Arial", 16))
        self.result_label.pack(pady=10)

        # Button to choose signature image
        self.btn_select = Button(
            root,
            text="Choose Signature Image",
            font=("Arial", 12),
            command=self.open_image
        )
        self.btn_select.pack(pady=20)

    def open_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Signature Image",
            filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
        )

        if not file_path:
            return

        # Display the selected image
        img = Image.open(file_path)
        img = img.resize((320, 200))
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

        # Verify signature using the single model
        result = verify_signature(file_path)

        # Color coding: green for genuine, red for forged
        if "Genuine" in result:
            self.result_label.config(text=result, fg="green")
        elif "Forged" in result:
            self.result_label.config(text=result, fg="red")
        else:
            self.result_label.config(text=result, fg="orange")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SignatureVerifierApp(root)
    root.mainloop()
