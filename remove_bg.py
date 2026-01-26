from PIL import Image

def remove_background():
    img_path = "docs/assets/images/logo.png"
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    # Get the background color from the top-left corner
    bg_color = pixels[0, 0]
    
    # BFS Flood Fill to remove background
    queue = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
    visited = set(queue)
    
    # Ensure corners are actually background before starting
    # (In case the logo touches the corner, but usually logos have padding)
    # We assume (0,0) is definitely background.
    
    # We need to normalize bg_color comparison (ignore alpha if present in source but unlikely for png without alpha)
    target_color = bg_color
    
    while queue:
        x, y = queue.pop(0)
        
        # Make transparent
        pixels[x, y] = (0, 0, 0, 0)
        
        # Check neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited:
                    # If the neighbor matches the target background color, add to queue
                    # Use a small tolerance if needed, but for pixel art exact match is usually best
                    # However, if there's compression artifacts, we might need tolerance.
                    # Given it's a PNG logo, exact match should work.
                    if pixels[nx, ny] == target_color:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
    
    img.save(img_path)
    print(f"Processed {img_path}: Background removed.")

if __name__ == "__main__":
    remove_background()
