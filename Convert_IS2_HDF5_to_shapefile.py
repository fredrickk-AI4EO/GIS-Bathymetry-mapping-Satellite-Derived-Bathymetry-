Conversation opened. 1 unread message.

Skip to content
Using Gmail with screen readers
1 of 208
convert_IS2_HDF5_to_shapefile.py
Inbox

fredrick kariuki <fredrickkariuki716@gmail.com>
Attachments
3:49 PM (2 minutes ago)
to me

 One attachment
  •  Scanned by Gmail
import h5py
import pandas as pd
import arcpy
import os

'''
TO USE:
- Go to Analysis tab of ArcGIS Pro
- Click on the Python drop-down, and select Python Notebook
- Copy this code and paste it into the first cell of the notebook
- Copy the file path to the ICESat-2 HDF5 you have downloaded
- Set the filepath to the output shapefile you want to save
- Adjust the min_confidence parameter as desired
- Click the "play"/Run this cell button to run the code
- The python code will convert the HDF5 ICESat-2 points into a shapefile and add the points to your map
- Repeat as needed for each HDF5 file
'''

# ================= CONFIGURATION =================
# 1. Input: Path to your ATL24 HDF5 file
## e.g.: r"C:\Users\me\Downloads\ATL24_20241102020949_07142514_006_01_001_01_subsetted.h5"
file_path = r""

# 2. Output: Path for the resulting Shapefile
## e.g.: r"C:\Users\me\data\test3.shp"
output_shp = r""

# 3. Filters
## Highest quality is 1.0, lowest is 0, > 0.6 is acceptable
min_confidence = 0.6  # Keep bathymetry data strictly > min_confidence
# =================================================

def process_beam(f, beam_id, conf_threshold):
    """
    Extracts and filters data for a single beam.
    Returns a DataFrame or None if no valid data found.
    """
    # --- GROUP PATH ---
    group = f"/{beam_id}"
    
    if group not in f:
        print(f"  [Skipping] {beam_id}: Group not found.")
        return None

    try:
        # [cite_start]--- READ VARIABLES [cite: 5, 6] ---
        # Coordinates
        lats = f[f"{group}/lat_ph"][:]
        lons = f[f"{group}/lon_ph"][:]
        
        # [cite_start]Heights for Depth Calculation [cite: 6]
        surface_h = f[f"{group}/surface_h"][:]
        ortho_h   = f[f"{group}/ortho_h"][:]
        
        # [cite_start]Classification (40=Bathymetry) [cite: 5]
        classes = f[f"{group}/class_ph"][:]
        
        # [cite_start]Confidence (0.0 to 1.0) [cite: 5]
        confidence = f[f"{group}/confidence"][:]
        
    except KeyError as e:
        print(f"  [Error] {beam_id}: Missing variable {e}")
        return None

    # --- CALCULATE DEPTH ---
    # Logic: Surface Height - Bottom Height (Unchanged)
    depths = surface_h - ortho_h

    # --- CREATE DATAFRAME ---
    df = pd.DataFrame({
        'Latitude': lats,
        'Longitude': lons,
        'Depth': depths,
        'Class': classes,
        'Confidence': confidence
    })
    
    # --- ADD BEAM ATTRIBUTE ---
    # This adds the beam name (e.g. 'gt1l') to every row
    df['Beam'] = beam_id

    # --- FILTERING ---
    # [cite_start]1. Filter for Bathymetry Only (Class 40) [cite: 5]
    df = df[df['Class'] == 40].copy()
    
    # 2. Filter for Confidence > threshold
    df = df[df['Confidence'] > conf_threshold].copy()
    
    # 3. Clean up NaN depths
    df = df.dropna(subset=['Depth'])

    count = len(df)
    if count > 0:
        print(f"  [Success] {beam_id}: {count} points recovered.")
        return df
    else:
        print(f"  [Skipping] {beam_id}: No points matched filters.")
        return None

# --- MAIN EXECUTION ---
print(f"Opening file: {os.path.basename(file_path)}")

beam_list = ['gt1l', 'gt1r', 'gt2l', 'gt2r', 'gt3l', 'gt3r']
all_dfs = []

with h5py.File(file_path, 'r') as f:
    for beam in beam_list:
        df_beam = process_beam(f, beam, min_confidence)
        if df_beam is not None:
            all_dfs.append(df_beam)

# Combine all beams
if all_dfs:
    print("Merging data from all beams...")
    df_final = pd.concat(all_dfs, ignore_index=True)
    
    # 1. Save temp CSV
    temp_csv = file_path.replace(".h5", "_temp_allbeams.csv")
    df_final.to_csv(temp_csv, index=False)
    
    # 2. Convert to Shapefile
    print(f"Converting {len(df_final)} total points to Shapefile...")
    
    if arcpy.Exists(output_shp):
        arcpy.management.Delete(output_shp)

    arcpy.management.XYTableToPoint(
        in_table=temp_csv,
        out_feature_class=output_shp,
        x_field="Longitude",
        y_field="Latitude",
        z_field="Depth",
        coordinate_system=arcpy.SpatialReference(4326)
    )
    
    # Cleanup
    if os.path.exists(temp_csv):
        os.remove(temp_csv)
    
    print(f"Success! Shapefile created at: {output_shp}")
    print("Attributes included: Depth, Class, Confidence, Beam")

else:
    print("Process stopped: No valid data found in any beam.")
convert_IS2_HDF5_to_shapefile.py
Displaying convert_IS2_HDF5_to_shapefile.py.
