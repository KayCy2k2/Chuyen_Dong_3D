"""# Hàm vẽ các trục x, y, z
def draw_axes():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  # Màu đỏ cho trục x
    glVertex3f(-2.0, 0.0, 0.0)
    glVertex3f(2.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)  # Màu xanh lá cho trục y
    glVertex3f(0.0, -2.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)  # Màu xanh dương cho trục z
    glVertex3f(0.0, 0.0, -2.0)
    glVertex3f(0.0, 0.0, 2.0)
    glEnd()"""
    
"""def draw_axes():
    # Vẽ lưới trục tọa độ
    glLineWidth(1.0)
    glBegin(GL_LINES)
    for i in range(-20, 20, 2):
        glVertex3f(i, -20, 0.0)
        glVertex3f(i, 20, 0.0)
        glVertex3f(-20, i, 0.0)
        glVertex3f(20, i, 0.0)
    glEnd()"""
    
"""
def draw_sphere():
    for stack in range(stacks):
        stack_angle = (stack / stacks) * math.pi
        next_stack_angle = ((stack + 1) / stacks) * math.pi
        sin_stack = math.sin(stack_angle)
        cos_stack = math.cos(stack_angle)
        sin_next_stack = math.sin(next_stack_angle)
        cos_next_stack = math.cos(next_stack_angle)
        
        glBegin(GL_QUAD_STRIP)
        for j in range(-1, slices):
            lng = 2 * math.pi * float(j) / slices
            x = math.cos(lng)
            y = math.sin(lng)
            
            normal = np.array([x * cos_stack, y * cos_stack, sin_stack])
            vertex = np.array([x * cos_stack, y * cos_stack, sin_stack])
            glNormal3fv(normal)
            glVertex3fv(vertex)
            
            normal = np.array([x * cos_next_stack, y * cos_next_stack, sin_next_stack])
            vertex = np.array([x * cos_next_stack, y * cos_next_stack, sin_next_stack])
            glNormal3fv(normal)
            glVertex3fv(vertex)
            normal = np.array([x * cos_next_stack, y * cos_next_stack, -sin_next_stack])
            vertex = np.array([x * cos_next_stack, y * cos_next_stack, -sin_next_stack])
            glNormal3fv(normal)
            glVertex3fv(vertex)
        glEnd()"""
        """
        glBegin(GL_LINES)
        for slice in range(slices):
            slice_angle = (slice / slices) * 2 * math.pi
            x = radius * math.cos(slice_angle)
            y = radius * math.sin(slice_angle)
            
            glVertex3f(x * sin_stack, y * sin_stack, cos_stack)
            glVertex3f(x * sin_next_stack, y * sin_next_stack, cos_next_stack)
        glEnd()"""

"""def draw_sphere(color=(0.4, 1.0, 0.0)):  # Add color parameter

    # Set the desired color
    glColor3f(*color)

    # Vẽ nửa cầu trên
    for stack in range(stacks):
        stack_angle = math.pi * stack / stacks
        next_stack_angle = math.pi * (stack + 1) / stacks
        sin_stack = math.sin(stack_angle)
        cos_stack = math.cos(stack_angle)
        sin_next_stack = math.sin(next_stack_angle)
        cos_next_stack = math.cos(next_stack_angle)

        glBegin(GL_QUAD_STRIP)
        for slice in range(slices + 1):
            slice_angle = 2 * math.pi * slice / slices
            x = radius * math.cos(slice_angle)
            y = radius * math.sin(slice_angle)

            # Optimized calculation of normal vectors
            nx = x * cos_stack
            ny = y * cos_stack
            nz = sin_stack
            normal = (nx, ny, nz)

            glNormal3f(*normal)
            glVertex3f(x * cos_stack, y * cos_stack, sin_stack)
            glVertex3f(x * cos_next_stack, y * cos_next_stack, sin_next_stack)
        glEnd()

    # Vẽ nửa cầu dưới
    for stack in range(stacks):
        stack_angle = math.pi * stack / stacks
        next_stack_angle = math.pi * (stack + 1) / stacks
        sin_stack = math.sin(stack_angle)
        cos_stack = math.cos(stack_angle)
        sin_next_stack = math.sin(next_stack_angle)
        cos_next_stack = math.cos(next_stack_angle)

        glBegin(GL_QUAD_STRIP)
        for slice in range(slices + 1):
            slice_angle = 2 * math.pi * (slices - slice) / slices
            x = radius * math.cos(slice_angle)
            y = radius * math.sin(slice_angle)

            # Optimized calculation of normal vectors
            nx = x * cos_stack
            ny = y * cos_stack
            nz = sin_stack
            normal = (nx, ny, nz)

            glNormal3f(*normal)
            glVertex3f(x * cos_stack, y * cos_stack, -sin_stack)
            glVertex3f(x * cos_next_stack, y * cos_next_stack, -sin_next_stack)
        glEnd()"""
        
"""def draw_sphere():

    for half in (1, -1):  # Draw both hemispheres in a single loop
        for stack in range(stacks):
            stack_angle = math.pi * stack / stacks
            sin_stack = math.sin(stack_angle)
            cos_stack = math.cos(stack_angle)

            glBegin(GL_QUAD_STRIP)
            for slice in range(slices + 1):
                slice_angle = 2 * math.pi * slice / slices
                x = radius * math.cos(slice_angle)
                y = radius * math.sin(slice_angle)
                z = half * sin_stack

                normal = (x * cos_stack, y * cos_stack, z)
                glNormal3f(*normal)
                glVertex3f(x * cos_stack, y * cos_stack, z)
                glVertex3f(x, y, half * sin_stack)  # Simplified vertex calculation
            glEnd()"""

