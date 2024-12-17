import streamlit as st
from gensim.summarization import summarize

# Judul Aplikasi
st.title("Ringkasin")
st.subheader("Extractive Text Summarization menggunakan Gensim")

# Input teks dari pengguna
text = st.text_area("Masukkan teks yang ingin diringkas", height=300)

# Tombol untuk menjalankan summarization
if st.button("Ringkas Teks"):
    if len(text.split()) > 50:  # Minimal jumlah kata untuk ringkasan
        try:
            # Set rasio ringkasan default
            ratio = 0.5
            summary = summarize(text, ratio=ratio)
            if summary.strip():  # Memastikan ringkasan tidak kosong
                st.subheader("Hasil Ringkasan:")
                st.write(summary)
            else:
                st.error("Ringkasan kosong. Pastikan teks memiliki struktur yang cukup.")
        except ValueError as e:
            st.error(f"Kesalahan: {e}. Pastikan teks cukup panjang dan memiliki struktur.")
    else:
        st.warning("Masukkan teks dengan lebih dari 50 kata.")

