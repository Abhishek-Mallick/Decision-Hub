// import express from "express";
// import cors from 'cors';
const cors = require("cors");
const express = require("express");
// cors is a middleware for express
const app = express()

app.use(cors());
/*
for production usage
app.use(cors())({
    origin: whitelist of IP where we have the frontend
})
*/

const port = process.env.PORT || 3005;

app.get("/", (req, res) => {
    res.send("Hello World - server API")
})

app.listen(port, () => {
    console.log(`Server is listening on port ${port}`)
})