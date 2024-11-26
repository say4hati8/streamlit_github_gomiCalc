import streamlit as st
import trimesh
import numpy as np

# Streamlit app title
st.title("3D STL Volume Calculator with Ground Plane")

# File uploader to upload STL file
uploaded_file = st.file_uploader("Upload an STL file", type=["stl"])

if uploaded_file is not None:
    try:
        # Load the mesh using trimesh
        mesh = trimesh.load_mesh(uploaded_file, file_type='stl')
        
        # Check if the mesh is watertight (closed)
        if not mesh.is_watertight:
            st.error("The 3D model is not watertight (closed). Please upload a closed STL file.")
        else:
            # Calculate the volume of the mesh in cubic centimeters
            volume_cm3 = mesh.volume
            
            # Create a plane to cover the ground
            # Assuming the ground plane is at z=0
            plane_height = 0  # Ground level
            plane_size = mesh.bounds[1][0] - mesh.bounds[0][0]  # Width of the mesh
            plane = trimesh.creation.box(extents=[plane_size, plane_size, 0.01])  # Thin plane
            
            # Position the plane at the ground level
            plane.apply_translation([mesh.centroid[0], mesh.centroid[1], plane_height])
            
            # Combine the original mesh and the plane
            combined_mesh = trimesh.util.concatenate([mesh, plane])
            
            # Calculate the new volume
            new_volume_cm3 = combined_mesh.volume
            
            # Convert volume to cubic meters
            volume_m3 = new_volume_cm3 / 1_000_000  # 1 ㎥ = 1,000,000 ㎤

            # Display the volume in cubic meters
            st.success(f"Volume of the 3D model with ground plane: {volume_m3:.6f} ㎥")
    except Exception as e:
        st.error(f"Error loading the STL file: {e}")
else:
    st.info("Please upload an STL file to calculate its volume.")
