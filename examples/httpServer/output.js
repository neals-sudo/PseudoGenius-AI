// require necessary modules for the server
const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg');

// create a new express application
const app = express();

// use body-parser middleware to handle json payloads
app.use(bodyParser.json());

// create a new pool of connections for the PostgreSQL database
const pool = new Pool({
  connectionString: 'postgres://admin:pass@localhost/test?sslmode=disable'
});

// start the HTTP server on port 8080
app.listen(8080, () => {
  console.log('Server started on port 8080');
});

// handle POST requests to the /api/create route
app.post('/api/create', async (req, res) => {
  const { username, password } = req.body;

  // ensure username and password are valid
  if (!username || !password) {
    return res.status(400).send('Invalid parameters');
  }

  // insert new user record into PostgreSQL
  try {
    await pool.query('INSERT INTO users (username, password) VALUES ($1, $2)', [username, password]);
    return res.status(200).send('User created');
  } catch (err) {
    console.error(err);
    return res.status(500).send('Error creating user');
  }
});

// handle PUT requests to the /api/password_change route
app.put('/api/password_change', async (req, res) => {
  const { username, newpassword } = req.body;

  // ensure username and newpassword are valid
  if (!username || !newpassword) {
    return res.status(400).send('Invalid parameters');
  }

  // update user password in PostgreSQL
  try {
    await pool.query('UPDATE users SET password = $1 WHERE username = $2', [newpassword, username]);
    return res.status(200).send('Password updated');
  } catch (err) {
    console.error(err);
    return res.status(500).send('Error updating password');
  }
});

// handle GET requests to the /api/retrieve route
app.get('/api/retrieve', async (req, res) => {
  const { username } = req.query;

  // ensure username is valid
  if (!username) {
    return res.status(400).send('Invalid parameters');
  }

  // retrieve user from PostgreSQL
  try {
    const result = await pool.query('SELECT * FROM users WHERE username = $1', [username]);

    if (result.rows.length > 0) {
      return res.status(200).json(result.rows[0]);
    } else {
      return res.status(404).send('User not found');
    }
  } catch (err) {
    console.error(err);
    return res.status(500).send('Error retrieving user');
  }
});

// handle DELETE requests to the /api/remove route
app.delete('/api/remove', async (req, res) => {
  const { username } = req.body;

  // ensure username is valid
  if (!username) {
    return res.status(400).send('Invalid parameters');
  }

  // remove user from PostgreSQL
  try {
    await pool.query('DELETE FROM users WHERE username = $1', [username]);
    return res.status(200).send('User removed');
  } catch (err) {
    console.error(err);
    return res.status(500).send('Error removing user');
  }
});
