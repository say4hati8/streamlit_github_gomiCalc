import streamlit as st
import trimesh

# Streamlit app title
st.title("3D STL Volume Calculator")

# File uploader to upload STL file
uploaded_file = st.file_uploader("Upload an STL file", type=["stl"])

if uploaded_file is not None:
    try:
        # Load the mesh using trimesh
        mesh = trimesh.load(uploaded_file, file_type='stl')
        
        # Display mesh information
        st.info(f"Number of vertices: {len(mesh.vertices)}")
        st.info(f"Number of faces: {len(mesh.faces)}")
        
        # Calculate the volume of the mesh
        volume = mesh.volume
        
        # Display the volume
        st.success(f"Volume of the 3D model: {volume*1000}L")
    except Exception as e:
        st.error(f"Error loading the STL file: {e}")
else:
    st.info("Please upload an STL file to calculate its volume.")
