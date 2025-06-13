const express = require('express');
const router = express.Router();
const db = require('../models/db');
const { predictHeartDisease } = require('../ml_model/predict');

router.post('/', async (req, res) => {
  try {
    const { username, ...inputData } = req.body;
    
    // Save user if not exists
    const userRes = await db.query(
      'INSERT INTO users (username) VALUES ($1) ON CONFLICT (username) DO UPDATE SET username = EXCLUDED.username RETURNING id',
      [username]
    );
    const userId = userRes.rows[0].id;

    // Get prediction
    const prediction = await predictHeartDisease(inputData);

    // Save prediction
    await db.query(
      `INSERT INTO predictions (
        user_id, age, sex, cp, trestbps, chol, fbs, restecg, thalch, exang, 
        oldpeak, slope, ca, thal, prediction, risk_percentage
      ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16)`,
      [
        userId,
        inputData.age,
        inputData.sex,
        inputData.cp,
        inputData.trestbps,
        inputData.chol,
        inputData.fbs,
        inputData.restecg,
        inputData.thalch,
        inputData.exang,
        inputData.oldpeak,
        inputData.slope,
        inputData.ca,
        inputData.thal,
        prediction.prediction,
        prediction.risk_percentage
      ]
    );

    res.render('result', { prediction });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Prediction failed' });
  }
});

module.exports = router;