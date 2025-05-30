import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Modeli yükle
model = tf.keras.models.load_model("mnist_augmented_model.h5")

# Başlık
st.title("🧠 MNIST Görüntü Artırma ve Tahmin")

# Görsel yükleme
uploaded_file = st.file_uploader("Bir el yazısı rakam görseli yükleyin (28x28, PNG/JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Görseli göster
    image = Image.open(uploaded_file).convert('L').resize((28, 28))
    st.image(image, caption="Orijinal Görsel", width=150)

    # Görseli normalize et
    img_array = np.array(image).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=-1)  # (28,28,1)
    img_array = np.expand_dims(img_array, axis=0)   # (1,28,28,1)

    # Görüntü artırma
    def augment(image):
        image = tf.image.random_flip_left_right(image)
        image = tf.image.random_brightness(image, max_delta=0.1)
        image = tf.image.random_contrast(image, 0.8, 1.2)
        return image

    augmented_img = augment(tf.convert_to_tensor(img_array[0])).numpy()

    # Görselleri yan yana göster
    col1, col2 = st.columns(2)
    col1.image(img_array[0].squeeze(), caption="Orijinal", use_column_width=True, clamp=True)
    col2.image(augmented_img.squeeze(), caption="Artırılmış", use_column_width=True, clamp=True)

    # Tahmin yap
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)

    st.markdown(f"### 🧾 Modelin Tahmini: **{predicted_class}**")
