INPUT=347991
reste = INPUT - 1
solution = 0
x = z = 0
max_right = max_up = max_left = max_down = 0
prev_move = "down"

while reste > 0 :
        if prev_move == "down":
            max_right += 1
            x, reste = func(x, reste, max_right)
            prev_move = "right"
        elif prev_move == "right":
            max_up += 1
            z, reste = func(z, reste, max_up)
            prev_move = "up"
        elif prev_move == "up":
            max_left -= 1
            x, reste = func(x, -reste, max_left)
            prev_move = "left"
        elif prev_move == "left":
            max_down -= 1
            z, reste = func(z, -reste, max_down)
            prev_move = "down"
    
solution = abs(x) + abs(z)
print(solution) # OUTPUT: 480
