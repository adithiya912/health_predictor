const { Pool } = require('pg');

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'healthrisk',
  password: 'Adithiya@2005',
  port: 5432,
});

module.exports = {
  query: (text, params) => pool.query(text, params),
};