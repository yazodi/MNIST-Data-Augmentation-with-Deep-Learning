# 🧠 MNIST Data Augmentation with Deep Learning

Bu projede MNIST el yazısı rakam verileri üzerine TensorFlow kullanarak veri artırma (data augmentation) işlemleri gerçekleştirildi ve CNN modeli eğitildi.

## 🚀 Özellikler
- TensorFlow ile veri artırma (parlaklık, kontrast, yatay çevirme)
- Basit CNN modeli ile rakam sınıflandırma
- Modelin Streamlit web uygulaması
- Huggingface üzerinden model paylaşımı

## 📊 Kullanılan Yöntemler
- `tf.image` modülüyle veri artırma
- CNN (Convolutional Neural Network)
- Modelin `.h5` formatında kaydedilmesi
- Streamlit arayüzü ile yükleme ve tahmin

## 🖼️ Streamlit Arayüz
Streamlit ile model şu işlemleri yapar:
- Görsel yükleme
- Otomatik artırma
- Model ile tahmin

## 🧠 Huggingface Modeli
[Modeli Görüntüle](https://huggingface.co/kullaniciadi/mnist-augmentation-model)

## 🖥️ Uygulamayı Çalıştırma

```bash
pip install -r requirements.txt
streamlit run app.py



 Yazar
[Hande Çarkcı]