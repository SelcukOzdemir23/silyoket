import streamlit as st
from rembg import remove
from PIL import Image
import base64
import io

def main():
    # Özel logo ekleme
    logo_image = Image.open("unnamed.png")
    st.image(logo_image, width=200)

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
                    
                    # if st.button("Fotoğrafı İndir"):
                    img_byte_arr = output.convert("RGB")
                    img_byte_io = io.BytesIO()
                    img_byte_arr.save(img_byte_io, format='JPEG')
                    img_byte_io.seek(0)

                    # Base64 kodlamasını gerçekleştirin
                    encoded_img = base64.b64encode(img_byte_io.read()).decode()
                    href = f'<a href="data:image/jpeg;base64,{encoded_img}" download="output.jpg">Fotoğrafı İndir</a>'
                    st.markdown(href, unsafe_allow_html=True)

                    st.title("Made by Müşerref Selçuk Özdemir")


if __name__ == "__main__":
    main()
