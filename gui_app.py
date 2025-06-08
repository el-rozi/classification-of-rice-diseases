import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import os

# Muat model
MODEL_PATH = "best_resnet_model.keras"
model = load_model(MODEL_PATH)

# Label kelas
class_names = ['Bacterial leaf blight', 'Brown spot', 'Leaf smut']

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

def predict_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return

    # Tampilkan gambar dengan border
    img = Image.open(file_path)
    img_resized = ImageOps.contain(img, (224, 224))
    img_with_border = ImageOps.expand(img_resized, border=10, fill="#f0f0f0")
    img_tk = ImageTk.PhotoImage(img_with_border)
    label_img.configure(image=img_tk)
    label_img.image = img_tk

    # Prediksi
    processed = preprocess_image(file_path)
    prediction = model.predict(processed)
    class_idx = np.argmax(prediction)
    confidence = prediction[0][class_idx]

    label_result.config(
        text=f"Prediksi:\n{class_names[class_idx]}\n\nKepercayaan: {confidence*100:.2f}%",
        fg="#2f4f4f"
    )

# Setup root
root = tk.Tk()
root.title("🌾 Rice Leaf Disease Classifier - Pengenalan Pola")
root.geometry("450x600")
root.configure(bg="#ffffff")

# Judul
tk.Label(
    root, text="Klasifikasi Penyakit Daun Padi",
    font=("Helvetica", 18, "bold"), fg="#2e8b57", bg="#ffffff"
).pack(pady=(20, 10))

# Tombol upload
tk.Button(
    root, text="📷 Pilih Gambar", command=predict_image,
    font=("Helvetica", 12), bg="#4CAF50", fg="white",
    activebackground="#45a049", relief="flat", padx=20, pady=5
).pack(pady=10)

# Placeholder gambar
placeholder = Image.new("RGB", (244, 244), color="#f8f8f8")
ph_border = ImageOps.expand(placeholder, border=10, fill="#f0f0f0")
ph_img = ImageTk.PhotoImage(ph_border)
label_img = tk.Label(root, image=ph_img, bg="#ffffff")
label_img.image = ph_img
label_img.pack(pady=15)

# Label hasil
label_result = tk.Label(root, text="", font=("Helvetica", 14), bg="#ffffff", justify="center")
label_result.pack(pady=10)

# Footer
tk.Label(
    root, text="Model: ResNet50 | Dataset: Rice Leaf Disease",
    font=("Helvetica", 9), fg="#888888", bg="#ffffff"
).pack(side="bottom", pady=10)

root.mainloop()
