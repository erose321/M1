
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg

class Artist:
    def __init__ (self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.pics = list(transition_matrix.keys())
        

    def get_next_pic(self, current_pic):
        return np.random.choice( 
            self.pics, p=[self.transition_matrix[current_pic][next_pic] 
            for next_pic in self.pics]
        )

    def compose_sequence(self, current_pic = "CollegeStreet.png", length = 6):
        sequence = []
        current_pic = current_pic
        while len(sequence) < length:
            next_pic = self.get_next_pic(current_pic)
            sequence.append(next_pic)
            current_pic = next_pic
        return sequence
    
    def make_sunset_grid(self, sequence, grid_size=(5, 4)):
        """ Draws the grid of ranomized sunset pics """
        fig, ax = plt.subplots(figsize = (8,6))
        ax.set_aspect('equal')
        ax.axis('off')

        rows, cols = grid_size 
        for idx, photo in enumerate(sequence):
            row = idx // cols
            col = idx % cols
            x, y = col, -row
            img = mpimg.imread(photo)
            ax.imshow(img, extent=[x, x+1, y-1, y])

        plt.xlim(0, cols)
        plt.ylim(-rows, 0)
        plt.show()

    

        
def main():

    transition_matrix = {
        "BrooklynBridge.png": {"BrooklynBridge.png": 0.3, "CollegeStreet.png": 0.2, "Brunswick.png": 0.2, "Hinsdale.png": 0.1, "Ocean.png": 0.1, "NY.png": 0.1},
        "CollegeStreet.png": {"BrooklynBridge.png": 0.1, "CollegeStreet.png": 0.4, "Brunswick.png": 0.2, "Hinsdale.png": 0.1, "Ocean.png": 0.1, "NY.png": 0.1},
        "Brunswick.png": {"BrooklynBridge.png": 0.2, "CollegeStreet.png": 0.2, "Brunswick.png": 0.3, "Hinsdale.png": 0.1, "Ocean.png": 0.1, "NY.png": 0.1},
        "Hinsdale.png": {"BrooklynBridge.png": 0.1, "CollegeStreet.png": 0.2, "Brunswick.png": 0.2, "Hinsdale.png": 0.3, "Ocean.png": 0.1, "NY.png": 0.1},
        "Ocean.png": {"BrooklynBridge.png": 0.1, "CollegeStreet.png": 0.1, "Brunswick.png": 0.2, "Hinsdale.png": 0.2, "Ocean.png": 0.3, "NY.png": 0.1},
        "NY.png": {"BrooklynBridge.png": 0.1, "CollegeStreet.png": 0.1, "Brunswick.png": 0.1, "Hinsdale.png": 0.2, "Ocean.png": 0.2, "NY.png": 0.3},
    }   

    artist = Artist(transition_matrix)
    seq = artist.compose_sequence(current_pic="CollegeStreet.png", length=6)

    print("Generated sequence:", seq)

    artist.make_sunset_grid(seq, grid_size=(3, 2))



if __name__ == "__main__":
    main()
    
