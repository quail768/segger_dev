import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Define method colors
method_colors = {
    "segger": "#D55E00",
    # 'segger_n0': '#E69F00',
    # 'segger_n1': '#F0E442',
    # 'segger_embedding': '#C72228',
    "Baysor": "#000075",
    # 'Baysor_n0': '#0F4A9C',
    # 'Baysor_n1': '#0072B2',
    "10X": "#8B008B",
    "10X-nucleus": "#CC79A7",
    # 'BIDCell': '#009E73'
}

# Define the path to your figures and data
# figures_path = Path("/path/to/your/figures")  # Update with the actual path
cell_counts_path = figures_path / "cell_counts_data.csv"
cell_area_log2_path = figures_path / "cell_area_log2_data.csv"
mcer_box_path = figures_path / "mcer_box.csv"
sensitivity_boxplot_data = figures_path / "sensitivity_results.csv"

# Load the data
cell_counts_data = pd.read_csv(cell_counts_path)
cell_area_log2_data = pd.read_csv(cell_area_log2_path)
sensitivity_boxplot_data = pd.read_csv(sensitivity_boxplot_data)

# Cell counts barplot
cell_counts_data.rename(columns={"Unnamed: 0": "Method"}, inplace=True)
cell_counts_data = cell_counts_data[~cell_counts_data["Method"].isin(["segger_n0", "segger_n1"])]


sensitivity_results.csv


# Finally, the MCER plot

mcer_methods_final = method_colors.keys()
mcer_data_filtered = mcer_box_data[mcer_box_data["Segmentation Method"].isin(mcer_methods_final)]


import seaborn as sns
import matplotlib.pyplot as plt


sns.set_style("white")
sns.set_context("paper", font_scale=1.2)


mcer_methods_final = method_colors.keys()
cell_area_log2_data = cell_area_log2_data[cell_area_log2_data["Segmentation Method"].isin(mcer_methods_final)]

# Create the boxplot with the size 4x6 inches and show only the outliers
plt.figure(figsize=(2, 4))
sns.boxplot(
    data=cell_area_log2_data,
    x="Segmentation Method",
    y="Cell Area (log2)",
    palette=method_colors,
    showfliers=False,
    showcaps=False,
    flierprops={"marker": "x"},
)  # Hide the default outliers in the boxplot

# Add a stripplot to show only the outliers
# sns.stripplot(data=mcer_data_filtered,
#               x='Segmentation Method',
#               y='MECR',
#               jitter=False,       # Avoid jittering to keep points in place
#               dodge=True,         # Keep points aligned with the boxplot categories
#               marker="D",         # Use diamond-shaped marker
#               edgecolor='black',  # Set black edge color for the points
#               linewidth=1,        # Define the thickness of the point borders
#               color='black',      # Set the color of the outlier points
#               size=6)             # Set the size of the outliers

# Rotate the x-axis labels
plt.xticks(rotation=45, ha="right")

# Setting solid black borders on all four sides
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color("black")  # Set border color to black

# plt.ylim(0, 0.2)

# Show horizontal grid lines
ax.yaxis.grid(False)
ax.xaxis.grid(False)

# Adding the y-axis label with "Mutually Exclusive Co-expression Rate (MECR)"
plt.ylabel(r"Cell Area ($\mu m^2$)")

# Remove the x-axis label
ax.set_xlabel("")

# Create a clean layout for publication-level
plt.tight_layout()

# Save the updated plot as both PNG and PDF
cell_areas_boxplot_pdf_path = figures_path / "cell_areas.pdf"
cell_areas_boxplot_png_path = figures_path / "cell_areas.png"

plt.savefig(cell_areas_boxplot_pdf_path, format="pdf", bbox_inches="tight", dpi=300)
plt.savefig(cell_areas_boxplot_png_path, format="png", bbox_inches="tight", dpi=300)

# Close the figure
plt.close()


mcer_methods_final = method_colors.keys()
sensitivity_boxplot_data = sensitivity_boxplot_data[
    sensitivity_boxplot_data["Segmentation Method"].isin(mcer_methods_final)
]


