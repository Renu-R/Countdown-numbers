# Countdown-numbers
An application to play the numbers round of the countdown game show.

In the game a randomly generated 3 digit target number is to be constructed from 6 randomly generated numbers using the basic math operations. Each number can only be used once and numbers may remain unused. A solver algorithm uses brute force recursion trying every permutation of numbers and operators to find a mathematical expression using the input numbers that equals the target number.

Then using PyQt5, I designed a gui where upon pressing the start button, the target and numbers are randomly generated and displayed. The countdown theme tune start playing once the numbers are displayed and after 30 seconds, when the music ends, the solution to the problem is displayed and the start button can be pressed again. Finally, I packaged the project into a .exe file so that the application can be shared by sharing the dist file.
