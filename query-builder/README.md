### To run client
```
cd client
npm install
npm run dev
```
### Setting up server
Specify PORT config in `.env` file to run in server default set to `3005`
Get one OpenAI API key from [here](https://platform.openai.com/api-keys)

.`.env` contents ->
```
OPENAI_API = sk-ABCD
PORT = 5002
```
run:
```
cd server
npm install
node index.js / npm start
```


