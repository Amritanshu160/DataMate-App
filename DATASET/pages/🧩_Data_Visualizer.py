import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Plotly All-in-One Plotter", layout="wide", page_icon="🧩")
st.title("\U0001F4C8 Universal Plotly Plotter (2D + 3D)")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset Loaded Successfully!")

    cols = df.columns.tolist()

    tab2d, tab3d = st.tabs(["2D Plots", "3D Plots"])

    with tab2d:
        st.subheader("2D Plot Settings")
        x_axis = st.selectbox("Select X-axis", cols, key="2d_x")
        y_axis = st.selectbox("Select Y-axis", cols, key="2d_y")
        color = st.selectbox("Select Color (Optional)", [None] + cols, key="2d_color")

        sequential_colorscales = [
        "Viridis", "Cividis", "Plasma", "Inferno", "Magma", "Turbo",
        "Blues", "Greens", "Greys", "Oranges", "Purples", "Reds",
        "YlGnBu", "YlOrRd", "YlGn", "OrRd", "PuBuGn"
        ]

        diverging_colorscales = [
        "RdBu", "RdYlBu", "RdYlGn", "Spectral", "PiYG", "PRGn",
        "BrBG", "PuOr", "RdGy", "RdBu_r"
        ]
        cyclic_colorscales = [
        "twilight", "hsv", "phase"
        ]

        misc_colorscales = [
        "Jet", "Rainbow", "Hot", "Cool", "Spring",
        "Summer", "Winter", "Copper", "Earth", "IceFire"
        ]

        all_colorscales = (
        sequential_colorscales +
        diverging_colorscales +
        cyclic_colorscales +
        misc_colorscales
        )

        colorscale = st.selectbox("Select a Colorscale (Available only for Heatmaps)", all_colorscales)

        plot_types_2d = [
            "Scatter", "Line", "Bar", "Histogram", "Box", "Violin", "Area", "Pie", "Sunburst", "Treemap",
            "Funnel", "Polar Scatter", "Polar Bar", "Parallel Coordinates", "Heatmap", "Density Contour", "Density Heatmap"
        ]
        plot_choice_2d = st.selectbox("Select 2D Plot Type", plot_types_2d)

        if st.button("Generate 2D Plot"):
            fig = None

            if plot_choice_2d == "Scatter":
                fig = px.scatter(df, x=x_axis, y=y_axis, color=color)
            elif plot_choice_2d == "Line":
                fig = px.line(df, x=x_axis, y=y_axis, color=color)
            elif plot_choice_2d == "Bar":
                fig = px.bar(df, x=x_axis, y=y_axis, color=color)
            elif plot_choice_2d == "Histogram":
                fig = px.histogram(df, x=x_axis, color=color)
            elif plot_choice_2d == "Box":
                fig = px.box(df, x=x_axis, y=y_axis, color=color)
            elif plot_choice_2d == "Violin":
                fig = px.violin(df, x=x_axis, y=y_axis, color=color)
            elif plot_choice_2d == "Area":
                fig = px.area(df, x=x_axis, y=y_axis, color=color)
            elif plot_choice_2d == "Pie":
                fig = px.pie(df, names=x_axis, values=y_axis, color=color)
            elif plot_choice_2d == "Sunburst":
                fig = px.sunburst(df, path=[x_axis, y_axis], values=color if color else y_axis)
            elif plot_choice_2d == "Treemap":
                fig = px.treemap(df, path=[x_axis, y_axis], values=color if color else y_axis)
            elif plot_choice_2d == "Funnel":
                fig = px.funnel(df, x=x_axis, y=y_axis, color=color)
            elif plot_choice_2d == "Polar Scatter":
                fig = px.scatter_polar(df, r=y_axis, theta=x_axis, color=color)
            elif plot_choice_2d == "Polar Bar":
                fig = px.bar_polar(df, r=y_axis, theta=x_axis, color=color)
            elif plot_choice_2d == "Parallel Coordinates":
                fig = px.parallel_coordinates(df, dimensions=[x_axis, y_axis, color] if color else [x_axis, y_axis])
            elif plot_choice_2d == "Heatmap":
                fig = px.density_heatmap(df, x=x_axis, y=y_axis, color_continuous_scale=colorscale)
            elif plot_choice_2d == "Density Contour":
                fig = px.density_contour(df, x=x_axis, y=y_axis, color=color)
            elif plot_choice_2d == "Density Heatmap":
                fig = px.density_heatmap(df, x=x_axis, y=y_axis, color_continuous_scale=colorscale)

            if fig:
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("Failed to generate the plot. Please check your selections.")

    with tab3d:
        st.subheader("3D Plot Settings")
        x_axis_3d = st.selectbox("Select X-axis", cols, key="3d_x")
        y_axis_3d = st.selectbox("Select Y-axis", cols, key="3d_y")
        z_axis_3d = st.selectbox("Select Z-axis", cols, key="3d_z")
        color_3d = st.selectbox("Select Color (Optional, only available for 3D Scatter and Line Plot)", [None] + cols, key="3d_color")

        sequential_colorscales = [
        "Viridis", "Cividis", "Plasma", "Inferno", "Magma", "Turbo",
        "Blues", "Greens", "Greys", "Oranges", "Purples", "Reds",
        "YlGnBu", "YlOrRd", "YlGn", "OrRd", "PuBuGn"
        ]

        diverging_colorscales = [
        "RdBu", "RdYlBu", "RdYlGn", "Spectral", "PiYG", "PRGn",
        "BrBG", "PuOr", "RdGy", "RdBu_r"
        ]
        cyclic_colorscales = [
        "twilight", "hsv", "phase"
        ]

        misc_colorscales = [
        "Jet", "Rainbow", "Hot", "Cool", "Spring",
        "Summer", "Winter", "Copper", "Earth", "IceFire"
        ]

        all_colorscales = (
        sequential_colorscales +
        diverging_colorscales +
        cyclic_colorscales +
        misc_colorscales
        )


        colorscale = st.selectbox("Select a Colorscale (Available for 3D Surface, Mesh, Volume, Cone, Streamtube, Isosurface)", all_colorscales)

        plot_types_3d = [
            "3D Scatter", "3D Line", "3D Surface", "3D Mesh", "3D Volume", "3D Cone", "3D Streamtube", "3D Isosurface"
        ]
        plot_choice_3d = st.selectbox("Select 3D Plot Type", plot_types_3d)

        if st.button("Generate 3D Plot"):
            fig = None

            if plot_choice_3d == "3D Scatter":
                fig = px.scatter_3d(df, x=x_axis_3d, y=y_axis_3d, z=z_axis_3d, color=color_3d)
            elif plot_choice_3d == "3D Line":
                fig = px.line_3d(df, x=x_axis_3d, y=y_axis_3d, z=z_axis_3d, color=color_3d)
            elif plot_choice_3d == "3D Surface":
                fig = go.Figure(data=go.Surface(z=df.pivot_table(index=x_axis_3d, columns=y_axis_3d, values=z_axis_3d).values, colorscale=colorscale))
            elif plot_choice_3d == "3D Mesh":
                fig = go.Figure(data=[go.Mesh3d(x=df[x_axis_3d], y=df[y_axis_3d], z=df[z_axis_3d], colorscale=colorscale, intensity=df[z_axis_3d])])
            elif plot_choice_3d == "3D Volume":
                fig = go.Figure(data=go.Volume(x=df[x_axis_3d], y=df[y_axis_3d], z=df[z_axis_3d], value=df[z_axis_3d], isomin=0, isomax=1, colorscale=colorscale))
            elif plot_choice_3d == "3D Cone":
                fig = go.Figure(data=go.Cone(x=df[x_axis_3d], y=df[y_axis_3d], z=df[z_axis_3d], u=df[x_axis_3d], v=df[y_axis_3d], w=df[z_axis_3d], colorscale=colorscale))
            elif plot_choice_3d == "3D Streamtube":
                fig = go.Figure(data=go.Streamtube(x=df[x_axis_3d], y=df[y_axis_3d], z=df[z_axis_3d], u=df[x_axis_3d], v=df[y_axis_3d], w=df[z_axis_3d], colorscale=colorscale))
            elif plot_choice_3d == "3D Isosurface":
                fig = go.Figure(data=go.Isosurface(x=df[x_axis_3d], y=df[y_axis_3d], z=df[z_axis_3d], value=df[z_axis_3d], colorscale=colorscale))

            if fig:
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("Failed to generate the plot. Please check your selections.")