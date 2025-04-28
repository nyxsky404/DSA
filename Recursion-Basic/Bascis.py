# Recursion: when a function calls itself
#   Base Case: To avoid infinite recursion


# Infinite Recursion: ! Run at your own Risk !
    # def greet():
    #     print("Hello")
    #     greet()

    # greet()


# Head Recursion: The recursive call happens first, before any other operation (like printing).

count = 0

def func(count):
    if count == 4:
        return
    
    count +=1
    func(count)
    print("My Name")


func(count)


# Tail Recursion: The recursive call is the last thing the function does.

count = 0

def Your(count):
    if count == 4:
        return
    print("Your Name")
    count +=1
    Your(count)

Your(count)


# For Both:
    # Time Complexity: O(N)
    # Space Complexity: O(N)