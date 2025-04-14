import streamlit as st
from cryptography.fernet import Fernet

# --- Generate or load a key ---
def load_key():
    return Fernet.generate_key()

# --- Encrypt function ---
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

# --- Decrypt function ---
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message).decode()
    return decrypted

# --- Streamlit UI ---
st.set_page_config(page_title="🔐 Secure Data Encryption App")

st.title("🔐 Secure Data Encryption System")
st.write("Encrypt and decrypt sensitive messages using Python and Cryptography.")

# Generate encryption key
key = load_key()
st.code(f"Encryption Key: {key.decode()}", language="bash")

# Input from user
user_input = st.text_area("🔤 Enter your message")

option = st.selectbox("Choose Action", ["Encrypt", "Decrypt"])

if st.button("Submit"):
    if user_input:
        try:
            if option == "Encrypt":
                encrypted_text = encrypt_message(user_input, key)
                st.success("✅ Encrypted Message:")
                st.code(encrypted_text)
            elif option == "Decrypt":
                decrypted_text = decrypt_message(user_input.encode(), key)
                st.success("🔓 Decrypted Message:")
                st.code(decrypted_text)
        except Exception as e:
            st.error("⚠️ Error occurred: " + str(e))
    else:
        st.warning("Please enter a message.")

