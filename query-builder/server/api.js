import { Configuration, OpenAIApi } from "openai";
import dotenv from "dotenv"
dotenv.config();

const openaikey = process.env.OPENAI_API_KEY;

if(!openaikey) {
    console.log("No OpenAI API key found. Please add it to your .env file.")
    process.exit(1);
}

const configuration = new Configuration({
    apiKey: openaikey
})
// openai is the new object which we will use late to send requests
const openai = new OpenAIApi(configuration);

export default openai

// the query in the form will first get submitted in our own api then it'll go to the open ai api