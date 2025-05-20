import streamlit as st

st.title("Selamat datang di Website Informatika")
st.image("view/young.png", width=200)
st.write("\n")
st.subheader("ngodingseru bersama Bapak Hendri Setiadi, S.Tr.Kom, Gr.")
st.write(
    "Mari latihan membuat Website sederhana melalui Github dan Framework Streamlit"
)
st.write(
    """
    - Menggunakan github.com
    - Framework Streamlit.io
    """
)

st.image("python.jpg", width=200)

#########

st.title("Aplikasi Sederhana")

# Menggunakan layout kolom
col1, col2 = st.columns(2)

with col1:
    st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
    angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

    if (angka % 2) == 0:
        st.write(f"{angka} adalah Bilangan Genap")
    else:
        st.write(f"{angka} adalah Bilangan Ganjil")

with col2:
    st.header("Aplikasi menghitung Total Belanja")

    def hitung_total(harga, jumlah):
        return harga * jumlah

    harga_barang = st.number_input("Masukkan Harga Barang:", value=0, step=1000)
    jumlah_barang = st.number_input("Masukkan Jumlah Barang:", value=0, step=1)
    total_harga = hitung_total(harga_barang, jumlah_barang)

    if total_harga > 100000:
        total_harga_diskon = total_harga - 0.05 * total_harga
        st.write(f"Total Harga (dengan diskon): Rp. {total_harga_diskon:,.0f}")
    else:
        st.write(f"Total Harga: Rp. {total_harga:,.0f}")

    bayar = st.number_input("Masukkan Jumlah Uang:", value=0, step=10000)

    if bayar >= total_harga:
        kembalian_uang = bayar - total_harga
        st.write(f"Uang Kembalian: Rp. {kembalian_uang:,.0f}")
    else:
        st.write("Uang yang anda bayarkan kurang ")


###########################

st.header (":mailbox: Get in touch with Me!")
st.title(f"Mail Message", anchor=False)
#st.page == "Contact":
st.write("Feel free to contact us with any questions or inquiries.")

contact_form_html = """
    <form action="https://formsubmit.co/thishendri@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your name" required style="padding: 10px; margin-bottom: 20px; border-radius: 5px; border: 1px solid #ccc;">
         <input type="email" name="email" placeholder="Your email" required style="padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
         <textarea name="message" placeholder="Your message here" style="padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; height: 150px;"></textarea>
         <button type="submit" style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">Send</button>
    </form>
"""

st.markdown(contact_form_html, unsafe_allow_html=True)

# You can add other contact information below the form
st.write("Email: contact@example.com")
st.write("Phone: 123-456-7890")
