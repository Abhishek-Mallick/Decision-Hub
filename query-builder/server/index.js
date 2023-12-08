import express from "express";
import cors from 'cors';
// const cors = require("cors");
// const express = require("express");
import generate from './generate.js'
// const generate = require("./generate.js");
// cors is a middleware for express
const app = express()

// we need to specify that we are sending as a json type
app.use(express.json())
app.use(cors());
/*
for production usage
app.use(cors())({
    origin: whitelist of IP where we have the frontend
})
*/

const port = process.env.PORT || 3005;

app.get("/", (req, res) => {
    res.send("Server API configured properly")
})

app.post("/generate", async (req,res) => {
    const queryDescription = req.body.queryDescription
    // console.log("Recieved: ", queryDescription)
    // res.json({response: `you sent this: ${queryDescription}`})
    
    try{
        const SQLQuery = await generate(queryDescription)
        res.json({response: SQLQuery})
        return;
    } catch(error) {
        console.log("Error: ", error)
        res.status(404).send("Internal Server Error while handling API call back")
        return;
    }

})

app.listen(port, () => {
    console.log(`Server is listening on port ${port}`)
})