<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Energy Efficiency Predictor</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --muted:#9aa6b2;
      --accent:#60a5fa;
      --accent-2:#7c3aed;
      --text:#e6eef6;
    }
    html,body{height:100%;}
    body{
      margin:0;
      font-family:Inter, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background:linear-gradient(180deg,#071428 0%, #081226 45%, #06111b 100%);
      color:var(--text);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      line-height:1.5;
      padding:32px;
    }
    .container{
      max-width:960px;
      margin:0 auto;
      background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius:12px;
      box-shadow: 0 8px 30px rgba(2,6,23,0.6);
      padding:28px;
      border:1px solid rgba(255,255,255,0.03);
    }
    header{
      display:flex;
      align-items:center;
      gap:18px;
      margin-bottom:18px;
    }
    header h1{
      margin:0;
      font-size:22px;
      letter-spacing:-0.2px;
    }
    .meta{
      color:var(--muted);
      font-size:13px;
    }
    .badge{
      display:inline-block;
      background:linear-gradient(90deg,var(--accent),var(--accent-2));
      padding:6px 10px;
      border-radius:999px;
      font-weight:600;
      font-size:13px;
      color:white;
    }

    section{
      margin-top:18px;
      padding:18px;
      background:rgba(255,255,255,0.02);
      border-radius:10px;
      border:1px solid rgba(255,255,255,0.01);
    }
    h2{margin:0 0 10px 0; font-size:18px;}
    h3{margin:12px 0 8px 0; font-size:15px;}
    p{color:var(--muted);}
    ul{margin:8px 0 0 20px; color:var(--muted);}
    pre.code{
      background:#071122;
      color:#cfe9ff;
      padding:14px;
      border-radius:8px;
      overflow:auto;
      font-size:13px;
      border:1px solid rgba(255,255,255,0.03);
    }

    .two-col{
      display:grid;
      grid-template-columns:1fr 1fr;
      gap:18px;
    }

    .center{
      text-align:center;
    }

    .button {
      display:inline-block;
      margin-top:10px;
      background:linear-gradient(90deg,var(--accent),var(--accent-2));
      color:white;
      padding:10px 14px;
      border-radius:8px;
      text-decoration:none;
      font-weight:600;
    }

    footer{
      margin-top:18px;
      color:var(--muted);
      font-size:13px;
      text-align:center;
    }

    @media (max-width:720px){
      .two-col{grid-template-columns:1fr;}
      body{padding:18px;}
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div>
        <h1>🏠 Energy Efficiency of Buildings (Green Building Analysis)</h1>
        <div class="meta">Edunet X Shell Internship — 4 weeks</div>
      </div>
      <div style="margin-left:auto" class="center">
        <span class="badge">ML • Data Analysis • Deployment</span>
      </div>
    </header>

    <!-- Provided snippet with the Launch App link -->
    <section>
      <h2>Project Snapshot</h2>
      <p>This project predicts Heating and Cooling Loads of buildings using Machine Learning.</p>
      <p>Visit the live app here:
        <a class="button" href="https://energy-efficiency-green-building-aman-pandey.streamlit.app/" target="_blank" rel="noopener noreferrer">
          Launch App
        </a>
      </p>
    </section>

    <!-- Weekly breakdown -->
    <section>
      <h2>Weekly Timeline</h2>

      <h3>Week 1</h3>
      <ul>
        <li>Defined the problem statement and project scope</li>
        <li>Collected and explored the dataset (<code>ENB2012_data.xlsx</code>)</li>
        <li>Preprocessed the data (renamed columns, checked missing values)</li>
        <li>Created feature distribution plots and a correlation heatmap</li>
        <li>Plotted <strong>Relative Compactness vs Heating Load</strong> to visualize its impact</li>
        <li>Split the dataset into <strong>Train and Test</strong> sets</li>
      </ul>

      <h3>Week 2</h3>
      <ul>
        <li>Selected <strong>Linear Regression</strong> as baseline algorithm</li>
        <li>Trained two separate models:
          <ul>
            <li><strong>Heating Load Model (Y1)</strong></li>
            <li><strong>Cooling Load Model (Y2)</strong></li>
          </ul>
        </li>
        <li>Evaluated using: <strong>MSE, RMSE, R²</strong></li>
        <li>Plotted <strong>Actual vs Predicted</strong> for both targets</li>
      </ul>

      <h3>Week 3</h3>
      <ul>
        <li>Implemented advanced algorithms: Decision Trees, Random Forests, Gradient Boosting (XGBoost/LightGBM)</li>
        <li>Compared model performance vs baseline</li>
        <li>Tuned hyperparameters (GridSearchCV / RandomizedSearchCV)</li>
      </ul>

      <h3>Week 4</h3>
      <ul>
        <li>Final evaluation on test data and selected best model</li>
        <li>Built an interactive Streamlit app for predictions</li>
        <li>Prepared project documentation and final report</li>
      </ul>
    </section>

    <!-- Pipeline and why it matters -->
    <section>
      <h2>Project Pipeline</h2>
      <ol>
        <li>Define the Problem</li>
        <li>Data Collection & Understanding</li>
        <li>Data Preprocessing</li>
        <li>Data Splitting</li>
        <li>Algorithm Selection</li>
        <li>Model Training</li>
        <li>Model Evaluation</li>
        <li>Model Optimization</li>
        <li>Final Evaluation on Test Data</li>
        <li>Model Deployment</li>
      </ol>

      <h3>Why this matters</h3>
      <p>
        Heating and cooling are the largest contributors to building energy consumption.
        Identifying how features like <strong>compactness, surface area, wall area,</strong> and <strong>glazing ratio</strong>
        affect loads enables design choices that reduce energy use while preserving comfort.
      </p>
    </section>

    <!-- Results and project structure -->
    <section>
      <h2>Results & Insights</h2>
      <ul>
        <li><strong>Compact buildings</strong> require less heating energy</li>
        <li><strong>Glazing area & surface area</strong> strongly influence cooling loads</li>
        <li>Advanced models (Random Forest / Gradient Boosting) outperform Linear Regression baseline</li>
      </ul>

      <h2>Project Structure</h2>
      <pre class="code">
📦 Energy-Efficiency-Buildings
 ┣ 📜 ENB2012_data.xlsx        # Dataset
 ┣ 📜 app.py                   # Streamlit deployment file
 ┣ 📜 analysis.ipynb           # Jupyter Notebook (data analysis & modeling)
 ┣ 📜 requirements.txt         # Python dependencies
 ┣ 📜 README.md                # Project Report
      </pre>
    </section>

    <!-- Commands -->
    <section>
      <h2>Quick Setup & Commands</h2>
      <p>Clone and run locally:</p>
      <pre class="code">
# clone
git clone https://github.com/your-username/energy-efficiency-buildings.git
cd energy-efficiency-buildings

# install dependencies
pip install -r requirements.txt

# run Streamlit app
python -m streamlit run app.py
      </pre>
    </section>

    <footer>
      <div>Created by <strong>Aman</strong> — Edunet X Shell Internship</div>
      <div style="margin-top:8px;color:var(--muted);font-size:12px">
        Last updated: <!-- You can manually update this date before uploading --> 2025-09-13
      </div>
    </footer>
  </div>
</body>
</html>