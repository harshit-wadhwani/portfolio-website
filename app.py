import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image
from streamlit_timeline import timeline

with st.sidebar:
    image = Image.open("G:\\My Data\\personal photos\\forweb.jpg")
    st.image(image, width = 200)
    st.title("Harshit Wadhwani ")
    #components.html('<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="harshitwadhwani" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/harshitwadhwani?trk=profile-badge">Harshit Wadhwani</a></div>', height = 310 )
    with open("HARSHIT WADHWANI CV .pdf", "rb") as file:
        btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name="HARSHIT WADHWANI CV .pdf"
            )
        
st.title ("Intoduction")
st.write("Motivated and detail-oriented student with a strong foundation in Python programming and a passion for problem-solving, seeking opportunities to apply my skills and learn new technologies.")

st.title ("Skills ⚒️")
col1, col2, col3 = st.columns(3)

with col1:
    st.button('Python')
    st.button('Flask')
    
with col2:
    st.button("MySQL")
    st.button('Pandas')

with col3:
    st.button("Streamlit")
    st.button('NumPy')

jsonex = '{}'

st.title('Education')
