import streamlit as st
from functions import *
import streamlit_authenticator as stauth 
from dependencies import sign_up, fetch_users
st.set_page_config(page_title="IMDb Web APP ",layout="wide", page_icon="media/imdb_icon.png")
st.image('media/post.jpg')
st.markdown("---")
#st.title("Welcome")

sidebar=st.sidebar


try:
        users = fetch_users()
        emails = []
        usernames = []
        passwords = []

        for user in users:
            emails.append(user['key'])
            usernames.append(user['username'])
            passwords.append(user['password'])

        credentials = {'usernames': {}}
        for index in range(len(emails)):
            credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

        Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=10)

        email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

        info, info1 = st.columns(2)

        if not authentication_status:
            sign_up()

        if username:
            if username in usernames:
                if authentication_status:
                    # let User see app
                    st.sidebar.subheader(f'Welcome {username}')
                    sidebar.image('media/welcome.gif')
                    col1,col2=sidebar.columns(2)
                    Authenticator.logout('Log Out', 'sidebar')
                    display_movies()

                elif not authentication_status:
                    with info:
                        st.error('Incorrect Password or username')
                else:
                    with info:
                        st.warning('Please feed in your credentials')
            else:
                with info:
                    st.warning('Username does not exist, Please Sign up')


except:
        st.success('Refresh Page')


