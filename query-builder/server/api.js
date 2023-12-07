// import { Configuration, OpenAIApi } from "openai";
// certain changes made as per new update of open ai from v3 to v4

import OpenAI from 'openai';


import dotenv from "dotenv";
dotenv.config();

const openaiApiKey = process.env.OPENAI_API;

if (!openaiApiKey) {
  console.error('OPENAI_API is not set.');
  process.exit(1);
}

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API // This is also the default, can be omitted
});
// const configuration = new Configuration({
//   apiKey: process.env.OPENAI_API,
// });
// const openai = new OpenAIApi(configuration);

export default openai;

// the query in the form will first get submitted in our own api then it'll go to the open ai api