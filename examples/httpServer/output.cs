using System;
using System.Net;
using System.IO;
using Npgsql;

namespace HttpServer
{
    class Program
    {
        static void Main(string[] args)
        {
            // Start HTTP server on a specified port
            HttpListener listener = new HttpListener();
            listener.Prefixes.Add("http://localhost:8080/");
            listener.Start();

            // Establish a connection to the PostgreSQL database
            string connString = "Host=localhost;Username=admin;Password=pass;Database=test";
            var conn = new NpgsqlConnection(connString);
            conn.Open();

            Console.WriteLine("Listening...");

            while (true)
            {
                // Handle incoming requests
                HttpListenerContext context = listener.GetContext();
                HttpListenerRequest request = context.Request;
                HttpListenerResponse response = context.Response;

                // Handle different routes
                if (request.HttpMethod == "POST" && request.Url.AbsolutePath == "/api/create")
                {
                    // Ensure username and password are valid
                    // Insert new user record into PostgreSQL
                    // return 200 OK if created or error if not
                }
                else if (request.HttpMethod == "PUT" && request.Url.AbsolutePath == "/api/password_change")
                {
                    // Update an existing user's password based on the username
                }
                else if (request.HttpMethod == "GET" && request.Url.AbsolutePath == "/api/retrieve")
                {
                    // return 200 OK if user found, and 404 if it isn't
                }
                else if (request.HttpMethod == "DELETE" && request.Url.AbsolutePath == "/api/remove")
                {
                    // Remove a user record from the database based on the username
                }

                // Send response
                string responseString = "<HTML><BODY> Hello world!</BODY></HTML>";
                byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseString);
                response.ContentLength64 = buffer.Length;
                Stream output = response.OutputStream;
                output.Write(buffer, 0, buffer.Length);
                output.Close();
            }
        }
    }
}
