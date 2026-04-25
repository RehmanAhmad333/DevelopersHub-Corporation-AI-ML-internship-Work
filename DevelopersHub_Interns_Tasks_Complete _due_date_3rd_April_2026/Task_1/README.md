<!-- README.md for Task 1 -->
<h1 align="center">🌸 Iris Dataset Exploration & Visualization</h1>

<p align="center">
  <img src="https://img.icons8.com/color/96/000000/flower.png"/>
  <br>
  <i>Understanding data trends through EDA and visual storytelling</i>
</p>

<hr>

<h2>📌 Objective</h2>
<p>Learn how to load, inspect, and visualize a dataset to uncover patterns, distributions, and relationships — using the classic <strong>Iris Dataset</strong>.</p>

<hr>

<h2>📊 Dataset Overview</h2>
<table style="width:100%; border-collapse: collapse; background:#f9f9f9;">
  <tr style="background:#4CAF50; color:white;"><th>Property</th><th>Value</th></tr>
  <tr><td>Name</td><td>Iris (Fisher’s Iris)</td></tr>
  <tr><td>Samples</td><td>150</td></tr>
  <tr><td>Features</td><td>SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm</td></tr>
  <tr><td>Target</td><td>Species (Setosa, Versicolor, Virginica)</td></tr>
  <tr><td>Missing Values</td><td>None</td></tr>
</table>

<hr>

<h2>🛠️ Steps Performed</h2>

<h3>1. Data Loading & Inspection</h3>
<ul>
  <li>Loaded <code>Iris.csv</code> using <strong>pandas</strong>.</li>
  <li>Printed shape → <code>(150, 6)</code> (extra <code>Id</code> column).</li>
  <li>Displayed column names & first 5 rows (<code>.head()</code>).</li>
  <li>Used <code>.info()</code> → no nulls, mixed data types.</li>
  <li>Used <code>.describe()</code> → statistical summary.</li>
</ul>

<h3>2. Data Visualization</h3>
<table style="width:100%; border:1px solid #ddd;">
  <tr style="background:#ddd;"><th>Plot Type</th><th>Purpose</th><th>Insight</th></tr>
  <tr><td>Scatter Plot</td><td>SepalLength vs PetalLength</td><td>Positive correlation, clear species separation</td></tr>
  <tr><td>Histogram + KDE</td><td>Distribution of SepalLength</td><td>Approximately normal, slight skew</td></tr>
  <tr><td>Box Plot</td><td>Identify outliers across all features</td><td>SepalWidth has mild outliers</td></tr>
  <tr><td>Pair Plot</td><td>All feature relationships</td><td>Petal features are highly discriminative</td></tr>
</table>

<hr>

<h2>📈 Sample Visualizations</h2>
<p align="center">
  <img src="scatter.png" alt="Scatter plot" width="45%">
  <br>
  <img src="box.png" alt="Boxplot" width="45%">
</p>
<p><em>(Actual plots generated in code)</em></p>

<hr>

<h2>🧰 Tools & Libraries</h2>
<pre style="background:#2d2d2d; color:#ccc; padding:10px; border-radius:8px;">
pandas        → data manipulation
matplotlib    → base plotting
seaborn       → statistical visualizations
</pre>

<hr>

<h2>🏁 Conclusion</h2>
<p>✅ The Iris dataset is clean and well-balanced.<br>
✅ Petal measurements are more powerful for classification than sepal measurements.<br>
✅ Basic EDA + visualisation is essential before any machine learning.</p>

<hr>
<p align="center">Made with ❤️ using Python & seaborn</p>