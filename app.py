import streamlit as st 
import streamlit.components.v1 as components

with st.sidebar:
    
    st.title("Harshit Wadhwani ")
    components.html('<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="harshitwadhwani" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/harshitwadhwani?trk=profile-badge">Harshit Wadhwani</a></div>', height = 310 )
    with open("HARSHIT WADHWANI CV .pdf", "rb") as file:
        btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name="HARSHIT WADHWANI CV .pdf"
            )