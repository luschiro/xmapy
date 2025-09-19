import streamlit as st

def main():
    
    # setup pages
    home = st.Page("home.py")
    resolution = st.Page("resolution.py")
    about = st.Page("about.py")

    # setup navigation and run
    pg = st.navigation([home, resolution,about])
    pg.run()

if __name__ == "__main__":
    main()
