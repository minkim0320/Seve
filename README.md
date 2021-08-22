## SEVE (Scan Text Save Note)
A web application to save students' time so that they can focus on important things.
## Inspiration
With most classes moving online, many students are required to flip through different types of notes, whether it is electronic notes, pictures from lecture videos, or hand written notes that need to be typed up. Seve simplifies this procedure by making it possible to snap a quick picture and convert the text into electronic notes, and to save it for future use.
## What it does
Seve allows the uploading of images whether they are screenshots of lectures or quick snapped pics from hand written notes, and converts it to an electronic text form, and provides a notepad in which one can add more text on top. It works like a notepad, but allows the extraction of text from pictures which can be added. Users can save their work, and come back to it to write more notes.
## How we built it
We worked with Flask as the main backend framework creating RESTful endpoints, connecting to firebase for a realtime database, and using the Google Cloud Vision API to extract texts from images that get uploaded. The frontend was developed with HTML, CSS, and JavaScript (styled with Bootstrap 5).
## Challenges we ran into
The biggest challenge of this project was connecting all the various components. This includes connecting the database to match the requests from the frontend, and incorporating Google Vision API responses into the workflow.
## Accomplishments that we're proud of
We are proud of making a functional finished product that uses a variety of technologies that were new to us. 
## What we learned
We were able to learn the full process of web development and how to connect all the small pieces together to create a fully functioning website.
## What's next for Seve
Our next steps for SEVE would be to allow the users to upload multiple images which can be integrated directly to the notepad, and also to enable user authentication.
