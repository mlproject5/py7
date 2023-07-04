import requests
import streamlit as st
import time
import pyshorteners

st.set_page_config(page_title='URL Shortener', page_icon='url.png', layout="centered", initial_sidebar_state="auto", menu_items=None)

def bitlyshort_1():
    def shorten_url(url):
        s = pyshorteners.Shortener(api_key='5789cb55e916f992f8c406e35cb773ea40d621c0')
        return s.bitly.short(url)

    def main():
        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 36px;'>Bitly</h1></center>",
            unsafe_allow_html=True)
        long_url = st.text_input("Enter the long URL", key="long_url_1")
        if st.button("Shorten URL"):
            if long_url:
                placeholder = st.empty()
                placeholder.info("Please wait...")
                shortened_url = shorten_url(long_url)
                time.sleep(3)
                placeholder.empty()
                st.success("Shortened URL Generated Successfully")
                st.text_input("Shortened URL", value=shortened_url)
            else:
                st.warning("Please enter a URL to shorten.")

    if __name__ == '__main__':
        main()


def tinyurl_2():
    def shorten_url(url):
        s = pyshorteners.Shortener()
        return s.tinyurl.short(url)

    def main():
        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 36px;'>TinyURL</h1></center>",
            unsafe_allow_html=True)
        long_url = st.text_input("Enter the long URL", key="long_url_2")
        if st.button("Shorten URL"):
            if long_url:
                placeholder = st.empty()
                placeholder.info("Please wait...")
                shortened_url = shorten_url(long_url)
                time.sleep(2)
                placeholder.empty()
                st.success("Shortened URL Generated Successfully")
                st.text_input("Shortened URL", value=shortened_url)
            else:
                st.warning("Please enter a URL to shorten.")

    if __name__ == '__main__':
        main()


def cuttly_3():
    def shorten_url(url):
        s = pyshorteners.Shortener(api_key='76ce1df69422cb3cca6a792ad29a2f9ca5f26')
        return s.cuttly.short(url)

    def main():
        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 36px;'>Cuttly</h1></center>",
            unsafe_allow_html=True)
        long_url = st.text_input("Enter the long URL", key="long_url_3")
        if st.button("Shorten URL"):
            if long_url:
                placeholder = st.empty()
                placeholder.info("Please wait...")
                shortened_url = shorten_url(long_url)
                time.sleep(2)
                placeholder.empty()
                st.success("Shortened URL Generated Successfully")
                st.text_input("Shortened URL", value=shortened_url)
            else:
                st.warning("Please enter a URL to shorten.")

    if __name__ == '__main__':
        main()


def google_4():
    def shorten_url(url):
        api_token = 'YOUR_BITLY_API_TOKEN'
        api_url = 'https://api-ssl.bitly.com/v4/shorten'

        headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json'
        }
        payload = {
            'long_url': url
        }
        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            shortened_url = response.json().get('id')
            return shortened_url
        else:
            return None

    def main():
        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 36px;'>Google</h1></center>",
            unsafe_allow_html=True)
        long_url = st.text_input("Enter the long URL", key="long_url_4")
        if st.button("Shorten URL"):
            if long_url:
                shortened_url = shorten_url(long_url)
                if shortened_url:
                    st.success(f"Shortened URL: {shortened_url}")
                else:
                    st.error("Failed to shorten URL. Please try again.")
                    st.warning("Maybe API is DEAD!")
            else:
                st.warning("Please enter a URL to shorten.")

    if __name__ == '__main__':
        main()


def rebrandly_5():
    def shorten_url(url):
        api_key = '1059e0f875fb4d84a234f428fece3813'
        api_url = 'https://api.rebrandly.com/v1/links'
        headers = {
            'Content-Type': 'application/json',
            'apikey': api_key
        }
        payload = {
            'destination': url
        }
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            shortened_url = response.json()['shortUrl']
            return shortened_url
        else:
            return None

    def main():
        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 600; font-size: 36px;'>Rebrandly</h1></center>",
            unsafe_allow_html=True)
        long_url = st.text_input("Enter the long URL", key="long_url_5")
        if st.button("Shorten URL"):
            if long_url:
                shortened_url = shorten_url(long_url)
                if shortened_url:
                    st.success("Shortened URL Generated Successfully")
                    st.text_input("Shortened URL", value=shortened_url)
                else:
                    st.error("Failed to shorten URL (Rebrandly). Please try again.")
            else:
                st.warning("Please enter a URL to shorten.")

    if __name__ == '__main__':
        main()

st.sidebar.markdown("""
            <style>
                .sidebar-text {
                    text-align: center;
                    font-weight: 600;
                    font-size: 32px;
                    font-family: 'Comic Sans MS', cursive;
                }
            </style>
            <p class="sidebar-text">Shortener</p>
            <br/>
        """, unsafe_allow_html=True)
st.sidebar.image("data:image/png;base64,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")
st.sidebar.title("Mystique URL Shortener")
sidebar_options = {
    "Bitly": bitlyshort_1,
    "TinyURL": tinyurl_2,
    "Cuttly": cuttly_3,
    "Google": google_4,
    "Rebrandly": rebrandly_5
}

selected_option = st.sidebar.radio("Select a URL shortener:", list(sidebar_options.keys()))

if "prev_option" not in st.session_state:
    st.session_state.prev_option = selected_option

if st.session_state.prev_option != selected_option:
    if selected_option == "Bitly":
        st.session_state.long_url_1 = ""
    elif selected_option == "TinyURL":
        st.session_state.long_url_2 = ""
    elif selected_option == "Cuttly":
        st.session_state.long_url_3 = ""
    elif selected_option == "Google":
        st.session_state.long_url_4 = ""
    elif selected_option == "Rebrandly":
        st.session_state.long_url_5 = ""

st.session_state.prev_option = selected_option
sidebar_options[selected_option]()
