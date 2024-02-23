require 'sinatra'
require 'pg'

# Initiate HTTP server on a specified port
set :port, 8080

# Establish a connection to the PostgreSQL database
$db = PG.connect("postgres://admin:pass@localhost/test?sslmode=disable")

# Handle errors and output the logs
set :show_exceptions, :after_handler

error do
  'Sorry there was a nasty error - ' + env['sinatra.error'].message
end

# Create a new user and submit it to the database
post '/api/create' do
  username = params[:username]
  password = params[:password]

  # Ensure username and password are valid
  halt 400, 'Invalid parameters' if username.nil? || password.nil?

  # Insert new user record into PostgreSQL
  $db.exec_params("INSERT INTO users (username, password) VALUES ($1, $2)", [username, password])

  # Return 200 OK if created or error if not
  status 200
end

# Update an existing user's password based on the username
put '/api/password_change' do
  username = params[:username]
  newpassword = params[:newpassword]

  halt 400, 'Invalid parameters' if username.nil? || newpassword.nil?

  $db.exec_params("UPDATE users SET password = $1 WHERE username = $2", [newpassword, username])

  status 200
end

# Return 200 OK if user found, and 404 if it isn't
get '/api/retrieve' do
  username = params[:username]

  halt 400, 'Invalid parameters' if username.nil?

  res = $db.exec_params("SELECT * FROM users WHERE username = $1", [username])

  halt 404, 'User not found' if res.ntuples.zero?

  status 200
end

# Remove a user record from the database based on the username
delete '/api/remove' do
  username = params[:username]

  halt 400, 'Invalid parameters' if username.nil?

  $db.exec_params("DELETE FROM users WHERE username = $1", [username])

  status 200
end
