const express = require('express');
const app = express();
const morgan = require('morgan');
const bodyParser = require('body-parser')

const searchRoutes = require('./api/routes/search');

const signupRoutes = require('./api/routes/signup');

app.use(morgan('dev'));

//This will help to read url encoded data
app.use(bodyParser.urlencoded({extended: false}));

//This will help to read json data
app.use(bodyParser.json());

//Routes which should hadle request
app.use('/search', searchRoutes);//pro
app.use('/signup', signupRoutes);//ord

app.use((req, res, next)=>{
    const error = new Error('Not Found');
    error.status = 404;
    next(error);
});

app.use((error, req, res, next)=>{
    res.status(error.status || 500);
   res.json({
       error:{
           message:error.message
       }
   });
});



module.exports = app;   