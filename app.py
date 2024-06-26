from tempfile import NamedTemporaryFile
import pysrt
import streamlit as st

def main():
    page = st.sidebar.radio("Navigation", ('View Subtitles', 'Create Subtitles'))

    if page == 'View Subtitles':
        view_subtitles_page()
    elif page == 'Create Subtitles':
        create_subtitles_page()

def view_subtitles_page():
    st.title('Subtitle Viewer using pysrt in Streamlit')

    uploaded_file = st.file_uploader("Choose a .srt file", type="srt")

    if uploaded_file is not None:
        with NamedTemporaryFile(suffix='.srt', delete=False) as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            st.info(f'Uploaded file: {uploaded_file.name}')

            # Open the subtitle file using pysrt
            subtitles = pysrt.open(temp_file.name, encoding='utf-8')

        display_subtitles(subtitles)

def display_subtitles(subtitles):
    st.header('Subtitle Text')

    # Display subtitles as text
    for idx, subtitle in enumerate(subtitles):
        st.subheader(f'Subtitle {idx + 1}')
        st.write(subtitle.text)

def create_subtitles_page():
    st.title('Create Subtitles')

    subtitle_text = st.text_area('Enter Subtitle Text')

    if st.button('Save as .srt file'):
        save_as_srt(subtitle_text)

def save_as_srt(subtitle_text):
    if subtitle_text.strip() == '':
        st.warning('Please enter some text to save.')
        return

    # Create a pysrt SubRipFile object
    subs = pysrt.SubRipFile()

    # Split text into individual subtitles
    lines = subtitle_text.strip().split('\n')
    for idx, line in enumerate(lines):
        subs.append(pysrt.SubRipItem(index=idx + 1, start=None, end=None, text=line))

    # Prompt user to save the file
    st.info('Choose where to save the .srt file.')
    with NamedTemporaryFile(suffix='.srt', delete=False) as temp_file:
        temp_file.write(subs.text.encode('utf-8'))

    st.success(f'Subtitle file saved as: {temp_file.name}')

if __name__ == '__main__':
    main()
