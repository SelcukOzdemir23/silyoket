import streamlit as st
from rembg import remove
from PIL import Image
import base64

def main():
    st.title("Arka Plan Kaldırıcı")

    uploaded_file = st.file_uploader("Lütfen bir fotoğraf yükleyin", type=["jpg", "jpeg", "png"])

    # Özel logo ekleme
    logo_image = Image.open("path/to/your/logo.png")
    st.image(logo_image, width=200)

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Yüklenen Fotoğraf", use_column_width=True)

        if 'image/jpeg' not in uploaded_file.type and 'image/png' not in uploaded_file.type:
            st.warning("Yalnızca JPG veya PNG formatındaki fotoğraflar desteklenmektedir.")
        else:
            if st.button("Arka Planı Yok Et"):
                with st.spinner("Arka plan kaldırılıyor..."):
                    output = remove(image)
                    st.image(output, caption="Arka Planı Yok Edilmiş Fotoğraf", use_column_width=True)

                    if st.button("Fotoğrafı İndir"):
                        download_image(output)


def download_image(output):
    # Çıktıyı geçici bir dosyaya kaydedin
    output_path = "output.png"  # Kaydedilecek dosya adı ve uzantısı
    output.save(output_path, "PNG")  # Çıktıyı PNG formatında kaydet

    # Dosyayı indirme butonuyla indirin
    st.download_button(label="Fotoğrafı İndir", data=output_path, file_name="output.png")


if __name__ == "__main__":
    main()
