import os
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageOps

def create_wood_texture(width, height, wood_type="walnut", is_end_grain=False, angle=0.0):
    """
    Generates high-fidelity, photorealistic wood grain textures procedurally.
    """
    # Create coordinate grid
    y_indices, x_indices = np.indices((height, width))
    
    if is_end_grain:
        # Concentric growth rings centered off-screen to simulate log cut
        cx, cy = -width * 0.4, height * 0.5
        dx = x_indices - cx
        dy = y_indices - cy
        r = np.sqrt(dx**2 + dy**2)
        
        # Warp the radius slightly using sine waves for realistic wobbles in growth rings
        theta = np.arctan2(dy, dx)
        warp = np.sin(theta * 12) * 8 + np.cos(theta * 5) * 4
        warped_r = r + warp
        
        if wood_type == "maple":
            # Creamy light-amber tones for maple end-grain
            base_col = np.array([238, 224, 202])
            ring_col = np.array([214, 194, 168])
            
            # Growth rings
            ring_pattern = np.sin(warped_r * 0.08)
            ring_pattern = (ring_pattern + 1) / 2
            ring_pattern = np.power(ring_pattern, 1.2)
            
            color = base_col[None, None, :] * (1 - ring_pattern[:, :, None] * 0.12)
            color += ring_col[None, None, :] * ring_pattern[:, :, None] * 0.12
            
            # Add subtle radial medullary rays
            ray_pattern = np.abs(np.sin(theta * 60))
            ray_pattern = np.power(ray_pattern, 20)
            color += (np.array([255, 245, 230]) - color) * ray_pattern[:, :, None] * 0.15
            
        else:  # walnut
            # Deep rich dark brown with purplish-grey tones
            base_col = np.array([62, 42, 28])
            ring_col = np.array([34, 20, 12])
            
            ring_pattern = np.sin(warped_r * 0.06)
            ring_pattern = (ring_pattern + 1) / 2
            ring_pattern = np.power(ring_pattern, 3.0) # Sharp growth ring transition
            
            color = base_col[None, None, :] * (1 - ring_pattern[:, :, None] * 0.3)
            color += ring_col[None, None, :] * ring_pattern[:, :, None] * 0.3
            
            # Large, distinct walnut pores in end-grain
            pore_noise = np.random.rand(height, width)
            pore_mask = (pore_noise > 0.96) & (np.sin(warped_r * 0.12) > 0.0)
            color[pore_mask] = np.array([25, 15, 8])
            
    else:
        # Longitudinal side grain
        # Rotate/shear coordinates if needed
        c, s = np.cos(angle), np.sin(angle)
        nx = x_indices * c - y_indices * s
        ny = x_indices * s + y_indices * c
        
        # Warp the coordinates vertically to create organic wiggles in the grain
        warp_y = ny + np.sin(nx * 0.015) * 15 + np.sin(ny * 0.005) * 30
        warp_x = nx + np.sin(ny * 0.01) * 20
        
        if wood_type == "walnut":
            # Walnut side grain: beautiful dark cocoa brown with elegant flowing bands
            base_col = np.array([68, 48, 33])
            ring_col = np.array([38, 24, 14])
            pore_col = np.array([82, 60, 44])
            
            # Wide organic growth bands
            band_pattern = np.sin(warp_x * 0.012)
            band_pattern = (band_pattern + 1) / 2
            band_pattern = np.power(band_pattern, 2.2)
            
            color = base_col[None, None, :] * (1 - band_pattern[:, :, None] * 0.35)
            color += ring_col[None, None, :] * band_pattern[:, :, None] * 0.35
            
            # Fine longitudinal pores (stretched vertical fibers)
            fiber_noise = np.random.rand(height // 2, width)
            fiber_img = Image.fromarray((fiber_noise * 255).astype(np.uint8))
            fiber_img = fiber_img.resize((width, height), Image.Resampling.BILINEAR)
            fiber_val = np.array(fiber_img.filter(ImageFilter.GaussianBlur(radius=0.8))) / 255.0
            
            # Warp the fiber mask to follow the grain wiggles
            fiber_warp = (warp_x * 0.8).astype(int) % width
            y_coords = np.arange(height)[:, None]
            fiber_mask = fiber_val[y_coords, fiber_warp]
            pore_mask = (fiber_mask > 0.65) * 0.12
            color = color * (1 - pore_mask[:, :, None]) + pore_col[None, None, :] * pore_mask[:, :, None]
            
        elif wood_type == "maple":
            # Maple side grain: tight, clean cream and soft gold waves
            base_col = np.array([244, 230, 208])
            ring_col = np.array([225, 206, 178])
            
            # Very subtle, straight growth bands
            band_pattern = np.sin(warp_x * 0.008)
            band_pattern = (band_pattern + 1) / 2
            band_pattern = np.power(band_pattern, 1.5)
            
            color = base_col[None, None, :] * (1 - band_pattern[:, :, None] * 0.08)
            color += ring_col[None, None, :] * band_pattern[:, :, None] * 0.08
            
            # Soft fine grain lines
            fiber_noise = np.random.rand(height // 3, width)
            fiber_img = Image.fromarray((fiber_noise * 255).astype(np.uint8))
            fiber_img = fiber_img.resize((width, height), Image.Resampling.BILINEAR)
            fiber_val = np.array(fiber_img.filter(ImageFilter.GaussianBlur(radius=0.5))) / 255.0
            
            fiber_warp = (warp_x * 1.5).astype(int) % width
            y_coords = np.arange(height)[:, None]
            fiber_mask = fiber_val[y_coords, fiber_warp]
            color += (np.array([255, 245, 230]) - color) * (fiber_mask[:, :, None] > 0.7) * 0.04
            
        else: # yellowheart
            # Vibrant, lustrous golden-yellow grain
            base_col = np.array([238, 185, 45])
            ring_col = np.array([208, 150, 22])
            
            band_pattern = np.sin(warp_x * 0.015)
            band_pattern = (band_pattern + 1) / 2
            band_pattern = np.power(band_pattern, 1.8)
            
            color = base_col[None, None, :] * (1 - band_pattern[:, :, None] * 0.15)
            color += ring_col[None, None, :] * band_pattern[:, :, None] * 0.15
            
            # Soft golden pore highlights
            fiber_noise = np.random.rand(height // 2, width)
            fiber_img = Image.fromarray((fiber_noise * 255).astype(np.uint8))
            fiber_img = fiber_img.resize((width, height), Image.Resampling.BILINEAR)
            fiber_val = np.array(fiber_img.filter(ImageFilter.GaussianBlur(radius=0.6))) / 255.0
            
            fiber_warp = (warp_x * 1.2).astype(int) % width
            y_coords = np.arange(height)[:, None]
            fiber_mask = fiber_val[y_coords, fiber_warp]
            color += (np.array([255, 215, 90]) - color) * (fiber_mask[:, :, None] > 0.6) * 0.08
            
    # Clip values to valid range
    color = np.clip(color, 0, 255).astype(np.uint8)
    return Image.fromarray(color)

def main():
    # Setup dimensions
    width, height = 1600, 1200
    
    # 1. Generate core textures
    print("Generating procedural wood grain textures...")
    left_maple_bg = create_wood_texture(width, height, "maple", is_end_grain=False, angle=-0.08)
    right_walnut_bg = create_wood_texture(width, height, "walnut", is_end_grain=False, angle=0.03)
    
    walnut_endgrain = create_wood_texture(width, height, "walnut", is_end_grain=True)
    maple_endgrain = create_wood_texture(width, height, "maple", is_end_grain=True)
    
    yellowheart_inlay_tex = create_wood_texture(width, height, "yellowheart", is_end_grain=False, angle=0.15)
    maple_inlay_tex = create_wood_texture(width, height, "maple", is_end_grain=False, angle=-0.12)
    
    # 2. Build the basic 3D corner layout
    # Corner line runs vertically at x = 450
    corner_x = 450
    pin_height = 120
    
    # Create the master composite image
    img = Image.new("RGBA", (width, height))
    
    # Fill background faces
    # Left face (Maple tapa, compressed horizontally to simulate 3D skew)
    left_face_mask = Image.new("L", (width, height), 0)
    draw_l = ImageDraw.Draw(left_face_mask)
    draw_l.rectangle([0, 0, corner_x, height], fill=255)
    
    # Compress left maple texture horizontally for perspective
    left_maple_skew = left_maple_bg.resize((int(corner_x * 2.5), height)).crop((0, 0, corner_x, height))
    img.paste(left_maple_skew, (0, 0))
    
    # Right face (Walnut side panel)
    right_face_mask = Image.new("L", (width, height), 0)
    draw_r = ImageDraw.Draw(right_face_mask)
    draw_r.rectangle([corner_x, 0, width, height], fill=255)
    img.paste(right_walnut_bg, (0, 0), right_face_mask)
    
    # 3. Interlocking Box Joints (Alternating Walnut & Maple Pins)
    # y ranges from 0 to 1200, so we have 10 pins of 120px height
    print("Drawing interlocking box joint pins...")
    
    # Mask and Draw context for hairline joint lines
    lines_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw_lines = ImageDraw.Draw(lines_img)
    
    # Joint geometry
    left_pin_end = 370   # Where Walnut pins end on Maple left board
    right_pin_end = 530  # Where Maple pins end on Walnut right board
    
    for i in range(10):
        y_start = i * pin_height
        y_end = (i + 1) * pin_height
        
        # Hairline glue line color (subtle dark brown/charcoal)
        glue_col = (27, 19, 12, 220)
        
        if i % 2 == 0:
            # EVEN PINS:
            # - Left face shows Maple (part of left board, so it goes all the way to corner_x)
            # - Right face shows Maple END GRAIN (pin of left board extending through right board)
            pin_mask = Image.new("L", (width, height), 0)
            draw_p = ImageDraw.Draw(pin_mask)
            draw_p.rectangle([corner_x, y_start, right_pin_end, y_end], fill=255)
            img.paste(maple_endgrain, (0, 0), pin_mask)
            
            # Draw hairline joints around this pin
            draw_lines.line([corner_x, y_start, right_pin_end, y_start], fill=glue_col, width=1)
            draw_lines.line([right_pin_end, y_start, right_pin_end, y_end], fill=glue_col, width=1)
            draw_lines.line([corner_x, y_end, right_pin_end, y_end], fill=glue_col, width=1)
            
        else:
            # ODD PINS:
            # - Left face shows Walnut END GRAIN (pin of right board extending through left board)
            # - Right face shows Walnut (part of right board, so it goes all the way to corner_x)
            pin_mask = Image.new("L", (width, height), 0)
            draw_p = ImageDraw.Draw(pin_mask)
            draw_p.rectangle([left_pin_end, y_start, corner_x, y_end], fill=255)
            img.paste(walnut_endgrain, (0, 0), pin_mask)
            
            # Draw hairline joints around this pin
            draw_lines.line([left_pin_end, y_start, corner_x, y_start], fill=glue_col, width=1)
            draw_lines.line([left_pin_end, y_start, left_pin_end, y_end], fill=glue_col, width=1)
            draw_lines.line([left_pin_end, y_end, corner_x, y_end], fill=glue_col, width=1)
            
    # Paste hairline joint lines
    img = Image.alpha_composite(img.convert("RGBA"), lines_img)
    
    # 4. Generate the Geometric Inlay (Seated in Walnut side panel)
    print("Generating geometric inlay on side panel...")
    
    # Inlay coordinates (centered in walnut panel)
    center_x, center_y = 1050, 600
    
    # Define Diamond geometry
    # Vertices: North, East, South, West
    outer_diamond_pts = [(center_x, 180), (center_x + 400, center_y), (center_x, 1020), (center_x - 400, center_y)]
    mid_diamond_pts = [(center_x, 215), (center_x + 365, center_y), (center_x, 985), (center_x - 365, center_y)]
    inner_diamond_pts = [(center_x, 250), (center_x + 330, center_y), (center_x, 950), (center_x - 330, center_y)]
    
    # Create layer masks and paste inlays
    # A. Outer Maple Diamond Band
    outer_maple_mask = Image.new("L", (width, height), 0)
    draw_om = ImageDraw.Draw(outer_maple_mask)
    draw_om.polygon(outer_diamond_pts, fill=255)
    draw_om.polygon(mid_diamond_pts, fill=0)
    img.paste(maple_inlay_tex, (0, 0), outer_maple_mask)
    
    # B. Inner Yellowheart Diamond Band
    inner_yh_mask = Image.new("L", (width, height), 0)
    draw_iy = ImageDraw.Draw(inner_yh_mask)
    draw_iy.polygon(mid_diamond_pts, fill=255)
    draw_iy.polygon(inner_diamond_pts, fill=0)
    img.paste(yellowheart_inlay_tex, (0, 0), inner_yh_mask)
    
    # C. Center Compass Star Design
    # 8-point geometric star inside the inner diamond
    p_n = (center_x, 320)
    p_s = (center_x, 880)
    p_e = (center_x + 280, center_y)
    p_w = (center_x - 280, center_y)
    
    # Inner vertices for star wiggles
    i_ne = (center_x + 85, center_y - 85)
    i_se = (center_x + 85, center_y + 85)
    i_sw = (center_x - 85, center_y + 85)
    i_nw = (center_x - 85, center_y - 85)
    
    # List of 8 triangles: (points, wood_type)
    triangles = [
        # North points
        ([ (center_x, center_y), p_n, i_ne ], "maple"),
        ([ (center_x, center_y), p_n, i_nw ], "yellowheart"),
        # South points
        ([ (center_x, center_y), p_s, i_se ], "yellowheart"),
        ([ (center_x, center_y), p_s, i_sw ], "maple"),
        # East points
        ([ (center_x, center_y), p_e, i_ne ], "yellowheart"),
        ([ (center_x, center_y), p_e, i_se ], "maple"),
        # West points
        ([ (center_x, center_y), p_w, i_nw ], "maple"),
        ([ (center_x, center_y), p_w, i_sw ], "yellowheart")
    ]
    
    inlay_lines = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw_inlay_lines = ImageDraw.Draw(inlay_lines)
    inlay_glue_col = (19, 13, 8, 240)
    
    for pts, wood in triangles:
        t_mask = Image.new("L", (width, height), 0)
        draw_t = ImageDraw.Draw(t_mask)
        draw_t.polygon(pts, fill=255)
        
        tex = maple_inlay_tex if wood == "maple" else yellowheart_inlay_tex
        img.paste(tex, (0, 0), t_mask)
        
        # Hairline joinery lines around star triangles
        draw_inlay_lines.polygon(pts, outline=inlay_glue_col)
        
    # Draw hairline joints around the diamond borders
    draw_inlay_lines.polygon(outer_diamond_pts, outline=inlay_glue_col)
    draw_inlay_lines.polygon(mid_diamond_pts, outline=inlay_glue_col)
    draw_inlay_lines.polygon(inner_diamond_pts, outline=inlay_glue_col)
    
    # Paste inlay hairline lines
    img = Image.alpha_composite(img.convert("RGBA"), inlay_lines)
    
    # 5. Shading, routed pocket depth, and physical transitions
    print("Applying depth-shading to routed inlay pockets...")
    # To create a realistic recess/bevel for the routed pocket transition:
    # We can create a mask of the entire inlay and apply an inner shadow.
    inlay_mask = Image.new("L", (width, height), 0)
    draw_im = ImageDraw.Draw(inlay_mask)
    draw_im.polygon(outer_diamond_pts, fill=255)
    
    # Dilate and blur the inlay mask to create soft inner/outer shading
    inlay_blur = inlay_mask.filter(ImageFilter.GaussianBlur(radius=4))
    inlay_np = np.array(inlay_blur) / 255.0
    inlay_orig = np.array(inlay_mask) / 255.0
    
    # Edge gradient (3D bevel/shadow effect)
    # This simulates low-angle raking light hitting the routed transition edge
    # Let's say light comes from top-right, so bottom-left edges are highlighted
    # and top-right edges are in shadow.
    edge_gradient = inlay_orig - inlay_np
    edge_gradient = np.clip(edge_gradient, 0, 1)
    
    # Shadow map (raking light shadow in the routed pocket)
    shadow_map = np.zeros((height, width))
    # Simple offset to represent shadow cast by pocket edge
    offset_y, offset_x = 3, -3
    shifted_inlay = np.roll(inlay_orig, shift=(offset_y, offset_x), axis=(0, 1))
    pocket_shadow = np.clip(inlay_orig - shifted_inlay, 0, 1)
    pocket_shadow = Image.fromarray((pocket_shadow * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=2))
    pocket_shadow_np = np.array(pocket_shadow) / 255.0
    
    img_np = np.array(img).astype(float)
    # Apply pocket shadow (darken)
    img_np[:, :, :3] = img_np[:, :, :3] * (1.0 - pocket_shadow_np[:, :, None] * 0.45)
    
    # Apply subtle micro-bevel highlight (on the light-facing edge)
    bevel_highlight = np.roll(inlay_orig, shift=(-2, 2), axis=(0, 1)) - inlay_orig
    bevel_highlight = np.clip(bevel_highlight, 0, 1)
    bevel_highlight = Image.fromarray((bevel_highlight * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=1))
    bevel_highlight_np = np.array(bevel_highlight) / 255.0
    img_np[:, :, :3] += (255.0 - img_np[:, :, :3]) * bevel_highlight_np[:, :, None] * 0.4
    
    # 6. Apply Raking Low-Angle Light and Satin Finish Micro-Sheen
    print("Applying raking low-angle light and satin micro-sheen...")
    
    # Raking light gradient across the whole image (brightest in top-right, darker bottom-left)
    y_idx, x_idx = np.indices((height, width))
    light_gradient = (x_idx / width + (height - y_idx) / height) / 2.0
    # Center the light range to preserve colors but add drama
    light_map = 0.75 + 0.4 * light_gradient
    
    # Add satin micro-sheen:
    # Wood grain sheen depends on light angle. We can use the high-frequency wood textures
    # to modulate a soft specular sheen.
    # We generate a specular map using a warped highlight
    specular_map = np.power(light_gradient, 2.5) * 0.18
    # Modulate specular sheen with fine pores (giving that micro-sheen texture)
    noise_sheen = np.random.rand(height, width)
    sheen = specular_map * (0.8 + 0.2 * noise_sheen)
    
    img_np[:, :, :3] = img_np[:, :, :3] * light_map[:, :, None]
    img_np[:, :, :3] += (255.0 - img_np[:, :, :3]) * sheen[:, :, None]
    
    # Physical Corner shading along x = corner_x to make the 3D corner feel alive
    # Left face is angled away, so it should be slightly darker overall (shadow side)
    # Right face is facing more towards the raking light
    corner_shadow = np.zeros((height, width))
    # Soft vertical shadow on the left side of the corner line
    for dx in range(1, 150):
        # Quadratic falloff going left from corner_x
        val = 0.28 * (1.0 - (dx / 150.0))**2
        corner_shadow[:, corner_x - dx] = val
        
    # Soft highlight on the right side of the corner line
    corner_highlight = np.zeros((height, width))
    for dx in range(1, 60):
        val = 0.15 * (1.0 - (dx / 60.0))**2
        corner_highlight[:, corner_x + dx] = val
        
    img_np[:, :, :3] = img_np[:, :, :3] * (1.0 - corner_shadow[:, :, None])
    img_np[:, :, :3] += (255.0 - img_np[:, :, :3]) * corner_highlight[:, :, None]
    
    # Convert back to image
    img = Image.fromarray(np.clip(img_np, 0, 255).astype(np.uint8))
    
    # 7. Apply Shallow Depth of Field (DoF)
    print("Applying professional shallow depth of field (DoF) blur...")
    # Focal region is a sharp vertical band around the inlay-joint boundary (x = 450 to 900)
    # Everything else (far left x=0 and far right x=1600) transitions to a beautiful blur.
    # The blur is strongest at the corners.
    
    # Create the DoF blur map
    dof_map = np.zeros((height, width), dtype=float)
    focal_x = 650  # Center of razor-sharp focus
    focal_y = 600
    
    # Calculate distance from focal center
    dx = x_idx - focal_x
    dy = y_idx - focal_y
    dist = np.sqrt((dx * 0.9)**2 + (dy * 0.5)**2) # horizontal spread is wider
    
    # DoF mask: 0 in focal region, 255 in background
    dof_mask = (dist - 150) / 450.0
    dof_mask = np.clip(dof_mask, 0.0, 1.0)
    # Smooth transition
    dof_mask = 3 * dof_mask**2 - 2 * dof_mask**3
    
    # Generate multi-stage blur for high-quality DoF simulation
    img_blur_mid = img.filter(ImageFilter.GaussianBlur(radius=5))
    img_blur_high = img.filter(ImageFilter.GaussianBlur(radius=14))
    
    # Blend sharp, mid-blur and high-blur
    dof_mask_img = Image.fromarray((dof_mask * 255).astype(np.uint8))
    
    # Blend sharp with mid-blur
    img_mid_blended = Image.composite(img_blur_mid, img, dof_mask_img)
    # Blend with high-blur for outer edges
    outer_dof_mask = np.clip((dist - 400) / 500.0, 0.0, 1.0)
    outer_dof_mask = 3 * outer_dof_mask**2 - 2 * outer_dof_mask**3
    outer_dof_mask_img = Image.fromarray((outer_dof_mask * 255).astype(np.uint8))
    
    final_img = Image.composite(img_blur_high, img_mid_blended, outer_dof_mask_img)
    
    # Save the final image
    output_path = "/mnt/c/Users/Tony/Documents/GitHub/instruments/percussion/cajon/images/macro/finger-joint-inlay-corner.png"
    
    # Ensure parent directories exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save as PNG
    final_img.save(output_path, "PNG")
    print(f"SUCCESS: Image saved to {output_path}")

if __name__ == "__main__":
    main()
