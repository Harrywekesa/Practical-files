Programs like PyInstaller and cx_Freeze help turn Python scripts into executable programs that can be run by themselves on different platforms without the need to use Python to interpret the code.

Before we dive into writing a web application, let's get a very broad, generalized overview of what's about to happen. There are a lot of different pieces involved, and they all have to communicate with each other to function correctly: –
    First, your user makes a “request” for a particular webpage on your website (i.e., by typing a URL into a browser). 
    – This request gets received by the web server that hosts your website. 
    – The web server uses App Engine to look at the configuration file for your application. App Engine matches the user's request to a particular portion of your Python script. 
    – This Python code is called up by App Engine. When your code runs, it writes out a “response” webpage. 
    – App Engine delivers this response back to your user through the web server. 
    – The user can then view the web server's response (i.e., by displaying the resulting webpage in a browser).