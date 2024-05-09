import sys
from presentation.main_window import load_window

def main():
    load_window()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")