plt.figure(figsize=(2.5, 4))
sns.boxplot(
    data=sensitivity_boxplot_data,
    x="Segmentation Method",
    y="Sensitivity",
    palette=method_colors,
    showfliers=False,
    showcaps=False,
    flierprops={"marker": "x"},
)  # Hide the default outliers in the boxplot

# Add a stripplot to show only the outliers
# sns.stripplot(data=mcer_data_filtered,
#               x='Segmentation Method',
#               y='MECR',
#               jitter=False,       # Avoid jittering to keep points in place
#               dodge=True,         # Keep points aligned with the boxplot categories
#               marker="D",         # Use diamond-shaped marker
#               edgecolor='black',  # Set black edge color for the points
#               linewidth=1,        # Define the thickness of the point borders
#               color='black',      # Set the color of the outlier points
#               size=6)             # Set the size of the outliers

# Rotate the x-axis labels
plt.xticks(rotation=45, ha="right")

# Setting solid black borders on all four sides
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color("black")  # Set border color to black

# plt.ylim(0, 0.2)

# Show horizontal grid lines
ax.yaxis.grid(False)
ax.xaxis.grid(False)

# Adding the y-axis label with "Mutually Exclusive Co-expression Rate (MECR)"
plt.ylabel(r"Positive Marker Expression Rate (PMER)")

# Remove the x-axis label
ax.set_xlabel("")

# Create a clean layout for publication-level
plt.tight_layout()

# Save the updated plot as both PNG and PDF
sensitivity_boxplot_data_boxplot_pdf_path = figures_path / "sensitivity_boxplot_data.pdf"
sensitivity_boxplot_data_boxplot_png_path = figures_path / "sensitivity_boxplot_data.png"

plt.savefig(sensitivity_boxplot_data_boxplot_pdf_path, format="pdf", bbox_inches="tight", dpi=300)
plt.savefig(sensitivity_boxplot_data_boxplot_png_path, format="png", bbox_inches="tight", dpi=300)

# Close the figure
plt.close()


sns.set_style("white")
sns.set_context("paper")

# Create the boxplot with the size 4x6 inches and show only the outliers
plt.figure(figsize=(2.5, 4))
sns.boxplot(
    data=mcer_data_filtered,
    x="Segmentation Method",
    y="MECR",
    palette=method_colors,
    showfliers=False,
    showcaps=False,
    flierprops={"marker": "x"},
)  # Hide the default outliers in the boxplot

# Add a stripplot to show only the outliers
# sns.stripplot(data=mcer_data_filtered,
#               x='Segmentation Method',
#               y='MECR',
#               jitter=False,       # Avoid jittering to keep points in place
#               dodge=True,         # Keep points aligned with the boxplot categories
#               marker="D",         # Use diamond-shaped marker
#               edgecolor='black',  # Set black edge color for the points
#               linewidth=1,        # Define the thickness of the point borders
#               color='black',      # Set the color of the outlier points
#               size=6)             # Set the size of the outliers

# Rotate the x-axis labels
plt.xticks(rotation=45, ha="right")

# Setting solid black borders on all four sides
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color("black")  # Set border color to black

plt.ylim(0, 0.2)

# Show horizontal grid lines
ax.yaxis.grid(False)
ax.xaxis.grid(False)

# Adding the y-axis label with "Mutually Exclusive Co-expression Rate (MECR)"
plt.ylabel("Mutually Exclusive Co-expression Rate")

# Remove the x-axis label
ax.set_xlabel("")

# Create a clean layout for publication-level
plt.tight_layout()

# Save the updated plot as both PNG and PDF
final_mcer_boxplot_pdf_path = figures_path / "mcer_boxplot_with_outliers.pdf"
final_mcer_boxplot_png_path = figures_path / "mcer_boxplot_with_outliers.png"

plt.savefig(final_mcer_boxplot_pdf_path, format="pdf", bbox_inches="tight", dpi=300)
plt.savefig(final_mcer_boxplot_png_path, format="png", bbox_inches="tight", dpi=300)

# Close the figure
plt.close()
