from PIL import Image
import math

def color_distance(c1, c2):
    r1, g1, b1 = c1[:3]
    r2, g2, b2 = c2[:3]
    return math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)

def remove_background():
    img_path = "docs/assets/images/logo_original.png" # Read from original backup
    out_path = "docs/assets/images/logo.png"
    
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    # Get background color from top-left
    bg_color = pixels[0, 0]
    
    # Tolerance threshold (0-255). 
    # 50 is generous enough to catch "dark grey" artifacts but keep colored pixels.
    # For a black background, anything close to black should go.
    TOLERANCE = 50 
    
    # BFS Flood Fill with tolerance
    queue = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
    visited = set(queue)
    
    while queue:
        x, y = queue.pop(0)
        
        # Check current pixel distance to background color
        current_color = pixels[x, y]
        dist = color_distance(current_color, bg_color)
        
        if dist < TOLERANCE:
            # Make transparent
            pixels[x, y] = (0, 0, 0, 0)
            
            # Check neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < width and 0 <= ny < height:
                    if (nx, ny) not in visited:
                        neighbor_color = pixels[nx, ny]
                        neighbor_dist = color_distance(neighbor_color, bg_color)
                        
                        # Only add to queue if it's also background-ish
                        if neighbor_dist < TOLERANCE:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
    
    img.save(out_path)
    print(f"Processed {out_path} with tolerance {TOLERANCE}.")

if __name__ == "__main__":
    remove_background()