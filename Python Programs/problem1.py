class WhiteBox:
    def __init__(self, top, left, height, width):
        self.top = top
        self.left = left
        self.height = height
        self.width = width

def find_white_box(matrix):
    height = len(matrix)
    width = len(matrix[0])
    
    # Initialize variables to track white box properties
    top = left = height
    bottom = right = 0
    
    # Iterate over the matrix to find the boundaries of the white box
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 'w':
                top = min(top, i)
                left = min(left, j)
                bottom = max(bottom, i)
                right = max(right, j)
    
    # Calculate the height and width of the white box
    height = bottom - top + 1
    width = right - left + 1
    
    # Return the white box object
    return WhiteBox(top, left, height, width)

# Example matrix
matrix = [
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
]

# Find the white box in the matrix
white_box = find_white_box(matrix)

# Print the properties of the white box
print("Top:", white_box.top)
print("Left:", white_box.left)
print("Height:", white_box.height)
print("Width:", white_box.width)
