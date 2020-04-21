const express = require('express');
const app = express();
const morgan = require('morgan');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const playerRoutes = require('./routes/players');
const userRoutes = require('./routes/user');

const MONGODB_URI = 'mongodb+srv://admin:admin@striker-spfii.mongodb.net/PlayerDetails?retryWrites=true&w=majority';
mongoose.connect(MONGODB_URI, {
    useNewUrlParser:true,
    useUnifiedTopology: true
});

mongoose.connection.on('connection',() => {
    console.log('Mongoose is connected');
});

app.use(morgan('dev'));
app.use('/uploads',express.static('uploads'));
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Contend-Type, Accept, Authorization"
    );
    if (req.method === 'OPTIONS') {
        res.header('Access-Control-Allow-Methods', 'PUT', 'POST' , 'PUT' , 'DELETE' , 'GET');
        return res.status(200).json({});
    }
    next();
});



app.use("/players", playerRoutes);
app.use("/user", userRoutes);

app.use((req, res, next) => {
    const error = new Error('Not Found');
    error.status = 404; 
    next(error);
})

app.use((error, req, res, next) => {
    res.status(err.status || 500);
    res.json({
        error: {
            message: error.message
        }
    })
})

module.exports = app;