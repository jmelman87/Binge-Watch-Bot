# Binge-Watch-Bot


**This Project Was Created In February 2018 via PYTHON**

--> Anyone with a favorite show can easily watch it for hours on end without stopping. 

--> The problem is that streaming services like Netflix, Hulu, Disney+, and others, all time out after a certain amount of time.

--> If one is watching TV on their computer but they don't want to have to press a button on the keyboard every once in a while to keep their show from stopping, they can use my simple solution that I made using Python.

I used the **pyautogui** python library in order to be able to control the mouse on the screen.

I also used the **time** library to create sleep delays that will wait a certain amount of time (in our case, 1 hour) to perform the wanted functions.

I used a simple while loop that will wait 3,600 seconds, or 1 hour, and then trigger a slight mouse movement that will be recognized as activity by the streaming service. The video will not ask "Are You Still Watching?" and eventually time out; the video will continue to play for as long as the script is running (it must be manually stopped by the user when they are done watching).
