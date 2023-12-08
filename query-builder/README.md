## API Callback
![image](https://github.com/Abhishek-Mallick/Decision-Hub/assets/106394426/35c98b6f-8673-4878-a8fd-562b20300919)


### To run client
```
cd client
npm install
npm run dev
```
### Setting up server
Specify PORT config in `.env` file to run in server default set to `3005`
Get one OpenAI API key from [here](https://platform.openai.com/api-keys)

`.env` contents ->
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


