import streamlit as st
from rembg import remove # silmeyi sağlayan kütüphane
from PIL import Image
import base64
import io

def main():
    # Özel logo ekleme
    logo_image = Image.open("logom.png")
    st.image(logo_image, width=200)
    st.balloons()

    st.info("JPEG,JPG,PNG fotoğrafları yükleyebilirsiniz. Yükledikten sonra fotoğrafın görüntülenmesini bekleyin. Arka Planı Yok et butonuna basarak arka planı kaldırabilirsiniz. Ardından Fotoğrafı indir butonu ile kaydedebilirsiniz. ")

    st.title("Arka Plan Kaldırıcı")

    uploaded_file = st.file_uploader("Lütfen bir fotoğraf yükleyin", type=["jpg", "jpeg", "png"])

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
                    output.save("output.png","PNG")
                    with open("output.png", "rb") as file:
                        btn = st.download_button(
                            label="Download image",
                            data=file,
                            file_name="output.png",
                            mime="image/png"
                )

    st.text("Made by Müşerref Selçuk Özdemir")


if __name__ == "__main__":
    main()
