import streamlit as st

st.title("Latihan membuat Website")
st.write(
    "Latihan membuat website melalui Github dan Streamlit dengan menggunakan bahasa Python"
)
    
st.image("view/young.png" width=200px)


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
