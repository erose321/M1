# 
Title: Markov Sunset Artist 

For this project, I created an "Art project" that uses a Markov chain to generate a grid of Sunset Pics I have taken over the years. Using a transition matrix like we did in class with making a song, the program selects which images should follow another, allowing the output grid to vary each time it is run. 

The "Artist" class includes methods for generating a sequence of images (compose_sequence) and displaying them in a visual grid (make_sunset_grid). 

By running python3 shapeArt.py in the terminal, the program will output different variations of these sunset images in a 3x2 grid format - note that this will appear in a pop-up window. 

Personal Meaning: Being on the golf team at Bowdoin, we get to see some awesome sunsets towards the end of our practices, which is what inspired me to make this. Additionally, I love to take pictures in general, especially of pretty skies that I see along the way. Because it would take forever to make the transition matrix with ALL of my sunset photos, I had to keep it to only 6 of my favorite recent photos for purposes of this project

Challenges: This project challenged me in a few ways. For one, I had to think about probability in a new computationally creative way. Instead of being mathmatical, it directly shaped the artwork that my program produced. I also had to learn how to use Matplotlib which definetly took some extra time. There were also some issues with the layout of my photos on the grid, and having to debug that was a bit of a challenge. I think that these were important challenges because they forced me to integrate math, programming, and design into one computationally creative system. It showed me that computer science is just as much about producing personally meaningful outputs as it is about logisitally solving problems. 


Creativity: I believe that my system is creative, and could be even more creative with more time and learning. Producing a randomized grid of sunset pictures that I have personally taken could be very visually appealing to a user for many ways. Another reason this is creative is because the combination of randomness, probability, and my images means that each run produces a new and unexpected visual. It also pushes me to think about how changing those probabilities could create different visual outcomes, and how you could really play around with that. 

Moving forward, I want to expand the transition matricies with more nuanced probabilities to capture different artistic “styles.” It would also be interesting to learn the psychology behind this and what layouts are more visually appealing for a viewer. I also want to integrate more image manipulation - filters, etc to enhance the creativity. Note: My photos came out a little grey looking on the grids and I cannot seem to figure out why!

Credits: 
Libs -> NumPy, Matplotlib