#The text/plain is the way that our HTTP response lets a browser know to expect the body to contain plain text as opposed to HTML code, an image, or some other type of file.33
#Leaving a blank line after this header line is how we told the browser, “the header lines are over now; here comes the actual body to display.”
print("Content type : text/plain")
print(" ")
print("Congratulations It is a web app ")

#The body of the response is what we will actually see when we load the page in a browser. 
#In this case, it's just a simple string of text: “Congratulations, it's a web app!”