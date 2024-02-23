{-# LANGUAGE OverloadedStrings #-}

import Web.Scotty
import Database.Persist.Postgresql
import Control.Monad.IO.Class (liftIO)
import Data.Text.Lazy (Text)
import Network.HTTP.Types (status200, status404)

-- Initiate HTTP server on a specified port
main :: IO ()
main = scotty 8080 $ do
  -- Establish a connection to the PostgreSQL database
  pool <- liftIO $ createPostgresqlPool "postgres://admin:pass@localhost/test?sslmode=disable" 10

  -- Create a new user and submit it to the database
  post "/api/create" $ do
    username <- param "username"
    password <- param "password"
    -- Ensure username and password are valid
    -- Insert new user record into PostgreSQL
    -- return 200 OK if created or error if not
    result <- liftIO $ runSqlPool (insert (User username password)) pool
    json result

  -- Update an existing user's password based on the username
  put "/api/password_change" $ do
    username <- param "username"
    newpassword <- param "newpassword"
    -- Update password
    result <- liftIO $ runSqlPool (updateWhere [UserName ==. username] [UserPassword =. newpassword]) pool
    json result

  -- return 200 OK if user found, and 404 if it isn't
  get "/api/retrieve" $ do
    username <- param "username"
    user <- liftIO $ runSqlPool (getBy (UniqueUsername username)) pool
    case user of
      Just _ -> status status200
      Nothing -> status status404

  -- Remove a user record from the database based on the username
  delete "/api/remove" $ do
    username <- param "username"
    result <- liftIO $ runSqlPool (deleteBy (UniqueUsername username)) pool
    json result
