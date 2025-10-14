import streamlit as st
from view import view  # assuming view.py is inside view/ folder

def main():
    view.app()  # call the function that runs the UI

if __name__ == "__main__":
    main()
