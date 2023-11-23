import PySimpleGUI as sg
import requests
import threading

# Function to make API request and get password
def get_password(password_type: str) -> str:
    """
    Make an API request to get a password of the specified type.

    Parameters:
    - password_type (str): Type of password to request ('simple' or 'strong').

    Returns:
    - str: Generated password or error message.
    """
    """Make API request to get password of the specified type."""
    url = f"https://www.dinopass.com/password/{password_type}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Unable to fetch {password_type} password"

# Function to run API request in a separate thread
def run_api_request(password_type: str) -> None:
    """Run API request in a separate thread and update the GUI."""
    password = get_password(password_type)
    window.write_event_value('-THREAD-', f'{password}\n')

# Define the window's contents
layout = [
    [sg.Button('Simple password'), sg.Button('Strong password')],
    [sg.Text("Number of Passwords:"), sg.DropDown(values=list(range(1, 11)), default_value=5, key='-NUM_PASSWORDS-')],
    [sg.Text("Output:"), sg.Multiline(size=(None, 11), key='-OUTPUT-', disabled=True)],
    [sg.Button('Copy to Clipboard')],
]

# Create the window
window = sg.Window('DinoPass ', layout)

# Display and interact with the Window
while True:
    event, values = window.read()

    # Exit the program if the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Update the text area based on the button pressed
    if event in ('Simple password', 'Strong password'):
        # Get the password type from the pressed button
        password_type = event.split()[0].lower()

        # Get the number of passwords to generate
        num_passwords = int(values['-NUM_PASSWORDS-'])

        # Start separate threads for the API request
        threads = []
        for _ in range(num_passwords):
            thread = threading.Thread(target=run_api_request, args=(password_type,), daemon=True)
            threads.append(thread)
            thread.start()

    # Handle the result from the API request threads
    if event == '-THREAD-':
        generated_password = values[event]
        window['-OUTPUT-'].update(generated_password, append=True)

    # Copy to clipboard when the "Copy to Clipboard" button is pressed
    if event == 'Copy to Clipboard':
        output_text = values['-OUTPUT-']
        sg.clipboard_set(output_text)
        sg.popup('Text copied to clipboard!')

# Finish up by removing from the screen
window.close()


