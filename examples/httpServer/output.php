<?php

// Start HTTP Server
$server = new swoole_http_server("127.0.0.1", 8080);

// Establish a connection to the PostgreSQL database
$db = new PDO('pgsql:host=localhost;dbname=test', 'admin', 'pass');

$server->on('request', function ($request, $response) use ($db) {
    // Validate request
    if (empty($request->get) || empty($request->post)) {
        $response->status(400);
        $response->end('Invalid request');
        return;
    }

    // Handle routes
    switch ($request->server['request_uri']) {
        case '/api/create':
            // Ensure username and password are valid
            $username = $request->post['username'];
            $password = $request->post['password'];

            if (empty($username) || empty($password)) {
                $response->status(400);
                $response->end('Invalid parameters');
                return;
            }

            // Insert new user record into PostgreSQL
            $stmt = $db->prepare('INSERT INTO users (username, password) VALUES (?, ?)');
            $stmt->execute([$username, $password]);

            // Return 200 OK if created or error if not
            $response->status(200);
            $response->end('User created');
            break;
        case '/api/password_change':
            // Update an existing user's password based on the username
            $username = $request->post['username'];
            $newpassword = $request->post['newpassword'];

            $stmt = $db->prepare('UPDATE users SET password = ? WHERE username = ?');
            $stmt->execute([$newpassword, $username]);

            $response->status(200);
            $response->end('Password updated');
            break;
        case '/api/retrieve':
            // Return 200 OK if user found, and 404 if it isn't
            $username = $request->get['username'];

            $stmt = $db->prepare('SELECT * FROM users WHERE username = ?');
            $stmt->execute([$username]);

            if ($stmt->rowCount() > 0) {
                $response->status(200);
                $response->end('User found');
            } else {
                $response->status(404);
                $response->end('User not found');
            }
            break;
        case '/api/remove':
            // Remove a user record from the database based on the username
            $username = $request->get['username'];

            $stmt = $db->prepare('DELETE FROM users WHERE username = ?');
            $stmt->execute([$username]);

            $response->status(200);
            $response->end('User removed');
            break;
    }
});

$server->start();

?>
