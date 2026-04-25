<!-- README.md for Task 2 -->
<h1 align="center">📈 Stock Price Prediction (Next Day Close)</h1>

<p align="center">
  <img src="https://img.icons8.com/color/96/000000/stocks.png"/>
  <br>
  <i>Forecasting Apple’s closing price using regression models</i>
</p>

<hr>

<h2>🎯 Objective</h2>
<p>Use historical stock data (Open, High, Low, Volume) to predict the <strong>next day's closing price</strong> and compare Linear Regression vs Random Forest.</p>

<hr>

<h2>📁 Data Source</h2>
<ul>
  <li><strong>Library</strong>: <code>yfinance</code></li>
  <li><strong>Ticker</strong>: AAPL (Apple Inc.)</li>
  <li><strong>Period</strong>: 2018-01-01 to 2024-01-01</li>
  <li><strong>Records</strong>: 1509 trading days</li>
</ul>

<hr>

<h2>⚙️ Methodology</h2>

<h3>Feature & Target Definition</h3>
<pre style="background:#f4f4f4; padding:10px; border-left:4px solid #2196F3;">
X = ['High', 'Low', 'Open', 'Volume']
y = 'Close'
</pre>

<h3>Train/Test Split</h3>
<p><code>test_size = 20</code> (random_state=42) — <em>Note: random split used for regression practice; real time‑series would require chronological split.</em></p>

<h3>Models Used</h3>
<ul>
  <li><strong>Linear Regression</strong> – fast, interpretable</li>
  <li><strong>Random Forest Regressor</strong> – captures non‑linear patterns</li>
</ul>

<hr>

<h2>📊 Results</h2>

<table style="width:100%; border-collapse: collapse; text-align:center;">
  <tr style="background:#333; color:white;">
    <th>Model</th><th>R² (Train)</th><th>R² (Test)</th>
  </tr>
  <tr><td>Linear Regression</td><td>0.99977</td><td>0.99977</td></tr>
  <tr><td>Random Forest</td><td>0.99994</td><td>0.99977</td></tr>
</table>

<p>✅ Both models achieve near‑perfect scores because <code>High, Low, Open</code> are extremely correlated with <code>Close</code>.</p>

<hr>

<h2>📉 Actual vs Predicted Plot</h2>
<p align="center">
  <img src="https://i.imgur.com/placeholder.png" alt="Actual vs Predicted scatter" width="80%">
  <br>
  <em>Points lie almost exactly on the diagonal line → excellent prediction.</em>
</p>

<hr>

<h2>📦 Dependencies</h2>
<pre style="background:#2d2d2d; color:#eee; padding:10px; border-radius:6px;">
yfinance
pandas
matplotlib
seaborn
scikit-learn
</pre>

<hr>

<h2>⚠️ Limitations & Future Work</h2>
<ul>
  <li>Random split ignores time order → use <code>TimeSeriesSplit</code> or chronological split.</li>
  <li>Add technical indicators (RSI, MACD, moving averages).</li>
  <li>Try LSTM or Prophet for true forecasting.</li>
</ul>

<hr>

<h2>🏁 Conclusion</h2>
<p>Linear Regression and Random Forest can predict next‑day closing price with extremely high accuracy when using highly correlated features. However, careful validation respecting time series nature is essential for real‑world trading.</p>

<hr>
<p align="center">📅 Built with Python & yfinance</p>