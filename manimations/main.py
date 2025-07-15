from manim import *
from manim_slides.slide import Slide

class Example(Slide):
    def construct(self):
        #Slide 1: Title slide
        # self.slide1()

        #Slide 2: Show the map and the problem
        # self.slide2()
        
        #Slide 3: Grid-based map representation
        # self.slide3()
        
        #Slide 4: Vector-based map representation  
        # self.slide4()
        
        #Slide 5: Shortest path properties in simple polygons
        # self.slide5()
        
        #Slide 6: Funnel technique
        # self.slide6()
        
        #Slide 7: Funnel algorithm step by step
        # self.slide7()

        #Slide 8: Funnel algorithm in real world
        self.slide8()

        #Slide9: StepByStep in real world
        self.slide9()
    
    def slide1(self):
        #Slide 1: Title slide
        title = Text("Kỹ thuật Funnel", font_size=48, weight=BOLD)
        subtitle = Text("Trong Bài Toán Tìm Đường Đi Ngắn Nhất", font_size=36)
        
        authors = Text("Ha Minh Truong and Le Minh Phuc", font_size=24)
        institute = Text("MARS", font_size=20)
        date = Text("07/16/2025", font_size=20)
        
        # Position elements
        title.move_to(UP * 1.5)
        subtitle.next_to(title, DOWN, buff=0.5)
        authors.next_to(subtitle, DOWN, buff=1)
        institute.next_to(authors, DOWN, buff=0.3)
        date.next_to(institute, DOWN, buff=0.3)
        
        # Animate title slide
        for i in (title, subtitle, authors, institute, date):
            self.play(Write(i))
        self.wait(0.5)
        self.next_slide()
        self.play(FadeOut(title, subtitle, authors, institute, date))
        
        # Optional: Pause for a moment before moving on
        # self.wait(1)

    def slide2(self):
        self.img = ImageMobject("map/map.png")
        self.play(FadeIn(self.img))
        self.next_slide()

        self.play(FadeOut(self.img))
    
    def slide3(self):
        # Title for this slide
        title = Text("Grid-based Map", font_size=36, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        
        # Show the original image scaled to fit better
        self.img = ImageMobject("map/map.png").scale(0.6)   
        self.img.move_to(LEFT * 1.5)
        
        # Create grid overlay on the image
        grid_rows = 12
        grid_cols = 16
        
        # Calculate grid dimensions based on image size
        img_width = self.img.width
        img_height = self.img.height
        cell_width = img_width / grid_cols
        cell_height = img_height / grid_rows
        
        # Create grid lines
        grid_lines = VGroup()
        
        # Vertical lines
        for i in range(grid_cols + 1):
            x_pos = self.img.get_left()[0] + i * cell_width
            line = Line(
                start=(x_pos, self.img.get_top()[1], 0),
                end=(x_pos, self.img.get_bottom()[1], 0),
                color=WHITE,
                stroke_width=2
            )
            grid_lines.add(line)
        
        # Horizontal lines
        for i in range(grid_rows + 1):
            y_pos = self.img.get_top()[1] - i * cell_height
            line = Line(
                start=(self.img.get_left()[0], y_pos, 0),
                end=(self.img.get_right()[0], y_pos, 0),
                color=WHITE,
                stroke_width=2
            )
            grid_lines.add(line)
        
                # Create grid values overlay using terrain map
        grid_values = VGroup()
        
        # Define terrain map based on the aerial image
        # 0 = water/river, 1 = ground/walkable
        terrain_map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
        ]
        
        # Create overlay for all cells in the terrain map
        for row in range(len(terrain_map)):
            for col in range(len(terrain_map[row])):
                if row < grid_rows and col < grid_cols:
                    # Get value from terrain map
                    value = terrain_map[row][col]
                    
                    # Calculate cell center position
                    cell_x = self.img.get_left()[0] + (col + 0.5) * cell_width
                    cell_y = self.img.get_top()[1] - (row + 0.5) * cell_height
                    
                    # Create colored overlay
                    color = GREEN if value == 1 else BLUE
                    overlay = Rectangle(
                        width=cell_width * 0.8,
                        height=cell_height * 0.8,
                        fill_color=color,
                        fill_opacity=0.6,
                        stroke_color=WHITE,
                        stroke_width=1
                    )
                    overlay.move_to((cell_x, cell_y, 0))
                    
                    # Add value text
                    value_text = Text(str(value), font_size=12, color=WHITE, weight=BOLD)
                    value_text.move_to((cell_x, cell_y, 0))
                    
                    grid_values.add(overlay, value_text)
        
        # Text content
        storage_title = Text("Grid Resolution & Storage:", font_size=16, weight=BOLD, color=WHITE)
        
        # Calculate storage for this grid
        grid_size = len(terrain_map) * len(terrain_map[0])  # 12 x 16 = 192 cells
        bytes_per_cell = 12  # int x (4 bytes) + int y (4 bytes) + int value (4 bytes) = 12 bytes
        storage_per_cell = Text(f"Store (x, y, value) → {bytes_per_cell} bytes per cell", font_size=12, color=WHITE)
        current_grid = Text(f"Current grid: {grid_size} cells → {grid_size * bytes_per_cell} bytes", font_size=12, color=WHITE)
        
        # Real world application
        real_world_title = Text("In real world:", font_size=12, weight=BOLD, color=WHITE)
        resolution_info = Text("Outdoor forest: 0.5-1m per cell", font_size=12, color=YELLOW)
        example_area = Text("1km² area → 1000x1000 = 1M cells", font_size=12, color=YELLOW)
        
        # Calculate for 100km² forest
        forest_100km = 100 * 1000 * 1000  # 100km² = 100,000,000 m²
        cells_100km = forest_100km  # 1 cell per m²
        bytes_100km = cells_100km * bytes_per_cell
        gb_100km = bytes_100km / (1024 * 1024 * 1024)  # Convert to GB
        forest_storage = Text(f"Forest 100km² → {gb_100km:.1f}GB memory", font_size=12, color=YELLOW)

        # Storage and Resolution information in red box
        storage_info = VGroup()
        storage_info.add(storage_title)
        storage_info.add(storage_per_cell.next_to(storage_title, DOWN, buff=0.2, aligned_edge=LEFT))
        storage_info.add(current_grid.next_to(storage_per_cell, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.add(real_world_title.next_to(current_grid, DOWN, buff=0.3, aligned_edge=LEFT))
        storage_info.add(resolution_info.next_to(real_world_title, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.add(example_area.next_to(resolution_info, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.add(forest_storage.next_to(example_area, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.move_to(self.img.get_right() + RIGHT * 3)
        
        # Legend
        legend = VGroup()
        legend_title = Text("Legend:", font_size=20, weight=BOLD)
        
        walkable_square = Square(side_length=0.2, fill_color=GREEN, fill_opacity=0.6, stroke_color=WHITE)
        walkable_text = Text("1 = Ground", font_size=16)
        walkable_item = VGroup(walkable_square, walkable_text.next_to(walkable_square, RIGHT, buff=0.2))
        
        water_square = Square(side_length=0.2, fill_color=BLUE, fill_opacity=0.6, stroke_color=WHITE)
        water_text = Text("0 = Water", font_size=16)
        water_item = VGroup(water_square, water_text.next_to(water_square, RIGHT, buff=0.2))
        
        legend.add(legend_title)
        legend.add(walkable_item.next_to(legend_title, DOWN, buff=0.2, aligned_edge=LEFT))
        legend.add(water_item.next_to(walkable_item, DOWN, buff=0.1, aligned_edge=LEFT))
        legend.move_to(self.img.get_bottom() + DOWN * 1)
        
        # Animate the slide
        self.play(Write(title))
        self.next_slide()
        
        self.play(FadeIn(self.img))
        self.next_slide()
        
        self.play(Create(grid_lines))
        self.next_slide()
        
        self.play(FadeIn(grid_values))
        self.next_slide()
        
        self.play(FadeIn(legend))
        self.next_slide()
        
        self.play(FadeIn(storage_info))
        self.next_slide()
        
        # Clear everything
        self.play(FadeOut(title, self.img, grid_lines, grid_values, legend, storage_info))

    def slide4(self):
        # Title for this slide
        title = Text("Vector-based Map", font_size=36, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        
        # Show the original image scaled to fit better
        self.img = ImageMobject("map/map.png").scale(0.6)   
        self.img.move_to(LEFT * 1.5)
        
        # Create vector representation from map.txt data
        # Use bottom-left corner of image as origin (0,0)
        scale_factor = 0.99
        origin_x = self.img.get_left()[0]  # Left edge of image = x=0
        origin_y = self.img.get_bottom()[1]  # Bottom edge of image = y=0
        
        # Define key points from the LaTeX file (scaled and positioned)
        vector_points = VGroup()
        vector_lines = VGroup()
        
        # All points extracted from map/map.txt file
        key_points = [
            (0.3347507967871943, 3.485183600744722, "A"),
            (0.050904694188400594, 3.6085949497007195, "B"),
            (0.9641486764627804, 4.275016234063106, "C"),
            (2.5684962128907447, 4.595885741348698, "D"),
            (3.5187635998519236, 3.3617722517887247, "E"),
            (3.9630444560935136, 3.5715715450139203, "F"),
            (3.3459877113135272, 4.0035112663599115, "G"),
            (3.8272919722419165, 4.5218389319751005, "H"),
            (4.357960772752705, 4.447792122601502, "I"),
            (4.432007582126303, 4.2379928293763065, "J"),
            (5.431639508669881, 4.756320494991495, "K"),
            (7.043225809633118, 4.749466919462989, "L"),
            (6.0264503048242775, 3.6425973825824793, "M"),
            (6.296732401039286, 2.8446216699476925, "N"),
            (7.583790002063135, 4.517796551278697, "O"),
            (8.072871890452197, 4.221773303043212, "P"),
            (8.150095346513627, 3.629726806572241, "Q"),
            (8.510471474800305, 2.9861980060603166, "R"),
            (8.631955589793407, 2.8796705978210464, "S"),
            (8.644201190827998, 2.6898637817848825, "T"),
            (8.713164032907233, 2.6637460985435673, "U"),
            (8.668438722601804, 2.340347700950471, "V"),
            (8.080128871661172, 2.1786485021539224, "W"),
            (6.976866217449777, 0.9130917744833986, "Z"),
            (6.73721872009328, 0.9062447031303559, "A₁"),
            (6.73721872009328, 1.7895169076728765, "B₁"),
            (5.806017016079461, 2.583777184625841, "C₁"),
            (5.669075589018606, 2.4947652570362844, "D₁"),
            (4.683097314180445, 3.26848431993012, "E₁"),
            (3.484446850448112, 2.7444580422308507, "F₁"),
            (3.1338312795565395, 2.0522170432910776, "G₁"),
            (3.1620538406947065, 1.8886049360312143, "H₁"),
            (3.0259495654360555, 1.6926113295561307, "I₁"),
            (2.7181599984970997, 1.6755358917763574, "J₁"),
            (2.5849918458378176, 1.7998261675916907, "K₁"),
            (2.702304423074604, 2.0612071861344514, "L₁"),
            (2.2887578522794154, 2.5736453282067506, "M₁"),
            (1.8122802815806116, 2.7444580422308507, "N₁"),
            (1.4257041393155443, 2.4118227570260244, "O₁"),
            (0.9222561400866195, 2.3399016142790354, "P₁"),
            (0.643561711942036, 2.501724185459761, "Q₁"),
            (0.7334631403757726, 2.8523397563513346, "R₁"),
            (1.0481181398938506, 3.08608347027905, "S₁"),
            (1.3178224251950605, 3.805294897748944, "T₁"),
            (0.9042758543998721, 4.128940040110396, "U₁"),
        ]
        
        # Create points
        for x, y, label in key_points:
            # Scale and position the point relative to bottom-left origin
            point_x = origin_x + x * scale_factor
            point_y = origin_y + y * scale_factor
            
            # Create point
            point = Dot(point=(point_x, point_y, 0), color=RED, radius=0.05)
            point_label = Text(label, font_size=10, color=WHITE)
            point_label.next_to(point, UP, buff=0.1)
            
            vector_points.add(point, point_label)
        
        # Create lines following the exact path from map.txt \psline commands
        # Each tuple represents (start_point_index, end_point_index) based on the LaTeX file
        line_connections = [
            # Main river path from \psline commands in map.txt
            (0, 1),   # A -> B
            (1, 2),   # B -> C  
            (2, 3),   # C -> D
            (3, 4),   # D -> E
            (4, 5),   # E -> F
            (5, 6),   # F -> G
            (6, 7),   # G -> H
            (7, 8),   # H -> I
            (8, 9),   # I -> J
            (9, 10),  # J -> K
            (10, 11), # K -> L
            (11, 12), # L -> M
            (12, 13), # M -> N
            (13, 14), # N -> O
            (14, 15), # O -> P
            (15, 16), # P -> Q
            (16, 17), # Q -> R
            (17, 18), # R -> S
            (18, 19), # S -> T
            (19, 20), # T -> U
            (20, 21), # U -> V
            (21, 22), # V -> W
            (22, 23), # W -> Z
            (23, 24), # Z -> A₁
            (24, 25), # A₁ -> B₁
            (25, 26), # B₁ -> C₁
            (26, 27), # C₁ -> D₁
            (27, 28), # D₁ -> E₁
            (28, 29), # E₁ -> F₁
            (29, 30), # F₁ -> G₁
            (30, 31), # G₁ -> H₁
            (31, 32), # H₁ -> I₁
            (32, 33), # I₁ -> J₁
            (33, 34), # J₁ -> K₁
            (34, 35), # K₁ -> L₁
            (35, 36), # L₁ -> M₁
            (36, 37), # M₁ -> N₁
            (37, 38), # N₁ -> O₁
            (38, 39), # O₁ -> P₁
            (39, 40), # P₁ -> Q₁
            (40, 41), # Q₁ -> R₁
            (41, 42), # R₁ -> S₁
            (42, 43), # S₁ -> T₁
            (43, 44), # T₁ -> U₁
            (44, 0),  # U₁ -> A (close the polygon)
        ]
        
        for start_idx, end_idx in line_connections:
            if start_idx < len(key_points) and end_idx < len(key_points):
                start_x = origin_x + key_points[start_idx][0] * scale_factor
                start_y = origin_y + key_points[start_idx][1] * scale_factor
                end_x = origin_x + key_points[end_idx][0] * scale_factor
                end_y = origin_y + key_points[end_idx][1] * scale_factor
                
                line = Line(
                    start=(start_x, start_y, 0),
                    end=(end_x, end_y, 0),
                    color=BLUE,
                    stroke_width=3
                )
                vector_lines.add(line)
        
        # Storage and Comparison information for vector map
        storage_info = VGroup()
        storage_title = Text("Vector vs Grid Comparison:", font_size=16, weight=BOLD, color=WHITE)
        
        # Calculate storage for vector representation
        num_points = len(key_points)
        bytes_per_point = 16  # float x (8 bytes) + float y (8 bytes) = 16 bytes for double precision
        num_lines = len(line_connections)
        bytes_per_line = 8   # 2 point indices (4 bytes each) = 8 bytes
        vector_total = num_points * bytes_per_point + num_lines * bytes_per_line
        
        # Vector storage info
        storage_per_point = Text(f"Store point (x, y) → {bytes_per_point} bytes", font_size=12, color=WHITE)
        total_vector = Text(f"Vector total: {num_points} points + {num_lines} lines = {vector_total} bytes", font_size=12, color=WHITE)
        
        # Comparison with grid from slide3
        comparison_title = Text("So sánh với Grid:", font_size=12, weight=BOLD, color=WHITE)
        grid_comparison = Text("Grid (12×16): 2,304 bytes", font_size=12, color=RED)
        vector_comparison = Text(f"Vector: {vector_total} bytes", font_size=12, color=GREEN)
        efficiency = Text(f"Vector nhỏ hơn {2304/vector_total:.1f}x lần", font_size=12, color=YELLOW)
        
        # Real world application
        real_world_title = Text("Trong thực tế:", font_size=12, weight=BOLD, color=WHITE)
        precision_info = Text("Vector: Infinite precision", font_size=12, color=YELLOW)
        grid_real = Text("Grid 100km²: 1.1GB memory", font_size=12, color=RED)
        vector_real = Text("Vector 100km²: Same ~1KB", font_size=12, color=GREEN)
        
        storage_info.add(storage_title)
        storage_info.add(storage_per_point.next_to(storage_title, DOWN, buff=0.2, aligned_edge=LEFT))
        storage_info.add(total_vector.next_to(storage_per_point, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.add(comparison_title.next_to(total_vector, DOWN, buff=0.2, aligned_edge=LEFT))
        storage_info.add(grid_comparison.next_to(comparison_title, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.add(vector_comparison.next_to(grid_comparison, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.add(efficiency.next_to(vector_comparison, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.add(real_world_title.next_to(efficiency, DOWN, buff=0.2, aligned_edge=LEFT))
        storage_info.add(precision_info.next_to(real_world_title, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.add(grid_real.next_to(precision_info, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.add(vector_real.next_to(grid_real, DOWN, buff=0.1, aligned_edge=LEFT))
        storage_info.move_to(self.img.get_right() + RIGHT * 2.3)
        
        # Legend
        legend = VGroup()
        legend_title = Text("Legend:", font_size=20, weight=BOLD)
        
        point_dot = Dot(color=RED, radius=0.05)
        point_text = Text("Points (x, y)", font_size=16)
        point_item = VGroup(point_dot, point_text.next_to(point_dot, RIGHT, buff=0.2))
        
        line_sample = Line(start=ORIGIN, end=RIGHT*0.4, color=BLUE, stroke_width=3)
        line_text = Text("Vector Lines", font_size=16)
        line_item = VGroup(line_sample, line_text.next_to(line_sample, RIGHT, buff=0.2))
        
        legend.add(legend_title)
        legend.add(point_item.next_to(legend_title, DOWN, buff=0.2, aligned_edge=LEFT))
        legend.add(line_item.next_to(point_item, DOWN, buff=0.1, aligned_edge=LEFT))
        legend.move_to(self.img.get_bottom() + DOWN * 1)
        
        # Animate the slide
        self.play(Write(title))
        self.next_slide()
        
        self.play(FadeIn(self.img))
        self.next_slide()
        
        self.play(Create(vector_points))
        self.next_slide()
        
        self.play(Create(vector_lines))
        self.next_slide()
        
        self.play(FadeIn(legend))
        self.next_slide()
        
        self.play(FadeIn(storage_info))
        self.next_slide()
        
        # Clear everything
        self.play(FadeOut(title, self.img, vector_points, vector_lines, legend, storage_info))

    def slide5(self):
        # Title for this slide
        title = Text("Shortest Path Properties in Simple Polygons", font_size=30, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        
        # Show the original image scaled to fit better
        self.img = ImageMobject("map/map.png").scale(0.6)   
        self.img.move_to(LEFT * 1.5)
        
        # Create vector representation from slide4 data
        scale_factor = 1.2
        origin_x = self.img.get_left()[0] - 1
        origin_y = self.img.get_bottom()[1] -1
        
        # All points from slide4
        key_points = [
            (0.3347507967871943, 3.485183600744722, "A"),
            (0.050904694188400594, 3.6085949497007195, "B"),
            (0.9641486764627804, 4.275016234063106, "C"),
            (2.5684962128907447, 4.595885741348698, "D"),
            (3.5187635998519236, 3.3617722517887247, "E"),
            (3.9630444560935136, 3.5715715450139203, "F"),
            (3.3459877113135272, 4.0035112663599115, "G"),
            (3.8272919722419165, 4.5218389319751005, "H"),
            (4.357960772752705, 4.447792122601502, "I"),
            (4.432007582126303, 4.2379928293763065, "J"),
            (5.431639508669881, 4.756320494991495, "K"),
            (7.043225809633118, 4.749466919462989, "L"),
            (6.0264503048242775, 3.6425973825824793, "M"),
            (6.296732401039286, 2.8446216699476925, "N"),
            (7.583790002063135, 4.517796551278697, "O"),
            (8.072871890452197, 4.221773303043212, "P"),
            (8.150095346513627, 3.629726806572241, "Q"),
            (8.510471474800305, 2.9861980060603166, "R"),
            (8.631955589793407, 2.8796705978210464, "S"),
            (8.644201190827998, 2.6898637817848825, "T"),
            (8.713164032907233, 2.6637460985435673, "U"),
            (8.668438722601804, 2.340347700950471, "V"),
            (8.080128871661172, 2.1786485021539224, "W"),
            (6.976866217449777, 0.9130917744833986, "Z"),
            (6.73721872009328, 0.9062447031303559, "A₁"),
            (6.73721872009328, 1.7895169076728765, "B₁"),
            (5.806017016079461, 2.583777184625841, "C₁"),
            (5.669075589018606, 2.4947652570362844, "D₁"),
            (4.683097314180445, 3.26848431993012, "E₁"),
            (3.484446850448112, 2.7444580422308507, "F₁"),
            (3.1338312795565395, 2.0522170432910776, "G₁"),
            (3.1620538406947065, 1.8886049360312143, "H₁"),
            (3.0259495654360555, 1.6926113295561307, "I₁"),
            (2.7181599984970997, 1.6755358917763574, "J₁"),
            (2.5849918458378176, 1.7998261675916907, "K₁"),
            (2.702304423074604, 2.0612071861344514, "L₁"),
            (2.2887578522794154, 2.5736453282067506, "M₁"),
            (1.8122802815806116, 2.7444580422308507, "N₁"),
            (1.4257041393155443, 2.4118227570260244, "O₁"),
            (0.9222561400866195, 2.3399016142790354, "P₁"),
            (0.643561711942036, 2.501724185459761, "Q₁"),
            (0.7334631403757726, 2.8523397563513346, "R₁"),
            (1.0481181398938506, 3.08608347027905, "S₁"),
            (1.3178224251950605, 3.805294897748944, "T₁"),
            (0.9042758543998721, 4.128940040110396, "U₁"),
        ]
        
        # Helper function to find point index by label
        def find_point_index(label):
            for i, (x, y, point_label) in enumerate(key_points):
                if point_label == label:
                    return i
            return None
        
        # Helper function to get point coordinates
        def get_point_coords(label):
            idx = find_point_index(label)
            if idx is not None:
                x, y, _ = key_points[idx]
                return (origin_x + x * scale_factor, origin_y + y * scale_factor, 0)
            return None
        
        # Create polygon from vector lines
        polygon_lines = VGroup()
        line_connections = [
            (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10),
            (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18),
            (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26),
            (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (31, 32), (32, 33), (33, 34),
            (34, 35), (35, 36), (36, 37), (37, 38), (38, 39), (39, 40), (40, 41), (41, 42),
            (42, 43), (43, 44), (44, 0)
        ]
        
        for start_idx, end_idx in line_connections:
            start_x = origin_x + key_points[start_idx][0] * scale_factor
            start_y = origin_y + key_points[start_idx][1] * scale_factor
            end_x = origin_x + key_points[end_idx][0] * scale_factor
            end_y = origin_y + key_points[end_idx][1] * scale_factor
            
            line = Line(
                start=(start_x, start_y, 0),
                end=(end_x, end_y, 0),
                color=BLUE,
                stroke_width=2
            )
            polygon_lines.add(line)
        
        # Create key points for shortest path examples
        key_vertices = VGroup()
        example_labels = ["T₁", "E", "E₁", "F₁", "D₁", "A", "A₁"]
        for label in example_labels:
            coords = get_point_coords(label)
            if coords:
                point = Dot(point=coords, color=RED, radius=0.08)
                point_label = Text(label, font_size=12, color=WHITE, weight=BOLD)
                point_label.next_to(point, UP, buff=0.1)
                key_vertices.add(point, point_label)
        
        # Property explanation
        property_text = VGroup()
        prop_title = Text("Property:", font_size=20, weight=BOLD, color=YELLOW)
        prop_desc = Text("Shortest path is a\nsequence of line\nsegments with vertices\nat polygon vertices", 
                        font_size=20, color=WHITE)
        property_text.add(prop_title)
        property_text.add(prop_desc.next_to(prop_title, DOWN, buff=0.2, aligned_edge=LEFT))
        property_text.move_to(self.img.get_top() + RIGHT * 6.8 + DOWN * 0.5)
        
        # Animate the slide
        self.play(Write(title))
        self.next_slide()
        
        self.play(Create(polygon_lines))
        self.next_slide()
        
        self.play(FadeIn(property_text))
        self.next_slide()
        
        self.play(Create(key_vertices))
        self.next_slide()
        
        # Helper function to create angle using Manim built-in Angle class
        def create_manim_angle(vertex, point1, point2, angle_deg, radius=0.4, color=YELLOW):
            """Create angle using Manim's built-in Angle class"""
            # Create lines from vertex to the two points
            line1 = Line(start=vertex, end=point1)
            line2 = Line(start=vertex, end=point2)
            
            # For reflex angles (>180°), we want to draw the "other" angle (the smaller one)
            # but show the reflex angle value. This creates the correct visual.
            use_other_angle = False
            
            # Create Manim Angle object
            angle = Angle(line1, line2, radius=radius, color=color, 
                         stroke_width=3, other_angle=use_other_angle)
            
            return angle
        
        # Example 1: T₁ to E (direct edge)
        example1_title = Text("Example 1: T₁ → E", font_size=20, weight=BOLD, color=GREEN)
        example1_desc = Text("Shortest path: T₁E (1 edge)", font_size=16, color=WHITE)
        example1_text = VGroup(example1_title, example1_desc.next_to(example1_title, DOWN, buff=0.1, aligned_edge=LEFT))
        example1_text.move_to(property_text.get_center() + DOWN * 1.5)
        
        # Draw path T₁ → E
        t1_coords = get_point_coords("T₁")
        e_coords = get_point_coords("E")
        if t1_coords and e_coords:
            path1 = Line(start=t1_coords, end=e_coords, color=GREEN, stroke_width=4)
        
        self.play(FadeIn(example1_text))
        if t1_coords and e_coords:
            self.play(Create(path1))
        self.next_slide()
        
        # Example 2: T₁ to E₁ (via E) - Analyze angle T₁EE₁
        example2_title = Text("Example 2: T₁ → E₁", font_size=20, weight=BOLD, color=ORANGE)
        example2_desc = Text("Check angle T₁EE₁", font_size=16, color=WHITE)
        example2_text = VGroup(example2_title, example2_desc.next_to(example2_title, DOWN, buff=0.1, aligned_edge=LEFT))
        example2_text.move_to(example1_text.get_center() + DOWN * 0.8)
        
        # Draw path T₁ → E → E₁ and show angle
        e1_coords = get_point_coords("E₁")
        if t1_coords and e_coords and e1_coords:
            path2_1 = Line(start=t1_coords, end=e_coords, color=ORANGE, stroke_width=4)
            path2_2 = Line(start=e_coords, end=e1_coords, color=ORANGE, stroke_width=4)
            path2 = VGroup(path2_1, path2_2)
            
            # Show angle T₁EE₁ = 187° (hardcoded)
            angle_deg = 187
            angle_arc = create_manim_angle(e_coords, t1_coords, e1_coords, angle_deg, radius=0.4, color=YELLOW)
            angle_text = Text(f"{angle_deg}°", font_size=14, color=YELLOW, weight=BOLD)
            angle_text.move_to(angle_arc.get_center())
            
            # Conclusion text
            conclusion = Text("Angle > 180°", font_size=16, color=GREEN)
            conclusion.next_to(example2_desc, DOWN, buff=0.1, aligned_edge=LEFT)
        
        if t1_coords and e_coords:
            self.play(FadeOut(path1))
        self.play(FadeIn(example2_text))
        if t1_coords and e_coords and e1_coords:
            self.play(Create(path2))
            self.play(Create(angle_arc))
            self.play(Write(angle_text))
            self.play(Write(conclusion))
        self.next_slide()
        
        # Example 3: T₁ to F₁ - Analyze angle T₁EF₁
        example3_title = Text("Example 3: T₁ → F₁", font_size=20, weight=BOLD, color=PURPLE)
        example3_desc = Text("Check angle T₁EF₁", font_size=16, color=WHITE)
        example3_text = VGroup(example3_title, example3_desc.next_to(example3_title, DOWN, buff=0.1, aligned_edge=LEFT))
        example3_text.move_to(example2_text.get_center() + DOWN * 1.2)
        
        # Draw path T₁ → E → F₁ and show angle
        f1_coords = get_point_coords("F₁")
        if t1_coords and e_coords and f1_coords:
            path3_1 = Line(start=t1_coords, end=e_coords, color=PURPLE, stroke_width=4)
            path3_2 = Line(start=e_coords, end=f1_coords, color=PURPLE, stroke_width=4)
            path3_old = VGroup(path3_1, path3_2)
            
            # Show angle T₁EF₁ = 98° (hardcoded)
            angle_deg_f1 = 98
            angle_arc_f1 = create_manim_angle(e_coords, t1_coords, f1_coords, angle_deg_f1, radius=0.4, color=YELLOW)
            angle_text_f1 = Text(f"{angle_deg_f1}°", font_size=14, color=YELLOW, weight=BOLD)
            angle_text_f1.move_to(angle_arc_f1.get_center())
            
            # Show direct path T₁ → F₁
            path3_direct = Line(start=t1_coords, end=f1_coords, color=GREEN, stroke_width=4)
            
            # Conclusion text
            conclusion3 = Text("Angle < 180°", font_size=16, color=GREEN)
            conclusion3.next_to(example3_desc, DOWN, buff=0.1, aligned_edge=LEFT)
        
        if t1_coords and e_coords and e1_coords:
            self.play(FadeOut(path2, angle_arc, angle_text, conclusion))
        self.play(FadeIn(example3_text))
        if t1_coords and e_coords and f1_coords:
            self.play(Create(path3_old))
            self.play(Create(angle_arc_f1))
            self.play(Write(angle_text_f1))
            self.play(Write(conclusion3))
            self.next_slide()
            
            # Show the better direct path
            if t1_coords and e_coords and f1_coords:
                self.play(FadeOut(angle_arc_f1, angle_text_f1))
            self.play(FadeOut(path3_old), Create(path3_direct))
            better_text = Text("→ Shortest path: T₁F₁", font_size=16, color=GREEN, weight=BOLD)
            better_text.next_to(conclusion3, DOWN, buff=0.1, aligned_edge=LEFT)
            self.play(Write(better_text))
        self.next_slide()
        
        # Problem statement
        problem_title = Text("Problem:", font_size=20, weight=BOLD, color=RED)
        problem_desc = Text("Find shortest path from A to A₁", font_size=16, color=WHITE)
        problem_text = VGroup(problem_title, problem_desc.next_to(problem_title, DOWN, buff=0.1, aligned_edge=LEFT))
        problem_text.move_to(example3_text.get_center() + DOWN * 1.5)
        
        # Highlight A and A₁
        a_coords = get_point_coords("A")
        a1_coords = get_point_coords("A₁")
        if a_coords and a1_coords:
            highlight_a = Circle(radius=0.15, color=RED, stroke_width=3).move_to(a_coords)
            highlight_a1 = Circle(radius=0.15, color=RED, stroke_width=3).move_to(a1_coords)
        
        self.play(FadeIn(problem_text))
        if a_coords and a1_coords:
            self.play(Create(highlight_a), Create(highlight_a1))
        self.next_slide()
        
        # Clear everything - only clear objects that exist
        fade_objects = [title, polygon_lines, key_vertices, property_text, 
                       example1_text, example2_text, example3_text, path3_direct, better_text, conclusion3, problem_text]
        if a_coords and a1_coords:
            fade_objects.extend([highlight_a, highlight_a1])
        self.play(FadeOut(*fade_objects))

    def slide6(self):
        # Title for this slide
        title = Text("Funnel Technique", font_size=32, weight=BOLD)
        subtitle = Text("Shortest path algorithm on a sequence of adjacent triangles", font_size=24)
        subtitle2 = Text("(A type of vector-based map)", font_size=24, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        subtitle.next_to(title, DOWN, buff=0.2)
        subtitle2.next_to(subtitle, DOWN, buff=0.1)
        
        # Points from map/example.txt (exact coordinates)
        key_points = [
            (1, 3, "A"),
            (3, 2, "B"), 
            (3.46, 3.64, "C"),
            (4, 5, "D"),
            (6.68, 3.52, "E"),
            (2.14, 6.2, "F"),
            (3.24, 7.52, "G"),
        ]
        
        # Scale and position points for Manim
        scale_factor = 1
        
        # Calculate center of polygon for positioning
        center_x = sum(x for x, y, _ in key_points) / len(key_points) + 2
        center_y = sum(y for x, y, _ in key_points) / len(key_points) + 1.3
        
        # Helper function to get point coordinates
        def get_point_coords(label):
            for x, y, point_label in key_points:
                if point_label == label:
                    # Center the polygon and move it LEFT*1
                    centered_x = (x - center_x) * scale_factor + LEFT[0]
                    centered_y = (y - center_y) * scale_factor
                    return (centered_x, centered_y, 0)
            return None
        
        # Create all points
        all_points = VGroup()
        for x, y, label in key_points:
            coords = get_point_coords(label)
            if coords:
                point = Dot(point=coords, color=WHITE, radius=0.08)
                point_label = Text(label, font_size=14, color=WHITE, weight=BOLD)
                point_label.next_to(point, UP, buff=0.15)
                all_points.add(point, point_label)
        
        # Create original lines from map/example.txt
        original_lines = VGroup()
        line_connections = [
            ("A", "B"), ("A", "C"), ("C", "D"), ("B", "E"), ("D", "F"), ("F", "G"), ("G", "E")
        ]
        
        for start_label, end_label in line_connections:
            start_coords = get_point_coords(start_label)
            end_coords = get_point_coords(end_label)
            
            if start_coords and end_coords:
                line = Line(
                    start=start_coords,
                    end=end_coords,
                    color=BLUE,
                    stroke_width=2
                )
                original_lines.add(line)
        
        # Create triangulation edges for triangle sequence: ABC → BCE → ECD → DEG → DGF
        triangulation_edges = VGroup()
        triangulation_connections = [("B", "C"), ("C", "E"), ("D", "E"), ("D", "G")]
        
        for start_label, end_label in triangulation_connections:
            start_coords = get_point_coords(start_label)
            end_coords = get_point_coords(end_label)
            
            if start_coords and end_coords:
                line = Line(
                    start=start_coords,
                    end=end_coords,
                    color=YELLOW,
                    stroke_width=1.5
                )
                triangulation_edges.add(line)
        
        # Create funnel visualization
        funnel_elements = VGroup()
        
        # Funnel apex (A)
        a_coords = get_point_coords("A")
        if a_coords:
            funnel_apex = Dot(point=a_coords, color=RED, radius=0.12)
            apex_label = Text("A (Funnel apex)", font_size=12, color=RED, weight=BOLD)
            apex_label.next_to(funnel_apex, LEFT, buff=0.3)
            funnel_elements.add(funnel_apex, apex_label)
        
        # Left edge of funnel (AC)
        a_coords = get_point_coords("A")
        c_coords = get_point_coords("C")
        if a_coords is not None and c_coords is not None:
            left_edge = Line(start=a_coords, end=c_coords, color=GREEN, stroke_width=4)
            left_label = Text("AC (Left edge)", font_size=12, color=GREEN, weight=BOLD)
            left_label.next_to(left_edge.get_center(), UP, buff=0.2)
            funnel_elements.add(left_edge, left_label)
        
        # Right edge of funnel (AB)
        a_coords = get_point_coords("A")
        b_coords = get_point_coords("B")
        if a_coords is not None and b_coords is not None:
            right_edge = Line(start=a_coords, end=b_coords, color=ORANGE, stroke_width=4)
            right_label = Text("AB (Right edge)", font_size=12, color=ORANGE, weight=BOLD)
            right_label.next_to(right_edge.get_center(), DOWN * 1.5, buff=0.2)
            funnel_elements.add(right_edge, right_label)
        
        # Create colored triangles in sequence: ABC → BCE → ECD → DEG → DGF
        triangles = VGroup()
        triangle_data = [
            (["A", "B", "C"], RED, 0.3, "ABC"),
            (["B", "C", "E"], BLUE, 0.3, "BCE"),
            (["E", "C", "D"], GREEN, 0.3, "ECD"),
            (["D", "E", "G"], PURPLE, 0.3, "DEG"),
            (["D", "G", "F"], ORANGE, 0.3, "DGF"),
        ]
        
        triangle_objects = {}
        for vertices, color, opacity, name in triangle_data:
            coords = [get_point_coords(v) for v in vertices]
            valid_coords = [coord for coord in coords if coord is not None]
            if len(valid_coords) == len(vertices):
                triangle = Polygon(*valid_coords, fill_color=color, fill_opacity=opacity, stroke_color=color, stroke_width=2)
                triangle_objects[name] = triangle
                triangles.add(triangle)
        
        # Highlight start and end points
        start_end_points = VGroup()
        a_coords = get_point_coords("A")
        f_coords = get_point_coords("F")
        
        if a_coords and f_coords:
            highlight_a = Circle(radius=0.25, color=RED, stroke_width=4).move_to(a_coords)
            highlight_f = Circle(radius=0.25, color=RED, stroke_width=4).move_to(f_coords)
            start_label = Text("START", font_size=10, color=RED, weight=BOLD)
            end_label = Text("END", font_size=10, color=RED, weight=BOLD)
            start_label.next_to(highlight_a, DOWN, buff=0.1)
            end_label.next_to(highlight_f, DOWN, buff=0.1)
            start_end_points.add(highlight_a, highlight_f, start_label, end_label)
        
        # Explanation text
        explanation = VGroup()
        exp_title = Text("Funnel Technique:", font_size=22, weight=BOLD, color=YELLOW)
        exp_desc1 = Text("• Sequence of adjacent triangles:\nABC → BCE → ECD → DEG → DGF", font_size=18, color=WHITE)
        exp_desc2 = Text("• Funnel apex A with left edge AC, right edge AB", font_size=18, color=WHITE)
        exp_desc3 = Text("• Left edge AC: shortest path to left vertex", font_size=18, color=GREEN)
        exp_desc4 = Text("• Right edge AB: shortest path to right vertex", font_size=18, color=ORANGE)
        exp_desc5 = Text("• Find shortest path from A to F", font_size=18, color=WHITE)
        
        explanation.add(exp_title)
        explanation.add(exp_desc1.next_to(exp_title, DOWN *1.1, buff=0.2, aligned_edge=LEFT))
        explanation.add(exp_desc2.next_to(exp_desc1, DOWN *1.1, buff=0.1, aligned_edge=LEFT))
        explanation.add(exp_desc3.next_to(exp_desc2, DOWN *1.1, buff=0.1, aligned_edge=LEFT))
        explanation.add(exp_desc4.next_to(exp_desc3, DOWN *1.1, buff=0.1, aligned_edge=LEFT))
        explanation.add(exp_desc5.next_to(exp_desc4, DOWN *1.1, buff=0.1, aligned_edge=LEFT))
        explanation.move_to(RIGHT * 3.5 + UP * 0.5)
        
        # Legend
        legend = VGroup()
        legend_title = Text("Legend:", font_size=22, weight=BOLD)
        
        apex_dot = Dot(color=RED, radius=0.08)
        apex_text = Text("Funnel apex", font_size=18)
        apex_item = VGroup(apex_dot, apex_text.next_to(apex_dot, RIGHT, buff=0.1))
        
        left_line = Line(start=ORIGIN, end=RIGHT*0.3, color=GREEN, stroke_width=4)
        left_text = Text("Left edge", font_size=18)
        left_item = VGroup(left_line, left_text.next_to(left_line, RIGHT, buff=0.1))
        
        right_line = Line(start=ORIGIN, end=RIGHT*0.3, color=ORANGE, stroke_width=4)
        right_text = Text("Right edge", font_size=18)
        right_item = VGroup(right_line, right_text.next_to(right_line, RIGHT, buff=0.1))
        
        triangle_sample = Rectangle(width=0.3, height=0.2, fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE)
        triangle_text = Text("Current triangle", font_size=18)
        triangle_item = VGroup(triangle_sample, triangle_text.next_to(triangle_sample, RIGHT, buff=0.1))
        
        edge_line = Line(start=ORIGIN, end=RIGHT*0.3, color=YELLOW, stroke_width=3)
        edge_text = Text("Adjacent edge", font_size=18)
        edge_item = VGroup(edge_line, edge_text.next_to(edge_line, RIGHT, buff=0.1))
        
        legend.add(legend_title)
        legend.add(apex_item.next_to(legend_title, DOWN, buff=0.1, aligned_edge=LEFT))
        legend.add(left_item.next_to(apex_item, DOWN, buff=0.05, aligned_edge=LEFT))
        legend.add(right_item.next_to(left_item, DOWN, buff=0.05, aligned_edge=LEFT))
        legend.add(triangle_item.next_to(right_item, DOWN, buff=0.05, aligned_edge=LEFT))
        legend.add(edge_item.next_to(triangle_item, DOWN, buff=0.05, aligned_edge=LEFT))
        legend.move_to(RIGHT * 4 + DOWN * 2)
        
        # Animate the slide
        self.play(Write(title), Write(subtitle), Write(subtitle2))
        self.next_slide()
        
        self.play(Create(all_points))
        self.next_slide()
        
        self.play(Create(original_lines))
        self.next_slide()
        
        self.play(FadeIn(explanation))
        self.next_slide()
        
        self.play(Create(triangulation_edges))
        self.next_slide()
        
        # Show triangles one by one
        for name in ["ABC", "BCE", "ECD", "DEG", "DGF"]:
            if name in triangle_objects:
                self.play(FadeIn(triangle_objects[name]))
                self.next_slide()
        
        self.play(Create(funnel_elements))
        self.next_slide()
        
        self.play(Create(start_end_points))
        self.next_slide()
        
        self.play(FadeIn(legend))
        self.next_slide()
        
        # Clear everything
        fade_objects = [title, subtitle, subtitle2, all_points, original_lines, triangulation_edges, 
                       triangles, funnel_elements, start_end_points, explanation, legend]
        self.play(FadeOut(*fade_objects))

    def slide7(self):
        # Title for this slide
        title = Text("Funnel Algorithm - Step by Step", font_size=32, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        
        # Points from map/example.txt (same as slide6)
        key_points = [
            (1, 3, "A"),
            (3, 2, "B"), 
            (3.46, 3.64, "C"),
            (4, 5, "D"),
            (6.68, 3.52, "E"),
            (2.14, 6.2, "F"),
            (3.24, 7.52, "G"),
        ]
        
        # Scale and position points for Manim (same as slide6)
        scale_factor = 1.2
        center_x = sum(x for x, y, _ in key_points) / len(key_points) + 2
        center_y = sum(y for x, y, _ in key_points) / len(key_points) + 0.8
        
        # Helper function to get point coordinates
        def get_point_coords(label):
            for x, y, point_label in key_points:
                if point_label == label:
                    # Center the polygon and move it LEFT*1
                    centered_x = (x - center_x) * scale_factor + LEFT[0]
                    centered_y = (y - center_y) * scale_factor
                    return (centered_x, centered_y, 0)
            return None
        
        # Create all points
        all_points = VGroup()
        for x, y, label in key_points:
            coords = get_point_coords(label)
            if coords:
                point = Dot(point=coords, color=WHITE, radius=0.08)
                point_label = Text(label, font_size=14, color=WHITE, weight=BOLD)
                point_label.next_to(point, UP, buff=0.15)
                all_points.add(point, point_label)
        
        # Create original lines from map/example.txt + all triangle edges
        original_lines = VGroup()
        line_connections = [
            # Original polygon edges
            ("A", "B"), ("A", "C"), ("C", "D"), ("B", "E"), ("D", "F"), ("F", "G"), ("G", "E"),
            # Triangulation edges for ABC → BCE → ECD → DEG → DGF
            ("B", "C"), ("C", "E"), ("D", "E"), ("D", "G")
        ]
        for start_label, end_label in line_connections:
            start_coords = get_point_coords(start_label)
            end_coords = get_point_coords(end_label)
            if start_coords and end_coords:
                line = Line(
                    start=start_coords,
                    end=end_coords,
                    color=BLUE,
                    stroke_width=2
                )
                original_lines.add(line)
        
        # Funnel algorithm steps từ A đến F
        funnel_steps = [
            {
                "step": 1,
                "description": "Step 1: Initialize funnel from triangle ABC",
                "apex": "A",
                "left_edge": ("A", "C"),
                "right_edge": ("A", "B"), 
                "current_triangle": "ABC",
                "adjacent_edge": "BC"
            },
            {
                "step": 2,
                "description": "Step 2: Check common edge CE (triangle BCE)",
                "apex": "A",
                "left_edge": ("A", "C"),
                "right_edge": ("A", "E"),
                "current_triangle": "BCE",
                "adjacent_edge": "CE",
                "note": "Angle ABE <180°, update right edge to AE"
            },
            {
                "step": 3,
                "description": "Step 3: Check common edge DE (triangle ECD)",
                "apex": "A",
                "left_edge": ("A", "C", "D"),
                "right_edge": ("A", "E"),
                "current_triangle": "ECD",
                "adjacent_edge": "DE",
                "note": "Angle ACD>180°, extend left edge to ACD"
            },
            {
                "step": 4,
                "description": "Step 4: Check common edge DG (triangle DEG)",
                "apex": "C",
                "left_edge": ("A", "C", "D"),
                "right_edge": ("A", "C", "D", "G"),
                "current_triangle": "DEG", 
                "adjacent_edge": "DG",
                "note": "Move apex A→C→D, add segment ACD",
                "path_segment": [("A", "C"), ("C", "D")]
            },
            {
                "step": 5,
                "description": "Step 5: Check common edge FG (triangle DGF)",
                "apex": "D",
                "left_edge": ("D", "F"),
                "right_edge": ("D", "G"),
                "current_triangle": "DGF",
                "adjacent_edge": "FG"
            },
            {
                "step": 6,
                "description": "Step 6: Shortest path A→C→D→F",
                "apex": "D",
                "left_edge": ("D", "F"),
                "right_edge": ("D", "G"),
                "current_triangle": "DGF",
                "final_path": [("A", "C"), ("C", "D"), ("D", "F")]
            }
        ]
        
        # Create step information display
        def create_step_info(step_data):
            info = VGroup()

            # Funnel apex ký hiệu
            apex = step_data['apex']
            # Lấy đáy phễu (hai điểm cuối của left_edge và right_edge)
            left_edge = step_data['left_edge']
            right_edge = step_data['right_edge']
            if isinstance(left_edge, (list, tuple)) and len(left_edge) > 1:
                left_base = left_edge[-1]
            else:
                left_base = left_edge[-1] if left_edge else ""
            if isinstance(right_edge, (list, tuple)) and len(right_edge) > 1:
                right_base = right_edge[-1]
            else:
                right_base = right_edge[-1] if right_edge else ""
            # Đáy phễu là hai điểm cuối của left/right edge
            funnel_base = f"({left_base}, {right_base})"
            funnel_text = Text(f"F: {apex}{funnel_base}", font_size=22, color=YELLOW)

            # Shortest path ký hiệu
            # SP(A, D) = ACD, SP(A, E) = AE
            # Nếu có left_edge dài >=2 thì SP(A, D) = nối các điểm trong left_edge
            sp_left = "".join(left_edge) if isinstance(left_edge, (list, tuple)) else left_edge
            sp_right = "".join(right_edge) if isinstance(right_edge, (list, tuple)) else right_edge
            sp_left_text = Text(f"SP({apex}, {left_base}) = {sp_left}", font_size=18, color=GREEN)
            sp_right_text = Text(f"SP({apex}, {right_base}) = {sp_right}", font_size=18, color=ORANGE)

            info.add(funnel_text)
            info.add(sp_left_text.next_to(funnel_text, DOWN, buff=0.2, aligned_edge=LEFT))
            info.add(sp_right_text.next_to(sp_left_text, DOWN, buff=0.1, aligned_edge=LEFT))
            return info
        
        # Create funnel visualization for a step
        def create_funnel_visual(step_data):
            funnel_visual = VGroup()
            
            # Apex
            apex_coords = get_point_coords(step_data['apex'])
            if apex_coords:
                apex_dot = Dot(point=apex_coords, color=RED, radius=0.12)
                funnel_visual.add(apex_dot)
            
            # Current triangle highlight
            triangle_vertices = list(step_data['current_triangle'])
            triangle_coords = [get_point_coords(v) for v in triangle_vertices]
            valid_triangle_coords = [coord for coord in triangle_coords if coord is not None]
            if len(valid_triangle_coords) == len(triangle_vertices):
                triangle = Polygon(*valid_triangle_coords, fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE, stroke_width=2)
                funnel_visual.add(triangle)
            
            # Adjacent edge highlight - cạnh đang xét
            if 'adjacent_edge' in step_data and len(step_data['adjacent_edge']) == 2:
                edge_start = get_point_coords(step_data['adjacent_edge'][0])
                edge_end = get_point_coords(step_data['adjacent_edge'][1])
                if edge_start is not None and edge_end is not None:
                    # Add glowing effect with slightly larger line behind first
                    glow_line = Line(start=edge_start, end=edge_end, color=YELLOW, stroke_width=12, stroke_opacity=0.3)
                    funnel_visual.add(glow_line)
                    
                    # Highlight with bright yellow and thick stroke on top
                    edge_line = Line(start=edge_start, end=edge_end, color=YELLOW, stroke_width=8)
                    funnel_visual.add(edge_line)

            
            # Left edge (can be multiple points)
            left_coords = [get_point_coords(point) for point in step_data['left_edge']]
            left_coords = [coord for coord in left_coords if coord is not None]
            if len(left_coords) >= 2:
                for i in range(len(left_coords) - 1):
                    left_line = Line(start=left_coords[i], end=left_coords[i+1], color=GREEN, stroke_width=8)
                    funnel_visual.add(left_line)
            
            # Right edge (can be multiple points)
            right_coords = [get_point_coords(point) for point in step_data['right_edge']]
            right_coords = [coord for coord in right_coords if coord is not None]
            if len(right_coords) >= 2:
                for i in range(len(right_coords) - 1):
                    right_line = Line(start=right_coords[i], end=right_coords[i+1], color=ORANGE, stroke_width=8)
                    funnel_visual.add(right_line)
            
            # Path segments
            if 'path_segment' in step_data:
                for path_start, path_end in step_data['path_segment']:
                    path_start_coords = get_point_coords(path_start)
                    path_end_coords = get_point_coords(path_end)
                    if path_start_coords is not None and path_end_coords is not None:
                        path_line = Line(start=path_start_coords, end=path_end_coords, color=RED, stroke_width=6)
                        funnel_visual.add(path_line)
                        
            # Final complete path
            if 'final_path' in step_data:
                for path_start, path_end in step_data['final_path']:
                    path_start_coords = get_point_coords(path_start)
                    path_end_coords = get_point_coords(path_end)
                    if path_start_coords is not None and path_end_coords is not None:
                        path_line = Line(start=path_start_coords, end=path_end_coords, color=RED, stroke_width=6)
                        funnel_visual.add(path_line)

            # Legacy path support
            if 'path' in step_data:
                for path_start, path_end in step_data['path']:
                    path_start_coords = get_point_coords(path_start)
                    path_end_coords = get_point_coords(path_end)
                    if path_start_coords is not None and path_end_coords is not None:
                        path_line = Line(start=path_start_coords, end=path_end_coords, color=RED, stroke_width=6)
                        funnel_visual.add(path_line)
            
            return funnel_visual
        
        # Legend
        legend = VGroup()
        legend_title = Text("Legend:", font_size=14, weight=BOLD)
        
        apex_dot = Dot(color=RED, radius=0.08)
        apex_text = Text("Funnel apex", font_size=10)
        apex_item = VGroup(apex_dot, apex_text.next_to(apex_dot, RIGHT, buff=0.1))
        
        left_line = Line(start=ORIGIN, end=RIGHT*0.3, color=GREEN, stroke_width=8)
        left_text = Text("Left edge", font_size=10)
        left_item = VGroup(left_line, left_text.next_to(left_line, RIGHT, buff=0.1))
        
        right_line = Line(start=ORIGIN, end=RIGHT*0.3, color=ORANGE, stroke_width=8)
        right_text = Text("Right edge", font_size=10)
        right_item = VGroup(right_line, right_text.next_to(right_line, RIGHT, buff=0.1))
        
        triangle_sample = Rectangle(width=0.3, height=0.2, fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE)
        triangle_text = Text("Current triangle", font_size=10)
        triangle_item = VGroup(triangle_sample, triangle_text.next_to(triangle_sample, RIGHT, buff=0.1))
        
        edge_line = Line(start=ORIGIN, end=RIGHT*0.3, color=YELLOW, stroke_width=8)
        edge_text = Text("Highlighted edge", font_size=10)
        edge_item = VGroup(edge_line, edge_text.next_to(edge_line, RIGHT, buff=0.1))
        
        legend.add(legend_title)
        legend.add(apex_item.next_to(legend_title, DOWN, buff=0.1, aligned_edge=LEFT))
        legend.add(left_item.next_to(apex_item, DOWN, buff=0.05, aligned_edge=LEFT))
        legend.add(right_item.next_to(left_item, DOWN, buff=0.05, aligned_edge=LEFT))
        legend.add(triangle_item.next_to(right_item, DOWN, buff=0.05, aligned_edge=LEFT))
        legend.add(edge_item.next_to(triangle_item, DOWN, buff=0.05, aligned_edge=LEFT))
        legend.move_to(RIGHT * 4 + DOWN * 2.5)
        
        # Animation sequence
        self.play(Write(title))
        self.next_slide()
        
        self.play(Create(all_points), Create(original_lines))
        self.next_slide()
        
        self.play(FadeIn(legend))
        self.next_slide()
        
        # Execute funnel algorithm step by step
        current_funnel = None
        current_info = None
        
        for step_data in funnel_steps:
            # Clear previous step
            if current_funnel is not None:
                self.play(FadeOut(current_funnel))
            if current_info is not None:
                self.play(FadeOut(current_info))
            
            # Create and show new step
            current_info = create_step_info(step_data).move_to(RIGHT * 4 + UP * 1.2)
            current_funnel = create_funnel_visual(step_data)
            
            # Only animate if objects were created successfully
            if current_info:
                self.play(FadeIn(current_info))
            if current_funnel:
                self.play(Create(current_funnel))
            self.next_slide()
        
        # Clear everything - only include objects that exist
        fade_objects = [title, all_points, original_lines, legend]
        if current_funnel is not None:
            fade_objects.append(current_funnel)
        if current_info is not None:
            fade_objects.append(current_info)
        
        if fade_objects:
            self.play(FadeOut(*fade_objects))
        
        # Final slide boundary
        self.next_slide()

    def slide8(self):
        # Title for this slide
        title = Text("Funnel Algorithm: A to A₁ (HMT Analysis)", font_size=28, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        # Data from output.txt - Use exact coordinates and algorithm results
        scale_factor = 1.5
        origin_x = -6.5
        origin_y = -5

        key_points = [
            (0.3347507967871943, 3.485183600744722, "A"), (0.050904694188400594, 3.6085949497007195, "B"),
            (0.9641486764627804, 4.275016234063106, "C"), (2.5684962128907447, 4.595885741348698, "D"),
            (3.5187635998519236, 3.3617722517887247, "E"), (3.9630444560935136, 3.5715715450139203, "F"),
            (3.3459877113135272, 4.0035112663599115, "G"), (3.8272919722419165, 4.5218389319751005, "H"),
            (4.357960772752705, 4.447792122601502, "I"), (4.432007582126303, 4.2379928293763065, "J"),
            (5.431639508669881, 4.756320494991495, "K"), (7.043225809633118, 4.749466919462989, "L"),
            (6.0264503048242775, 3.6425973825824793, "M"), (6.296732401039286, 2.8446216699476925, "N"),
            (7.583790002063135, 4.517796551278697, "O"), (8.072871890452197, 4.221773303043212, "P"),
            (8.150095346513627, 3.629726806572241, "Q"), (8.510471474800305, 2.9861980060603166, "R"),
            (8.631955589793407, 2.8796705978210464, "S"), (8.644201190827998, 2.6898637817848825, "T"),
            (8.713164032907233, 2.6637460985435673, "U"), (8.668438722601804, 2.340347700950471, "V"),
            (8.080128871661172, 2.1786485021539224, "W"), (6.976866217449777, 0.9130917744833986, "Z"),
            (6.73721872009328, 0.9062447031303559, "A₁"), (6.73721872009328, 1.7895169076728765, "B₁"),
            (5.806017016079461, 2.583777184625841, "C₁"), (5.669075589018606, 2.4947652570362844, "D₁"),
            (4.683097314180445, 3.26848431993012, "E₁"), (3.484446850448112, 2.7444580422308507, "F₁"),
            (3.1338312795565395, 2.0522170432910776, "G₁"), (3.1620538406947065, 1.8886049360312143, "H₁"),
            (3.0259495654360555, 1.6926113295561307, "I₁"), (2.7181599984970997, 1.6755358917763574, "J₁"),
            (2.5849918458378176, 1.7998261675916907, "K₁"), (2.702304423074604, 2.0612071861344514, "L₁"),
            (2.2887578522794154, 2.5736453282067506, "M₁"), (1.8122802815806116, 2.7444580422308507, "N₁"),
            (1.4257041393155443, 2.4118227570260244, "O₁"), (0.9222561400866195, 2.3399016142790354, "P₁"),
            (0.643561711942036, 2.501724185459761, "Q₁"), (0.7334631403757726, 2.8523397563513346, "R₁"),
            (1.0481181398938506, 3.08608347027905, "S₁"), (1.3178224251950605, 3.805294897748944, "T₁"),
            (0.9042758543998721, 4.128940040110396, "U₁"),
        ]

        def get_point_coords(label):
            for x, y, point_label in key_points:
                if point_label == label:
                    return (origin_x + x * scale_factor, origin_y + y * scale_factor, 0)
            return None

        # Create polygon and points
        polygon_lines = VGroup()
        all_points = VGroup()
        line_connections = [
            (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10),
            (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18),
            (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26),
            (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (31, 32), (32, 33), (33, 34),
            (34, 35), (35, 36), (36, 37), (37, 38), (38, 39), (39, 40), (40, 41), (41, 42),
            (42, 43), (43, 44), (44, 0)
        ]
        
        for start_idx, end_idx in line_connections:
            start_x, start_y, _ = key_points[start_idx]
            end_x, end_y, _ = key_points[end_idx]
            line = Line(start=(origin_x + start_x * scale_factor, origin_y + start_y * scale_factor, 0),
                        end=(origin_x + end_x * scale_factor, origin_y + end_y * scale_factor, 0),
                        color=BLUE, stroke_width=2)
            polygon_lines.add(line)

        for x, y, label in key_points:
            point = Dot(point=(origin_x + x * scale_factor, origin_y + y * scale_factor, 0), 
                       color=WHITE, radius=0.06)
            point_label = Text(label, font_size=10, color=WHITE, weight=BOLD)
            point_label.next_to(point, UP, buff=0.05)
            all_points.add(point, point_label)

        # Setup slide
        self.play(Write(title))
        self.play(Create(polygon_lines), Create(all_points))
        
        # Highlight START and GOAL points theo phân tích HMT (chính xác)
        info_text = Text("5 Apex Changes: A → U₁ → E → E₁ → C₁ → B₁ → A₁", 
                        font_size=14, color=YELLOW, weight=BOLD)
        info_text.to_edge(DOWN, buff=0.3)
        self.play(Write(info_text))
        
        # Highlight start and goal points
        a_coord = get_point_coords("A")
        a1_coord = get_point_coords("A₁")
        if a_coord and a1_coord:
            start_circle = Circle(radius=0.15, color=GREEN, stroke_width=4).move_to(a_coord)
            goal_circle = Circle(radius=0.15, color=RED, stroke_width=4).move_to(a1_coord)
            self.play(Create(start_circle), Create(goal_circle))
        
        self.next_slide()

        # --- Draw all map connections (using index pairs) ---
        # List of connection pairs as index pairs (e.g., (0, 2))
        connection_pairs = [
            (0, 2),   # AC
            (2, 44),  # CU1
            (3, 43),  # DT1
            (3, 42),  # DS1
            (42, 40), # S1Q1
            (42, 39), # S1P1
            (42, 38), # S1O1
            (42, 37), # S1N1
            (3, 37), # DN1
            (3, 36), # DM1
            (3, 35), # DL1
            (4, 28),  # EL1
            (4, 34),  # EK1
            (4, 33),  # EJ1
            (33, 31), # J1H1
            (33, 30), # J1G1
            (33, 29), # J1F1
            (4, 29),  # EF1
            (4, 28),  # EE1
            (5, 28),   # FE1
            (5, 7),   # FH
            (5, 8),   # FI
            (5, 9),   # FJ
            (5, 10),  # FK
            (10, 28), # KE1
            (11, 28), # LE1
            (12, 28), # ME1
            (12, 27), # MD1
            (12, 26), # MC1
            (13, 26), # NC1
            (13, 25), # NB1
            (25, 14), # B1O
            (15, 25), # PB1
            (16, 25), # QB1
            (17, 25), # RB1
            (23, 25), # ZB1
            (25, 22), # B1W
            (18, 25), # SB1
            (19, 25), # TB1
            (20, 25), # UB1
            (20, 22)  # UW
        ]
        # Draw all map connections as blue lines
        map_lines = VGroup()
        for start_idx, end_idx in connection_pairs:
            start_label = key_points[start_idx][2]
            end_label = key_points[end_idx][2]
            start_coords = get_point_coords(start_label)
            end_coords = get_point_coords(end_label)
            if start_coords and end_coords:
                line = Line(start=start_coords, end=end_coords, color=BLUE, stroke_width=2.5)
                map_lines.add(line)
        self.play(Create(map_lines))
        self.next_slide()

        triangle_data = [
            (["A", "C", "U₁"], "BLUE", 0.3, "ACU1"),
            (["C", "U₁", "D"], "GREEN", 0.3, "CU1D"),
            (["D", "U₁", "T₁"], "BLUE", 0.3, "DU1T1"),
            (["D", "T₁", "S₁"], "GREEN", 0.3, "DT1S1"),
            (["D", "S₁", "N₁"], "BLUE", 0.3, "DS1N1"),
            (["D", "N₁", "M₁"], "GREEN", 0.3, "DN1M1"),
            (["D", "M₁", "L₁"], "BLUE", 0.3, "DM1L1"),
            (["D", "L₁", "E"], "GREEN", 0.3, "DL1E"),
            (["L₁", "E", "K₁"], "BLUE", 0.3, "L1EK1"),
            (["E", "K₁", "J₁"], "GREEN", 0.3, "EK1J1"),
            (["E", "J₁", "F₁"], "BLUE", 0.3, "EJ1F1"),
            (["E", "E₁", "F₁"], "GREEN", 0.3, "EFF1"),
            (["F", "E", "E₁"], "BLUE", 0.3, "E1FF1"),
            (["F", "E₁", "K"], "GREEN", 0.3, "FE1K"),
            (["K", "E₁", "L"], "BLUE", 0.3, "KE1L"),
            (["L", "E₁", "M"], "GREEN", 0.3, "LE1M"),
            (["M", "E₁", "D₁"], "BLUE", 0.3, "ME1D1"),
            (["M", "D₁", "C₁"], "GREEN", 0.3, "MD1C1"),
            (["M", "C₁", "N"], "BLUE", 0.3, "MC1N"),
            (["N", "C₁", "B₁"], "GREEN", 0.3, "NC1B1"),
            (["N", "B₁", "O"], "BLUE", 0.3, "NB1O"),
            (["O", "B₁", "P"], "GREEN", 0.3, "OB1P"),
            (["P", "B₁", "Q"], "BLUE", 0.3, "PB1Q"),
            (["Q", "B₁", "R"], "GREEN", 0.3, "QB1R"),
            (["R", "B₁", "S"], "BLUE", 0.3, "RB1S"),
            (["S", "B₁", "T"], "GREEN", 0.3, "SB1T"),
            (["T", "B₁", "U"], "BLUE", 0.3, "TB1U"),
            (["U", "B₁", "W"], "GREEN", 0.3, "UB1W"),
            (["W", "B₁", "Z"], "BLUE", 0.3, "WB1Z"),
            (["B₁", "A₁", "Z"], "GREEN", 0.3, "B1A1Z")
        ]

        # --- Draw all adjacent triangles (from triangle_data) ---
        triangles = VGroup()
        for vertices, color_name, opacity, name in triangle_data:
            coords = [get_point_coords(v) for v in vertices]
            if all(c is not None for c in coords):
                color = eval(color_name) if color_name in globals() else BLUE
                triangle = Polygon(*coords, fill_color=color, fill_opacity=opacity, stroke_color=color, stroke_width=2)
                triangles.add(triangle)
        self.play(FadeIn(triangles))
        self.next_slide()

    def slide9(self):    
        # Title for this slide
        title = Text("Funnel Algorithm: A to A₁ (HMT Analysis)", font_size=28, weight=BOLD)
        title.to_edge(UP, buff=0.5)

        # Data from output.txt - Use exact coordinates and algorithm results
        scale_factor = 1.5
        origin_x = -6.5
        origin_y = -5

        key_points = [
            (0.3347507967871943, 3.485183600744722, "A"), (0.050904694188400594, 3.6085949497007195, "B"),
            (0.9641486764627804, 4.275016234063106, "C"), (2.5684962128907447, 4.595885741348698, "D"),
            (3.5187635998519236, 3.3617722517887247, "E"), (3.9630444560935136, 3.5715715450139203, "F"),
            (3.3459877113135272, 4.0035112663599115, "G"), (3.8272919722419165, 4.5218389319751005, "H"),
            (4.357960772752705, 4.447792122601502, "I"), (4.432007582126303, 4.2379928293763065, "J"),
            (5.431639508669881, 4.756320494991495, "K"), (7.043225809633118, 4.749466919462989, "L"),
            (6.0264503048242775, 3.6425973825824793, "M"), (6.296732401039286, 2.8446216699476925, "N"),
            (7.583790002063135, 4.517796551278697, "O"), (8.072871890452197, 4.221773303043212, "P"),
            (8.150095346513627, 3.629726806572241, "Q"), (8.510471474800305, 2.9861980060603166, "R"),
            (8.631955589793407, 2.8796705978210464, "S"), (8.644201190827998, 2.6898637817848825, "T"),
            (8.713164032907233, 2.6637460985435673, "U"), (8.668438722601804, 2.340347700950471, "V"),
            (8.080128871661172, 2.1786485021539224, "W"), (6.976866217449777, 0.9130917744833986, "Z"),
            (6.73721872009328, 0.9062447031303559, "A₁"), (6.73721872009328, 1.7895169076728765, "B₁"),
            (5.806017016079461, 2.583777184625841, "C₁"), (5.669075589018606, 2.4947652570362844, "D₁"),
            (4.683097314180445, 3.26848431993012, "E₁"), (3.484446850448112, 2.7444580422308507, "F₁"),
            (3.1338312795565395, 2.0522170432910776, "G₁"), (3.1620538406947065, 1.8886049360312143, "H₁"),
            (3.0259495654360555, 1.6926113295561307, "I₁"), (2.7181599984970997, 1.6755358917763574, "J₁"),
            (2.5849918458378176, 1.7998261675916907, "K₁"), (2.702304423074604, 2.0612071861344514, "L₁"),
            (2.2887578522794154, 2.5736453282067506, "M₁"), (1.8122802815806116, 2.7444580422308507, "N₁"),
            (1.4257041393155443, 2.4118227570260244, "O₁"), (0.9222561400866195, 2.3399016142790354, "P₁"),
            (0.643561711942036, 2.501724185459761, "Q₁"), (0.7334631403757726, 2.8523397563513346, "R₁"),
            (1.0481181398938506, 3.08608347027905, "S₁"), (1.3178224251950605, 3.805294897748944, "T₁"),
            (0.9042758543998721, 4.128940040110396, "U₁"),
        ]

        def get_point_coords(label):
            for x, y, point_label in key_points:
                if point_label == label:
                    return (origin_x + x * scale_factor, origin_y + y * scale_factor, 0)
            return None

        # Funnel Algorithm Steps theo phân tích của Hà Minh Trường (phiên bản chính xác)
        # 5 lần dời đỉnh phễu: A→U₁→E→E₁→C₁→B₁  
        # Đường đi cuối: A → U₁ → E → E₁ → C₁ → B₁ → A₁ (7 points, 6 segments)
        # Tối ưu hiệu suất: 9 bước thay vì 10, hardcode thay vì đọc file
        funnel_steps = [
            {
                "step": 1,
                "apex": "A",
                "left_edge": ["A", "C"],
                "right_edge": ["A", "U₁"],
                "adjacent_edge": "CU₁",
                "move_apex": False
            },
            {
                "step": 2,
                "apex": "A",
                "left_edge": ["A", "U₁", "D"],
                "right_edge": ["A", "U₁"],
                "adjacent_edge": "DU₁",
                "move_apex": False
            },
            {
                "step": 3,
                "apex": "U₁",
                "left_edge": ["U₁", "D"],
                "right_edge": ["U₁", "T₁"],
                "adjacent_edge": "DT₁",
                "move_apex": True
            },
            {
                "step": 4,
                "apex": "U₁",
                "left_edge": ["U₁", "D"],
                "right_edge": ["U₁", "T₁", "S₁"],
                "adjacent_edge": "DS₁",
                "move_apex": False
            },
            {
                "step": 5,
                "apex": "U₁",
                "left_edge": ["U₁", "D"],
                "right_edge": ["U₁", "T₁", "N₁"],
                "adjacent_edge": "DN₁",
                "move_apex": False
            },
            {
                "step": 6,
                "apex": "U₁",
                "left_edge": ["U₁", "D"],
                "right_edge": ["U₁", "T₁", "M₁"],
                "adjacent_edge": "DM₁",
                "move_apex": False
            },
            {
                "step": 7,
                "apex": "U₁",
                "left_edge": ["U₁", "D"],
                "right_edge": ["U₁", "T₁", "L₁"],
                "adjacent_edge": "DL₁",
                "move_apex": False
            },
            {
                "step": 8,
                "apex": "U₁",
                "left_edge": ["U₁", "E"],
                "right_edge": ["U₁", "T₁", "L₁"],
                "adjacent_edge": "EL₁",
                "move_apex": False
            },
            {
                "step": 9,
                "apex": "U₁",
                "left_edge": ["U₁", "E"],
                "right_edge": ["U₁", "T₁", "L₁", "K₁"],
                "adjacent_edge": "EK₁",
                "move_apex": False
            },
            {
                "step": 10,
                "apex": "U₁",
                "left_edge": ["U₁", "E"],
                "right_edge": ["U₁", "T₁", "L₁", "J₁"],
                "adjacent_edge": "EJ₁",
                "move_apex": False
            },
            {
                "step": 11,
                "apex": "U₁",
                "left_edge": ["U₁", "E"],
                "right_edge": ["U₁", "T₁", "F₁"],
                "adjacent_edge": "EF₁",
                "move_apex": False
            },
            {
                "step": 12,
                "apex": "U₁",
                "left_edge": ["U₁", "E", "F₁"],
                "right_edge": ["U₁", "T₁", "F₁"],
                "adjacent_edge": "FF₁",
                "move_apex": False
            },
            {
                "step": 13,
                "apex": "U₁",
                "left_edge": ["U₁", "E", "F"],
                "right_edge": ["U₁", "E", "E₁"],
                "adjacent_edge": "FE₁",
                "move_apex": False
            },
            {
                "step": 14,
                "apex": "E",
                "left_edge": ["E", "F", "K"],
                "right_edge": ["E", "E₁"],
                "adjacent_edge": "KE₁",
                "move_apex": True
            },
            {
                "step": 15,
                "apex": "E",
                "left_edge": ["E", "L"],
                "right_edge": ["E", "E₁"],
                "adjacent_edge": "LE₁",
                "move_apex": False
            },
            {
                "step": 16,
                "apex": "E",
                "left_edge": ["E", "M"],
                "right_edge": ["E", "E₁"],
                "adjacent_edge": "ME₁",
                "move_apex": False
            },
            {
                "step": 17,
                "apex": "E",
                "left_edge": ["E", "M"],
                "right_edge": ["E", "E₁", "D₁"],
                "adjacent_edge": "MD₁",
                "move_apex": False
            },
            {
                "step": 18,
                "apex": "E",
                "left_edge": ["E", "M"],
                "right_edge": ["E", "E₁", "C₁"],
                "adjacent_edge": "MC₁",
                "move_apex": False
            },
            {
                "step": 19,
                "apex": "E",
                "left_edge": ["E", "E₁", "N"],
                "right_edge": ["E", "E₁", "C₁"],
                "adjacent_edge": "NC₁",
                "move_apex": False
            },
            {
                "step": 20,
                "apex": "E₁",
                "left_edge": ["E₁", "N"],
                "right_edge": ["E₁", "C₁", "B₁"],
                "adjacent_edge": "NB₁",
                "move_apex": True
            },
            {
                "step": 21,
                "apex": "E₁",
                "left_edge": ["E₁", "N", "O"],
                "right_edge": ["E₁", "C₁", "B₁"],
                "adjacent_edge": "OB₁",
                "move_apex": False
            },
            {
                "step": 22,
                "apex": "E₁",
                "left_edge": ["E₁", "N", "P"],
                "right_edge": ["E₁", "C₁", "B₁"],
                "adjacent_edge": "PB₁",
                "move_apex": False
            },
            {
                "step": 23,
                "apex": "E₁",
                "left_edge": ["E₁", "N", "Q"],
                "right_edge": ["E₁", "C₁", "B₁"],
                "adjacent_edge": "QB₁",
                "move_apex": False
            },
            {
                "step": 24,
                "apex": "E₁",
                "left_edge": ["E₁", "N", "R"],
                "right_edge": ["E₁", "C₁", "B₁"],
                "adjacent_edge": "RB₁",
                "move_apex": False
            },
            {
                "step": 25,
                "apex": "E₁",
                "left_edge": ["E₁", "N", "S"],
                "right_edge": ["E₁", "C₁", "B₁"],
                "adjacent_edge": "SB₁",
                "move_apex": False
            },
            {
                "step": 26,
                "apex": "E₁",
                "left_edge": ["E₁", "T"],
                "right_edge": ["E₁", "C₁", "B₁"],
                "adjacent_edge": "TB₁",
                "move_apex": False
            },
            {
                "step": 27,
                "apex": "E₁",
                "left_edge": ["E₁", "U"],
                "right_edge": ["E₁", "C₁", "B₁"],
                "adjacent_edge": "UB₁",
                "move_apex": False
            },
            {
                "step": 28,
                "apex": "E₁",
                "left_edge": ["E₁", "W"],
                "right_edge": ["E₁", "C₁", "B₁"],
                "adjacent_edge": "WB₁",
                "move_apex": False
            },
            {
                "step": 29,
                "apex": "E₁",
                "left_edge": ["E₁", "C₁", "B₁", "Z"],
                "right_edge": ["E₁", "C₁", "B₁"],
                "adjacent_edge": "ZB₁",
                "move_apex": False
            },
            {
                "step": 30,
                "apex": "B₁",
                "left_edge": ["B₁", "A₁"],
                "right_edge": ["B₁", "B₁"],
                "adjacent_edge": "A₁B₁",
                "move_apex": True
            }
        ]

        # Step-by-step execution
        current_funnel_left = None
        current_funnel_right = None
        current_apex = None
        path_segments = VGroup()
        step_texts = VGroup()
        
        for step_data in funnel_steps:
            # Clear previous funnel
            if current_funnel_left:
                self.play(FadeOut(current_funnel_left))
            if current_funnel_right:
                self.play(FadeOut(current_funnel_right))
            if current_apex:
                self.play(FadeOut(current_apex))
            
            # Draw new funnel
            apex_coord = get_point_coords(step_data['apex'])
            left_start = get_point_coords(step_data['left_edge'][0])
            left_end = get_point_coords(step_data['left_edge'][1])
            right_start = get_point_coords(step_data['right_edge'][0])
            right_end = get_point_coords(step_data['right_edge'][1])
            
            if apex_coord:
                current_apex = Dot(point=apex_coord, color=RED, radius=0.12)
                self.play(Create(current_apex))
            
            if left_start and left_end:
                current_funnel_left = Line(start=left_start, end=left_end, color=GREEN, stroke_width=4)
                self.play(Create(current_funnel_left))
            
            if right_start and right_end:
                current_funnel_right = Line(start=right_start, end=right_end, color=ORANGE, stroke_width=4)
                self.play(Create(current_funnel_right))
            
            # Add path segment if needed
            if step_data.get('adds_path_segment'):
                path_start = get_point_coords(step_data['path_segment'][0])
                path_end = get_point_coords(step_data['path_segment'][1])
                if path_start and path_end:
                    path_line = Line(start=path_start, end=path_end, color=RED, stroke_width=6)
                    path_segments.add(path_line)
                    self.play(Create(path_line))
            
            self.next_slide()
        
        # Thêm đoạn cuối từ B₁ đến A₁
        b1_coord = get_point_coords("B₁")
        a1_coord = get_point_coords("A₁")
        if b1_coord and a1_coord:
            final_segment = Line(start=b1_coord, end=a1_coord, color=RED, stroke_width=6)
            path_segments.add(final_segment)
            self.play(Create(final_segment))
        
        self.next_slide()
        
        # Clear funnel elements
        if current_funnel_left:
            self.play(FadeOut(current_funnel_left))
        if current_funnel_right:
            self.play(FadeOut(current_funnel_right))
        if current_apex:
            self.play(FadeOut(current_apex))
        
        # Final result theo phân tích Hà Minh Trường (chính xác)
        final_text = Text("Result according to HMT analysis (accurate):", font_size=16, color=WHITE, weight=BOLD)
        result_text = Text("Shortest Path: A → U₁ → E → E₁ → C₁ → B₁ → A₁ (7 points)", 
                          font_size=14, color=YELLOW)
        segments_text = Text("5 apex changes, 6 path segments", font_size=12, color=WHITE)
        
        final_group = VGroup(final_text, result_text, segments_text)
        final_group.arrange(DOWN, buff=0.3)
        final_group.to_edge(DOWN, buff=0.5)
        
        self.play(Write(final_group))
        
        # Make path more prominent
        self.play(path_segments.animate.set_stroke_width(8))
        
        self.wait(3)

pass