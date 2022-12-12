inputs = open('day6.txt')
inputs = inputs.read().strip()

def find_marker(inputs, length):

    buffer = []

    for count, value in enumerate(inputs):

        buffer.append(value)

        if value not in buffer[0:-1]:
            if len(buffer) == length:
                print(count+1)
                print(buffer, "\n")
                break
        else:
            while buffer[0] != value:
                buffer.pop(0)
            buffer.pop(0)

# Main Code
find_marker(inputs, 4)
find_marker(inputs, 14)

