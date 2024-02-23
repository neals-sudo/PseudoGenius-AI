// Importing the required 'https' module
const https = require('https');

function getRandomFact() {
  // Sending GET request to the API
  https.get('https://meowfacts.herokuapp.com/?count=1', (res) => {
    let data = '';

    // A chunk of data has been received.
    res.on('data', (chunk) => {
      data += chunk;
    });

    // The whole response has been received.
    res.on('end', () => {
      if(res.statusCode === 200) { // Check if the HTTP response is 200
        try {
          // Decode JSON response
          let jsonData = JSON.parse(data);
          
          // Read Fact
          let fact = jsonData.data[0];

          // Return Fact
          return fact;
        } catch (error) {
          console.error('Error:', error); // Log the error and stop the program
        }
      } else {
        console.error('HTTP Response not 200'); // Log the error and stop the program
      }
    });

  }).on('error', (error) => {
    console.error('Error:', error); // Log the error and stop the program
  });
}
