import glfw

def create_win():
    if not glfw.init():
        return
    window = glfw.create_window(640, 480, "Archery Prediction", None, None)
    if not window:
        glfw.terminate()
        
        return
    glfw.make_context_current(window)
    while not glfw.window_should_close(window):
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()
    return window
