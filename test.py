import streamlit as st
import trimesh

# Streamlit app title
st.title("3D STL Volume Calculator")

# File uploader to upload STL file
uploaded_file = st.file_uploader("Upload an STL file", type=["stl"])

if uploaded_file is not None:
    try:
        # Load the mesh using trimesh
        mesh = trimesh.load_mesh(uploaded_file, file_type='stl')
        
        # Calculate the volume of the mesh in cubic centimeters
        volume_cm3 = mesh.volume
        
        # Convert volume to cubic meters
        volume_m3 = volume_cm3 / 1_000_000  # 1 ㎥ = 1,000,000 ㎤

        # Display the volume in cubic meters
        st.success(f"Volume of the 3D model: {volume_m3:.6f} ㎥")
    except Exception as e:
        st.error(f"Error loading the STL file: {e}")
else:
    st.info("Please upload an STL file to calculate its volume.")