"""def draw_sphere():
    for stack in range(stacks):
        stack_angle = math.pi * stack / stacks
        next_stack_angle = math.pi * (stack + 1) / stacks
        sin_stack = math.sin(stack_angle)
        cos_stack = math.cos(stack_angle)
        sin_next_stack = math.sin(next_stack_angle)
        cos_next_stack = math.cos(next_stack_angle)

        glBegin(GL_QUAD_STRIP)
        for slice in range(slices + 1):
            slice_angle = 2 * math.pi * slice / slices
            slice_angle = 2 * math.pi * (slices - slice) / slices
            x = radius * math.cos(slice_angle)
            y = radius * math.sin(slice_angle)

            # Optimized calculation of normal vectors
            nx = x * cos_stack
            ny = y * cos_stack
            nz = sin_stack
            normal = (nx, ny, nz)

            glNormal3f(*normal)
            glVertex3f(x * cos_stack, y * cos_stack, sin_stack)
            glVertex3f(x * cos_stack, y * cos_stack, -sin_stack)
            glNormal3f(*normal)  # Reuse the same normal for the next vertex
            glVertex3f(x * cos_next_stack, y * cos_next_stack, sin_next_stack)
            glVertex3f(x * cos_next_stack, y * cos_next_stack, -sin_next_stack)
        glEnd()"""

"""# Vẽ khối cầu dạng lưới
def draw_sphere():
    for stack in range(stacks):
        # Tính toán các góc và giá trị sin, cos cho vòng tròn vĩ độ hiện tại
        stack_angle = (stack / stacks) * math.pi
        next_stack_angle = ((stack + 1) / stacks) * math.pi
        sin_stack = math.sin(stack_angle)
        cos_stack = math.cos(stack_angle)
        sin_next_stack = math.sin(next_stack_angle)
        cos_next_stack = math.cos(next_stack_angle)

        glBegin(GL_QUAD_STRIP)
        for j in range(stacks + 1):
            lng = 2 * math.pi * float(j - 1) / stacks
            x = math.cos(lng)
            y = math.sin(lng)
            glNormal3f(x * cos_stack, y * cos_stack, sin_stack)
            glVertex3f(x * cos_stack, y * cos_stack, sin_stack)
            glNormal3f(x * cos_next_stack, y * cos_next_stack, sin_next_stack)
            glVertex3f(x * cos_next_stack, y * cos_next_stack, sin_next_stack)
        glEnd()

        glBegin(GL_LINES)
        for slice in range(slices):
            # Tính toán tọa độ các điểm trên hai vòng tròn vĩ độ liên tiếp
            slice_angle = (slice / slices) * 2 * math.pi
            x = radius * math.cos(slice_angle)
            y = radius * math.sin(slice_angle)

            # Vẽ đường thẳng nối hai điểm tương ứng trên hai vòng tròn vĩ độ
            glVertex3f(x * sin_stack, y * sin_stack, cos_stack)
            glVertex3f(x * sin_next_stack, y * sin_next_stack, cos_next_stack)
        glEnd()"""
        
    """# Vẽ nửa cầu trên

    for stack in range(stacks):
        stack_angle = math.pi * stack / stacks
        next_stack_angle = math.pi * (stack + 1) / stacks
        sin_stack = math.sin(stack_angle)
        cos_stack = math.cos(stack_angle)
        sin_next_stack = math.sin(next_stack_angle)
        cos_next_stack = math.cos(next_stack_angle)

        glBegin(GL_QUAD_STRIP)
        for slice in range(slices + 1):
        slice_angle = 2 * math.pi * slice / slices
        x = radius * math.cos(slice_angle)
        y = radius * math.sin(slice_angle)

        # Optimized calculation of normal vectors
        nx = x * cos_stack
        ny = y * cos_stack
        nz = sin_stack
        normal = (nx, ny, nz)

        glNormal3f(*normal)
        glVertex3f(x * cos_stack, y * cos_stack, sin_stack)
        glNormal3f(*normal) # Reuse the same normal for the next vertex
        glVertex3f(x * cos_next_stack, y * cos_next_stack, sin_next_stack)
        glEnd()

    # Vẽ nửa cầu dưới

    for stack in range(stacks):
        stack_angle = math.pi * stack / stacks
        next_stack_angle = math.pi * (stack + 1) / stacks
        sin_stack = math.sin(stack_angle)
        cos_stack = math.cos(stack_angle)
        sin_next_stack = math.sin(next_stack_angle)
        cos_next_stack = math.cos(next_stack_angle)

        glBegin(GL_QUAD_STRIP)
        for slice in range(slices + 1):
        slice_angle = 2 * math.pi * (slices - slice) / slices
        x = radius * math.cos(slice_angle)
        y = radius * math.sin(slice_angle)

        # Optimized calculation of normal vectors
        nx = x * cos_stack
        ny = y * cos_stack
        nz = sin_stack
        normal = (nx, ny, nz)

        glNormal3f(*normal)
        glVertex3f(x * cos_stack, y * cos_stack, -sin_stack)
        glNormal3f(*normal) # Reuse the same normal for the next vertex
        glVertex3f(x * cos_next_stack, y * cos_next_stack, -sin_next_stack)
        glEnd()"""
