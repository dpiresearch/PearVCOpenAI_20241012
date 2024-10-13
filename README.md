# Laptop work history and real time api
Experiments in capturing history and exercising the beta openai realtime api

## Overview
Using the realtime console that was provided here https://github.com/openai/openai-realtime-console?tab=readme-ov-file#adding-and-using-tools
modify it and add functionality where you can ask about what you've been doing during the day.  There were a ton of problems to overcome and ultimately
no demo was shown, but learn a ton.

## Details
### Capturing history
History was captured by grabbing a screenshot of the laptop screen and sending it to GPT-4o to be summarized.
That summary was captured in a text file ( output.txt ) that was appended to every 10 seconds along with a timestamp.

Using this timestamp, the file can be uploaded to the site and you can ask what has been done in the past or get a summary
of the entire day given the descriptions given by the LLM throughout the day.

### Query via realtime console
I started modifying the realtime console to see if it can read the output.txt file.  Unfortunately that is not possible
as the script runs on the browser and it cannot access local files.  I then pivoted to uploading the file, but ran out of time 
before that could be done.

The realtime api cannot take text ( from a file like output.txt ) as payload - it only deals with audio, so the plan was 
to use function calling.  Using addTool in the code, I specified a function call that was executed if someone asked to 
summarize something.  The function call will invoke a chat completion api to summarize the output.txt.  However I ran into
issues trying to get the file contents to the function ( summarize_activity ). I got the upload button to work, but somehow that
information didn't get to the function call ( null result ).

In the end, I think it was still possible to get a demo out, but the openai tutorials didn't have python versions of the
realtime api that used websockets, so that'll have to be something I'll have to cook up myself.

## Execution

This starts the python script that takes a screenshot every 10 seconds and calls openai to get a summary of the image.  It then appends
that summary to output.txt along with a timestamp.
% python shootAndAsk.py

## Coding using cursor

Another goal to achieve was to use tools like Cursor and V0 to see what the state of the art of coding was like.  I used
Cursor for the majority of the work with the Realtime Console.  The conclusion is that it was useful 50% of the time, but
ultimately it got hung up on a few bugs that it couldn't resolve and I couldn't finish.  I wasn't a React person and the idea
was to see if the AI could pull me through, which it didn't
