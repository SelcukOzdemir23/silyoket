import streamlit as st
from rembg import remove
from PIL import Image
import base64

def main():
    st.title("Arka Plan Kaldırıcı")

    uploaded_file = st.file_uploader("Lütfen bir fotoğraf yükleyin", type=["jpg", "jpeg", "png"])

    # Özel logo ekleme
    logo_image = Image.open("unnamed.png")
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

                    save_button = st.button("Fotoğrafı İndir")
                    if save_button:
                        save_image(output)


def save_image(output):
    # Çıktıyı geçici bir dosyaya kaydedin
    output_path = "output.png"  # Kaydedilecek dosya adı ve uzantısı
    output.save(output_path, "PNG")  # Çıktıyı PNG formatında kaydet

    # Dosyayı okuyun ve base64 kodlayın
    with open(output_path, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode()

    # İndirme bağlantısını oluşturun
    href = f'<a href="data:file/png;base64,{encoded_image}" download="output.png">Fotoğrafı İndir</a>'

    # İndirme bağlantısını görüntüleyin
    st.markdown(href, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
