Requirements and Required Modules to Run This Code:
--------------------------------------------------
1. Python 3.x: Ensure that Python is installed on your machine.
2. Pip: Python's package installer should be set up to install necessary modules.
3. Modules to install using `pip`:
   - `pyttsx3`: For text-to-speech functionality.
     - Install command: `pip install pyttsx3`
   - `speech_recognition`: For recognizing speech from the microphone.
     - Install command: `pip install SpeechRecognition`
   - `wikipedia`: For searching and retrieving Wikipedia articles.
     - Install command: `pip install wikipedia`
   - `smtplib`: For sending emails. (This module is part of Python’s standard library, so no need to install.)

4. Email Setup:
   - You’ll need to update the email and password inside the `sendEmail` function with your own email credentials. Make sure your email provider allows access for less secure apps, or enable access via an app-specific password for security.

What the Code Does:
-------------------
1. Text-to-Speech (TTS): 
   - Uses `pyttsx3` to make the computer speak specific text. The voice is initialized as 'sapi5' (Windows Speech API), and male voice is set.

2. Wishing Based on Time: 
   - The `wishMe()` function greets the user with a "Good Morning," "Good Afternoon," or "Good Evening," depending on the current time.

3. Voice Command Recognition:
   - The `takeCommand()` function listens to the user's voice through the microphone, converts the speech to text using `Google Speech Recognition`, and processes the command.

4. Email Sending:
   - The `sendEmail()` function allows the program to send an email through Gmail by taking the recipient’s email and the content as input. (You need to configure your Gmail credentials.)

5. Handling Various Commands:
   - The program listens for specific voice commands and performs tasks accordingly:
     - Wikipedia Search: Search for topics on Wikipedia and read a summary.
     - Open Websites: Opens specific websites like YouTube, Google, Stack Overflow, Amazon, VIT Bhopal's VTOP, etc., based on the voice command.
     - Play Music or Video: It can play music from a local directory or a specific episode from the video directory.
     - Tell the Time: It tells the current time.
     - Open Applications: It opens applications like Visual Studio Code or Python on your system.
     - Send Emails: You can instruct it to send emails via voice commands.

 Running the Code:

1. Install the required modules using `pip`.
2. Update the email credentials in the `sendEmail` function to your personal email details.
3. Run the Python script, and it will start by greeting you based on the time of the day.
4. It will then continuously listen for voice commands. Based on your command, it will perform the relevant task (search Wikipedia, open websites, play music, etc.).
