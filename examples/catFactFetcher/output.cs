using System;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;

public class Program
{
    private static readonly HttpClient client = new HttpClient();

    public static async Task Main(string[] args)
    {
        try
        {
            // Send GET request
            Console.WriteLine("Sending GET request...");
            var response = await client.GetAsync("https://meowfacts.herokuapp.com/?count=1");

            // Make sure the http response is 200
            if (response.IsSuccessStatusCode)
            {
                Console.WriteLine("Response received...");

                // Decode JSON response
                Console.WriteLine("Decoding JSON response...");
                var jsonString = await response.Content.ReadAsStringAsync();
                var jsonObject = JObject.Parse(jsonString);

                // Read Fact
                Console.WriteLine("Reading Fact...");
                var fact = jsonObject["data"][0].ToString();

                // Return Fact
                Console.WriteLine("Returning Fact...");
                Console.WriteLine(fact);
            }
            else
            {
                Console.WriteLine("HTTP Response is not 200. Exiting program...");
            }
        }
        catch (Exception e)
        {
            // Stop program if any error happened
            Console.WriteLine("An error occurred: " + e.Message);
        }
    }
}
