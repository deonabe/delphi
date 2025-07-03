const express = require('express');
const cors = require('cors');
const { exec } = require('child_process');
const app = express();
const port = 3001;

app.use(cors());

app.get('/metrics/:protocol', (req, res) => {
  const protocol = req.params.protocol;
  exec(`python3 scripts/metrics.py ${protocol}`, (error, stdout, stderr) => {
    if (error) return res.status(500).send('Python script error');
    res.send(JSON.parse(stdout));
  });
});

app.get('/summary/:protocol', (req, res) => {
  const protocol = req.params.protocol;
  exec(`python3 scripts/summary.py ${protocol}`, (error, stdout, stderr) => {
    if (error) return res.status(500).send('GPT summary error');
    res.send(stdout);
  });
});

app.listen(port, () => {
  console.log(`Backend API running on http://localhost:${port}`);
});
