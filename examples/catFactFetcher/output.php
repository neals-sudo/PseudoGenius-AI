<?php

// Fetch a random fact about cats from an external API and return it to the user
function getRandomFact() {
    // Request a random cat fact from the API
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, "https://meowfacts.herokuapp.com/?count=1");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $output = curl_exec($ch);

    // Make sure the http response is 200 and the response is valid
    if(curl_getinfo($ch, CURLINFO_HTTP_CODE) != 200) {
        echo "Error: HTTP response code is not 200\n";
        curl_close($ch);
        return;
    }

    curl_close($ch);

    // Extract the JSON object from the API response
    $response = json_decode($output, true);

    // Access the 'data' dictionary and retrieve the first item (fact)
    if(!isset($response['data'][0])) {
        echo "Error: Cannot access 'data' dictionary or retrieve the first item\n";
        return;
    }

    $fact = $response['data'][0];

    // Return the extracted fact to the user
    return $fact;
}

// Print every step of the way of the code and stop program if any error happened
try {
    $fact = getRandomFact();
    if($fact) {
        echo "Fact: " . $fact . "\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

?>
