// Use import for loading modules in an ECMAScript module
import openAiClient from './api.js';

// Since calling a remote API of OpenAI, use async to asynchronize the code
const generate = async (queryDescription) => {
    const response = await openAiClient.completions.create({
        model: 'text-davinci-003',
        prompt: `Convert the following natural language description into a SQL query: \n\n${queryDescription}`,
        temperature: 0.2,
        // Temperature defines the creativity index
        max_tokens: 100
    });
    return response.choices[0].text;
};

// Export using ESM syntax
export default generate;
