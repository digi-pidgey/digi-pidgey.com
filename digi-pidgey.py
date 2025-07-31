# important notes for general coding and creating a website:
# enter "cmd" into file explore to open command prompt for that url
# ctr+c stops current session in a command prompt so you can enter additional commands
# enter 'cd' in command prompt followed by directory to det command prompt to that directory

# command for importing image presents using pillow
from PIL import Image
# img_digipidgey = Image.open("images/digipidgey.png")

# command for inserting images (requires loading presents from pillow)
# st.image(img_digipidgey, width=60)

# command to start a website using streamlit
import streamlit as st
import streamlit.components.v1 as components

# command to title a webpage
st.set_page_config(page_title="Digi-Pidgey", layout="wide", page_icon=":bird:")

#commands to hide the top margin/deploy buttons for streamlit
st.markdown("""
         <style>
         /* Hide the deploy button */
         .stDeployButton {
             visibility: hidden;
         }
         /* Hide the developer toolbar */
         div[data-testid="stToolbar"] {
             display: none !important;
         }
         /* Hide the status widget (running man) */
         div[data-testid="stStatusWidget"] {
             visibility: hidden !important;
         }
         </style>
         """, unsafe_allow_html=True)

st.markdown("""
<style>
header.stAppHeader {
    background-color: transparent;
}
section.stMain .block-container {
    padding-top: 0rem;
    z-index: 1;
}
</style>""", unsafe_allow_html=True)

# javascript player

st.markdown('<iframe src="//digi-pidgey.com/player/playerjs.html?file=//plrjs.com/x.mp4" type="text/html" width="640" height="360" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)

# command to create text / line spaces in streamlit
st.write("")



# command to insert an image, center it, and set size using HTML/CSS
st.markdown("""
<div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/digi-pidgey/images/refs/heads/main/digipidgey.png" 
    style="width: 60px; display: block; margin: 0 auto;">
</div>
""", unsafe_allow_html=True)

st.text("")
st.text("")
st.text("")

# command for centered text using HTML/CSS
st.markdown("<p style='text-align: center;'>Welcome to Digi-Pidgey.com</p>", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# command for centered text, custom font size, and font weight using HTML/CSS
st.markdown("<p style='text-align: center;font-size:40px;font-weight:bold;'>A website about nothing.</p>",
            unsafe_allow_html=True)

# command for reducing space lining size using HTML/CSS
st.markdown("""
    <style>
    p {
        line-height: .0;  /* Adjust this value as needed (e.g., 1.0 for single spacing) */
    }
    </style>
    """, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.markdown("<p style='text-align: center;'>⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄</p>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")

# command for links
st.markdown("<p style='text-align: center;font-size:14px;font-weight:bold;'"
            ">Info &nbsp &nbsp Baby Bird &nbsp &nbsp magickAI &nbsp &nbsp Support</p>"
            "", unsafe_allow_html=True)

# command to insert a footer for a streamlit website
# note: the <hr> after <div class=footer"> on the 108th line is the command for a divider
footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer"> <hr>  
<p><a style='display: block; text-align: center;font-size:11px' 
>Copyright: © 2025 Digi-Pidgey Productions. All rights reserved. 
<span style='font-weight: bold;'>Privacy.</a></p>  
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

# future notes:
# implement this song as background music https://www.youtube.com/watch?v=gXIZH3vc-_8
# don't forget to change webpage title icon to digipidgey img
