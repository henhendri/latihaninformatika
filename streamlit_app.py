import streamlit as st

st.title("Selamat datang di Website Informatika")
st.subheader("ngodingseru bersama Bapak Hendri Setiadi, S.Tr.Kom, Gr.")
st.image("view/young.png", width=200)

st.write("\n")
st.subheader("Hendri Setiadi, S.Tr.Kom")
st.write(
    "Mari latihan membuat Website sederhana melalui Github dan Framework Streamlit"
)
st.write(
    """
    - Menggunakan github
    - Framework Streamlit
    """
)

st.image("python.jpg", width=200)


st.title("Toko Sederhana")

# Menggunakan layout kolom
col1, col2 = st.columns(2)

with col1:
    st.header("Cek Genap/Ganjil")
    angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

    if (angka % 2) == 0:
        st.write(f"{angka} adalah Bilangan Genap")
    else:
        st.write(f"{angka} adalah Bilangan Ganjil")

with col2:
    st.header("Hitung Total Belanja")

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









st.header (":mailbox: Get in touch with Me!")
st.title(f"Mail Message", anchor=False)
#st.page == "Contact":
st.write("Feel free to contact us with any questions or inquiries.")

contact_form_html = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
"""

st.markdown(contact_form_html, unsafe_allow_html=True)

# You can add other contact information below the form
st.write("Email: contact@example.com")
st.write("Phone: 123-456-7890")
