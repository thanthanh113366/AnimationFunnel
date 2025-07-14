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
        self.slide6()
        
        #Slide 7: Funnel algorithm step by step
        self.slide7()

        #Slide 8: Funnel algorithm in real world
        # self.slide8()
    
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
        title = Text("Tính chất đường đi ngắn nhất trong đa giác đơn", font_size=28, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        
        # Show the original image scaled to fit better
        self.img = ImageMobject("map/map.png").scale(0.6)   
        self.img.move_to(LEFT * 1.5)
        
        # Create vector representation from slide4 data
        scale_factor = 0.99
        origin_x = self.img.get_left()[0]
        origin_y = self.img.get_bottom()[1]
        
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
        example_labels = ["T₁", "E", "F", "K", "R₁", "E₁", "D₁", "A", "A₁"]
        for label in example_labels:
            coords = get_point_coords(label)
            if coords:
                point = Dot(point=coords, color=RED, radius=0.08)
                point_label = Text(label, font_size=12, color=WHITE, weight=BOLD)
                point_label.next_to(point, UP, buff=0.1)
                key_vertices.add(point, point_label)
        
        # Property explanation
        property_text = VGroup()
        prop_title = Text("Tính chất:", font_size=18, weight=BOLD, color=YELLOW)
        prop_desc = Text("Đường đi ngắn nhất là chuỗi các đoạn thẳng\nvới đỉnh là đỉnh của đa giác", 
                        font_size=14, color=WHITE)
        property_text.add(prop_title)
        property_text.add(prop_desc.next_to(prop_title, DOWN, buff=0.2, aligned_edge=LEFT))
        property_text.move_to(self.img.get_right() + RIGHT * 2.5)
        
        # Animate the slide
        self.play(Write(title))
        self.next_slide()
        
        self.play(Create(polygon_lines))
        self.next_slide()
        
        self.play(FadeIn(property_text))
        self.next_slide()
        
        self.play(Create(key_vertices))
        self.next_slide()
        
        # Example 1: T₁ to E (direct edge)
        example1_title = Text("Ví dụ 1: T₁ → E", font_size=16, weight=BOLD, color=GREEN)
        example1_desc = Text("Đường đi ngắn nhất: T₁E (1 cạnh)", font_size=12, color=WHITE)
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
        
        # Example 2: T₁ to K (via E, F)
        example2_title = Text("Ví dụ 2: T₁ → K", font_size=16, weight=BOLD, color=ORANGE)
        example2_desc = Text("Đường đi ngắn nhất: T₁EFK", font_size=12, color=WHITE)
        example2_text = VGroup(example2_title, example2_desc.next_to(example2_title, DOWN, buff=0.1, aligned_edge=LEFT))
        example2_text.move_to(example1_text.get_center() + DOWN * 0.8)
        
        # Draw path T₁ → E → F → K
        f_coords = get_point_coords("F")
        k_coords = get_point_coords("K")
        if t1_coords and e_coords and f_coords and k_coords:
            path2_1 = Line(start=t1_coords, end=e_coords, color=ORANGE, stroke_width=4)
            path2_2 = Line(start=e_coords, end=f_coords, color=ORANGE, stroke_width=4)
            path2_3 = Line(start=f_coords, end=k_coords, color=ORANGE, stroke_width=4)
            path2 = VGroup(path2_1, path2_2, path2_3)
        
        if t1_coords and e_coords:
            self.play(FadeOut(path1))
        self.play(FadeIn(example2_text))
        if t1_coords and e_coords and f_coords and k_coords:
            self.play(Create(path2))
        self.next_slide()
        
        # Example 3: R₁ to D₁ (via E₁)
        example3_title = Text("Ví dụ 3: R₁ → D₁", font_size=16, weight=BOLD, color=PURPLE)
        example3_desc = Text("Đường đi ngắn nhất: R₁E₁D₁", font_size=12, color=WHITE)
        example3_text = VGroup(example3_title, example3_desc.next_to(example3_title, DOWN, buff=0.1, aligned_edge=LEFT))
        example3_text.move_to(example2_text.get_center() + DOWN * 0.8)
        
        # Draw path R₁ → E₁ → D₁
        r1_coords = get_point_coords("R₁")
        e1_coords = get_point_coords("E₁")
        d1_coords = get_point_coords("D₁")
        if r1_coords and e1_coords and d1_coords:
            path3_1 = Line(start=r1_coords, end=e1_coords, color=PURPLE, stroke_width=4)
            path3_2 = Line(start=e1_coords, end=d1_coords, color=PURPLE, stroke_width=4)
            path3 = VGroup(path3_1, path3_2)
        
        if t1_coords and e_coords and f_coords and k_coords:
            self.play(FadeOut(path2))
        self.play(FadeIn(example3_text))
        if r1_coords and e1_coords and d1_coords:
            self.play(Create(path3))
        self.next_slide()
        
        # Problem statement
        problem_title = Text("Bài toán:", font_size=18, weight=BOLD, color=RED)
        problem_desc = Text("Tìm đường đi ngắn nhất từ A đến A₁", font_size=14, color=WHITE)
        problem_text = VGroup(problem_title, problem_desc.next_to(problem_title, DOWN, buff=0.1, aligned_edge=LEFT))
        problem_text.move_to(example3_text.get_center() + DOWN * 1.2)
        
        # Highlight A and A₁
        a_coords = get_point_coords("A")
        a1_coords = get_point_coords("A₁")
        if a_coords and a1_coords:
            highlight_a = Circle(radius=0.15, color=RED, stroke_width=3).move_to(a_coords)
            highlight_a1 = Circle(radius=0.15, color=RED, stroke_width=3).move_to(a1_coords)
        
        if r1_coords and e1_coords and d1_coords:
            self.play(FadeOut(path3))
        self.play(FadeIn(problem_text))
        if a_coords and a1_coords:
            self.play(Create(highlight_a), Create(highlight_a1))
        self.next_slide()
        
        # Clear everything - only clear objects that exist
        fade_objects = [title, polygon_lines, key_vertices, property_text, 
                       example1_text, example2_text, example3_text, problem_text]
        if a_coords and a1_coords:
            fade_objects.extend([highlight_a, highlight_a1])
        self.play(FadeOut(*fade_objects))

    def slide6(self):
        # Title for this slide
        title = Text("Kỹ thuật Funnel", font_size=32, weight=BOLD)
        subtitle = Text("Thuật toán tìm đường đi ngắn nhất trên dãy tam giác liền kề", font_size=18)
        subtitle2 = Text("(1 dạng vector-based map)", font_size=16, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        subtitle.next_to(title, DOWN, buff=0.2)
        subtitle2.next_to(subtitle, DOWN, buff=0.1)
        
        # Points from example.txt (extracted from LaTeX coordinates)
        key_points = [
            (1.3079019630703324, 3.7580327660226813, "A"),
            (3.4303192184181963, 4.662939347760166, "B"),
            (3.282243595952066, 3.165730276158146, "C"),
            (4.549112810384512, 3.5770514496751846, "D"),
            (6.589265831028971, 4.366788102827899, "E"),
            (6.687982912673057, 2.2279180005392982, "F"),
        ]
        
        # Scale and position points for Manim
        scale_factor = 0.8
        
        # Calculate center of polygon for positioning
        center_x = sum(x for x, y, _ in key_points) / len(key_points)
        center_y = sum(y for x, y, _ in key_points) / len(key_points)
        
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
        
        # Create original lines from example.txt
        original_lines = VGroup()
        line_connections = [
            ("A", "B"), ("C", "A"), ("C", "D"), ("B", "E"), ("E", "F"), ("F", "D")
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
        
        # Create triangulation edges BC, BD, DE
        triangulation_edges = VGroup()
        triangulation_connections = [("B", "C"), ("B", "D"), ("D", "E")]
        
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
            apex_label = Text("A (Đỉnh phễu)", font_size=12, color=RED, weight=BOLD)
            apex_label.next_to(funnel_apex, LEFT, buff=0.3)
            funnel_elements.add(funnel_apex, apex_label)
        
        # Left edge of funnel (AB)
        a_coords = get_point_coords("A")
        b_coords = get_point_coords("B")
        if a_coords is not None and b_coords is not None:
            left_edge = Line(start=a_coords, end=b_coords, color=GREEN, stroke_width=4)
            left_label = Text("AB (Cạnh trái)", font_size=12, color=GREEN, weight=BOLD)
            left_label.next_to(left_edge.get_center(), UP, buff=0.2)
            funnel_elements.add(left_edge, left_label)
        
        # Right edge of funnel (AC)
        a_coords = get_point_coords("A")
        c_coords = get_point_coords("C")
        if a_coords is not None and c_coords is not None:
            right_edge = Line(start=a_coords, end=c_coords, color=ORANGE, stroke_width=4)
            right_label = Text("AC (Cạnh phải)", font_size=12, color=ORANGE, weight=BOLD)
            right_label.next_to(right_edge.get_center(), DOWN, buff=0.2)
            funnel_elements.add(right_edge, right_label)
        
        # Create colored triangles in sequence
        triangles = VGroup()
        triangle_data = [
            (["A", "B", "C"], RED, 0.3, "ABC"),
            (["B", "C", "D"], BLUE, 0.3, "BCD"),
            (["B", "D", "E"], GREEN, 0.3, "BDE"),
            (["D", "E", "F"], PURPLE, 0.3, "DEF"),
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
        exp_title = Text("Kỹ thuật Funnel:", font_size=18, weight=BOLD, color=YELLOW)
        exp_desc1 = Text("• Dãy tam giác liền kề: ABC → BCD → BDE → DEF", font_size=12, color=WHITE)
        exp_desc2 = Text("• Đỉnh phễu A với cạnh trái AB, cạnh phải AC", font_size=12, color=WHITE)
        exp_desc3 = Text("• Tìm đường đi ngắn nhất từ A đến F", font_size=12, color=WHITE)
        
        explanation.add(exp_title)
        explanation.add(exp_desc1.next_to(exp_title, DOWN, buff=0.2, aligned_edge=LEFT))
        explanation.add(exp_desc2.next_to(exp_desc1, DOWN, buff=0.1, aligned_edge=LEFT))
        explanation.add(exp_desc3.next_to(exp_desc2, DOWN, buff=0.1, aligned_edge=LEFT))
        explanation.move_to(RIGHT * 4 + UP * 2)
        
        # Legend
        legend = VGroup()
        legend_title = Text("Chú thích:", font_size=14, weight=BOLD)
        
        apex_dot = Dot(color=RED, radius=0.08)
        apex_text = Text("Đỉnh phễu", font_size=10)
        apex_item = VGroup(apex_dot, apex_text.next_to(apex_dot, RIGHT, buff=0.1))
        
        left_line = Line(start=ORIGIN, end=RIGHT*0.3, color=GREEN, stroke_width=4)
        left_text = Text("Cạnh trái", font_size=10)
        left_item = VGroup(left_line, left_text.next_to(left_line, RIGHT, buff=0.1))
        
        right_line = Line(start=ORIGIN, end=RIGHT*0.3, color=ORANGE, stroke_width=4)
        right_text = Text("Cạnh phải", font_size=10)
        right_item = VGroup(right_line, right_text.next_to(right_line, RIGHT, buff=0.1))
        
        triangle_sample = Rectangle(width=0.3, height=0.2, fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE)
        triangle_text = Text("Tam giác hiện tại", font_size=10)
        triangle_item = VGroup(triangle_sample, triangle_text.next_to(triangle_sample, RIGHT, buff=0.1))
        
        edge_line = Line(start=ORIGIN, end=RIGHT*0.3, color=YELLOW, stroke_width=3)
        edge_text = Text("Cạnh liền kề", font_size=10)
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
        for name in ["ABC", "BCD", "BDE", "DEF"]:
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
        title = Text("Thuật toán Funnel - Thực hiện từng bước", font_size=28, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        
        # Points from slide6 (same data)
        key_points = [
            (1.3079019630703324, 3.7580327660226813, "A"),
            (3.4303192184181963, 4.662939347760166, "B"),
            (3.282243595952066, 3.165730276158146, "C"),
            (4.549112810384512, 3.5770514496751846, "D"),
            (6.589265831028971, 4.366788102827899, "E"),
            (6.687982912673057, 2.2279180005392982, "F"),
        ]
        
        # Scale and position points for Manim (same as slide6)
        scale_factor = 0.8
        
        # Calculate center of polygon for positioning
        center_x = sum(x for x, y, _ in key_points) / len(key_points)
        center_y = sum(y for x, y, _ in key_points) / len(key_points)
        
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
        
        # Create original lines from slide6
        original_lines = VGroup()
        line_connections = [
            ("A", "B"), ("C", "A"), ("C", "D"), ("B", "E"), ("E", "F"), ("F", "D")
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
        
        # Funnel algorithm steps
        funnel_steps = [
            {
                "step": 1,
                "description": "Bước 1: Khởi tạo phễu từ tam giác ABC",
                "apex": "A",
                "left_edge": ("A", "B"),
                "right_edge": ("A", "C"),
                "current_triangle": "ABC",
                "adjacent_edge": "BC"
            },
            {
                "step": 2,
                "description": "Bước 2: Xử lý tam giác BCD, cạnh chung BC",
                "apex": "A",
                "left_edge": ("A", "B"),
                "right_edge": ("A", "C"),
                "current_triangle": "BCD",
                "adjacent_edge": "BD",
                "new_point": "D"
            },
            {
                "step": 3,
                "description": "Bước 3: Cập nhật phễu với điểm D",
                "apex": "A",
                "left_edge": ("A", "B"),
                "right_edge": ("A", "D"),
                "current_triangle": "BCD",
                "adjacent_edge": "BD"
            },
            {
                "step": 4,
                "description": "Bước 4: Xử lý tam giác BDE, cạnh chung BD",
                "apex": "A",
                "left_edge": ("A", "B"),
                "right_edge": ("A", "D"),
                "current_triangle": "BDE",
                "adjacent_edge": "DE",
                "new_point": "E"
            },
            {
                "step": 5,
                "description": "Bước 5: Cập nhật phễu với điểm E",
                "apex": "A",
                "left_edge": ("A", "E"),  # left hand AE
                "right_edge": ("A", "D"), # right hand AD
                "current_triangle": "BDE",
                "adjacent_edge": "DE"
                },
                {
                "step": 6,
                "description": "Bước 6: Xử lý tam giác DEF, cạnh chung DE",
                "apex": "A",
                "left_edge": ("A", "E"),  # AE remains left hand
                "right_edge": ("A", "D"), # AD remains right hand before adding F
                "current_triangle": "DEF",
                "adjacent_edge": "EF",
                "new_point": "F"
                },
                {
                "step": 7,
                "description": "Bước 7: Đường đi ngắn nhất A → F",
                "apex": "A",
                "left_edge": ("A", "E"),  # AE stays left
                "right_edge": ("A", "D"), # right hand AD (funnel chain A-D-F)
                "current_triangle": "DEF",
                "path": [("A", "D"), ("D", "F")]
                }
        ]
        
        # Create step information display
        def create_step_info(step_data):
            info = VGroup()
            
            # Step title
            step_title = Text(f"Bước {step_data['step']}", font_size=18, weight=BOLD, color=YELLOW)
            step_desc = Text(step_data['description'], font_size=14, color=WHITE)
            
            # Funnel state
            apex_text = Text(f"Đỉnh phễu: {step_data['apex']}", font_size=12, color=RED)
            left_text = Text(f"Cạnh trái: {step_data['left_edge'][0]}{step_data['left_edge'][1]}", font_size=12, color=GREEN)
            right_text = Text(f"Cạnh phải: {step_data['right_edge'][0]}{step_data['right_edge'][1]}", font_size=12, color=ORANGE)
            
            # Current triangle
            triangle_text = Text(f"Tam giác hiện tại: {step_data['current_triangle']}", font_size=12, color=BLUE)
            
            # Adjacent edge
            if 'adjacent_edge' in step_data:
                edge_text = Text(f"Cạnh liền kề: {step_data['adjacent_edge']}", font_size=12, color=YELLOW)
            else:
                edge_text = Text("", font_size=12)
            
            info.add(step_title)
            info.add(step_desc.next_to(step_title, DOWN, buff=0.2, aligned_edge=LEFT))
            info.add(apex_text.next_to(step_desc, DOWN, buff=0.3, aligned_edge=LEFT))
            info.add(left_text.next_to(apex_text, DOWN, buff=0.1, aligned_edge=LEFT))
            info.add(right_text.next_to(left_text, DOWN, buff=0.1, aligned_edge=LEFT))
            info.add(triangle_text.next_to(right_text, DOWN, buff=0.2, aligned_edge=LEFT))
            info.add(edge_text.next_to(triangle_text, DOWN, buff=0.1, aligned_edge=LEFT))
            
            info.move_to(RIGHT * 4 + UP * 1)
            return info
        
        # Create funnel visualization for a step
        def create_funnel_visual(step_data):
            funnel_visual = VGroup()
            
            # Apex
            apex_coords = get_point_coords(step_data['apex'])
            if apex_coords:
                apex_dot = Dot(point=apex_coords, color=RED, radius=0.12)
                funnel_visual.add(apex_dot)
            
            # Left edge
            left_start = get_point_coords(step_data['left_edge'][0])
            left_end = get_point_coords(step_data['left_edge'][1])
            if left_start is not None and left_end is not None:
                left_line = Line(start=left_start, end=left_end, color=GREEN, stroke_width=4)
                funnel_visual.add(left_line)
            
            # Right edge
            right_start = get_point_coords(step_data['right_edge'][0])
            right_end = get_point_coords(step_data['right_edge'][1])
            if right_start is not None and right_end is not None:
                right_line = Line(start=right_start, end=right_end, color=ORANGE, stroke_width=4)
                funnel_visual.add(right_line)
            
            # Current triangle highlight
            triangle_vertices = list(step_data['current_triangle'])
            triangle_coords = [get_point_coords(v) for v in triangle_vertices]
            valid_triangle_coords = [coord for coord in triangle_coords if coord is not None]
            if len(valid_triangle_coords) == len(triangle_vertices):
                triangle = Polygon(*valid_triangle_coords, fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE, stroke_width=2)
                funnel_visual.add(triangle)
            
            # Adjacent edge highlight
            if 'adjacent_edge' in step_data and len(step_data['adjacent_edge']) == 2:
                edge_start = get_point_coords(step_data['adjacent_edge'][0])
                edge_end = get_point_coords(step_data['adjacent_edge'][1])
                if edge_start is not None and edge_end is not None:
                    edge_line = Line(start=edge_start, end=edge_end, color=YELLOW, stroke_width=3)
                    funnel_visual.add(edge_line)
            
            # Final path
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
        legend_title = Text("Chú thích:", font_size=14, weight=BOLD)
        
        apex_dot = Dot(color=RED, radius=0.08)
        apex_text = Text("Đỉnh phễu", font_size=10)
        apex_item = VGroup(apex_dot, apex_text.next_to(apex_dot, RIGHT, buff=0.1))
        
        left_line = Line(start=ORIGIN, end=RIGHT*0.3, color=GREEN, stroke_width=4)
        left_text = Text("Cạnh trái", font_size=10)
        left_item = VGroup(left_line, left_text.next_to(left_line, RIGHT, buff=0.1))
        
        right_line = Line(start=ORIGIN, end=RIGHT*0.3, color=ORANGE, stroke_width=4)
        right_text = Text("Cạnh phải", font_size=10)
        right_item = VGroup(right_line, right_text.next_to(right_line, RIGHT, buff=0.1))
        
        triangle_sample = Rectangle(width=0.3, height=0.2, fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE)
        triangle_text = Text("Tam giác hiện tại", font_size=10)
        triangle_item = VGroup(triangle_sample, triangle_text.next_to(triangle_sample, RIGHT, buff=0.1))
        
        edge_line = Line(start=ORIGIN, end=RIGHT*0.3, color=YELLOW, stroke_width=3)
        edge_text = Text("Cạnh liền kề", font_size=10)
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
            current_info = create_step_info(step_data)
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
        title = Text("Funnel Algorithm: A to A₁ (Phân tích HMT)", font_size=28, weight=BOLD)
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

        # Funnel Algorithm Steps theo phân tích của Hà Minh Trường (phiên bản chính xác)
        # 5 lần dời đỉnh phễu: A→U₁→E→E₁→C₁→B₁  
        # Đường đi cuối: A → U₁ → E → E₁ → C₁ → B₁ → A₁ (7 points, 6 segments)
        # Tối ưu hiệu suất: 9 bước thay vì 10, hardcode thay vì đọc file
        funnel_steps = [
            {
                "step": 1,
                "description": "Khởi tạo funnel: AC, AU₁",
                "apex": "A",
                "left_edge": ["A", "C"],
                "right_edge": ["A", "U₁"]
            },
            {
                "step": 2,
                "description": "Giai đoạn DT1: U₁D, U₁T₁",
                "apex": "A",
                "left_edge": ["A", "C"],
                "right_edge": ["A", "T₁"],
                "note": "Chuẩn bị dời apex A→U₁"
            },
            {
                "step": 3,
                "description": "🔄 APEX A → U₁: Funnel cuộn, thêm A→U₁",
                "apex": "U₁",
                "left_edge": ["U₁", "D"],
                "right_edge": ["U₁", "T₁"],
                "adds_path_segment": True,
                "path_segment": ["A", "U₁"]
            },
            {
                "step": 4,
                "description": "Giai đoạn KE1: EFK, EE₁",
                "apex": "U₁",
                "left_edge": ["U₁", "E"],
                "right_edge": ["U₁", "E₁"],
                "note": "Chuẩn bị dời apex U₁→E"
            },
            {
                "step": 5,
                "description": "🔄 APEX U₁ → E: Funnel cuộn, thêm U₁→E",
                "apex": "E",
                "left_edge": ["E", "F"],
                "right_edge": ["E", "E₁"],
                "adds_path_segment": True,
                "path_segment": ["U₁", "E"]
            },
            {
                "step": 6,
                "description": "Giai đoạn NB1: E₁N, E₁C₁B₁",
                "apex": "E",
                "left_edge": ["E", "M"],
                "right_edge": ["E", "E₁"],
                "note": "Chuẩn bị dời apex E→E₁"
            },
            {
                "step": 7,
                "description": "🔄 APEX E → E₁: Funnel cuộn, thêm E→E₁",
                "apex": "E₁",
                "left_edge": ["E₁", "N"],
                "right_edge": ["E₁", "C₁"],
                "adds_path_segment": True,
                "path_segment": ["E", "E₁"]
            },
            {
                "step": 8,
                "description": "🔄 APEX E₁ → C₁: A1B1 giai đoạn 1",
                "apex": "C₁",
                "left_edge": ["C₁", "B₁"],
                "right_edge": ["C₁", "A₁"],
                "adds_path_segment": True,
                "path_segment": ["E₁", "C₁"]
            },
            {
                "step": 9,
                "description": "🔄 APEX C₁ → B₁: A1B1 giai đoạn 2",
                "apex": "B₁",
                "left_edge": ["B₁", "A₁"],
                "right_edge": ["B₁", "A₁"],
                "adds_path_segment": True,
                "path_segment": ["C₁", "B₁"]
            }
        ]

        # Step-by-step execution
        current_funnel_left = None
        current_funnel_right = None
        current_apex = None
        path_segments = VGroup()
        step_texts = VGroup()
        
        for step_data in funnel_steps:
            # Create step text với màu sắc phân biệt
            is_apex_change = "🔄 APEX" in step_data['description']
            text_color = RED if is_apex_change else (GREEN if step_data.get('adds_path_segment') else YELLOW)
            
            step_text = Text(f"Bước {step_data['step']}: {step_data['description']}", 
                           font_size=11, color=text_color, weight=BOLD if is_apex_change else NORMAL)
            if step_data['step'] == 1:
                step_text.move_to(RIGHT * 3.2 + UP * 3)
            else:
                step_text.next_to(step_texts[-1], DOWN, buff=0.12)
            step_texts.add(step_text)
            
            # Show step description
            self.play(Write(step_text))
            
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
        final_text = Text("Kết quả theo phân tích HMT (chính xác):", font_size=16, color=WHITE, weight=BOLD)
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
        self.next_slide()
        
        # Cleanup
        fade_objects = [title, polygon_lines, all_points, path_segments, final_group, 
                       step_texts, info_text]
        if a_coord and a1_coord:
            fade_objects.extend([start_circle, goal_circle])
        
        self.play(FadeOut(*fade_objects))

pass