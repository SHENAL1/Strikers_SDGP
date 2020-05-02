/** 
 * @description Globle library imports to the back-end
 * */
const express = require('express'); //setup the globle libraries
const app = express(); 
const morgan = require('morgan'); //Logger for node
const bodyParser = require('body-parser');
const mongoose = require('mongoose'); //pass date to database

const playerRoutes = require('./routes/players');   //connect player route 
const userRoutes = require('./routes/user');    //connect user route 

/*
 * 
 * Connects to Mongodb instance on Atles
 *
 */



const MONGODB_URI = 'mongodb+srv://admin:admin@striker-spfii.mongodb.net/StrikerDatabase?retryWrites=true&w=majority';
const option =  {
    useNewUrlParser:true,
    useUnifiedTopology: true,
    useCreateIndex:true,
};

/*Test the server wether connect or not*/
mongoose.connect(MONGODB_URI, option, (err) => {
    if (err){
        console.error("Connection could not be create,Please recheak",
        err
        );
    }else{
        console.log("Connection to db ready");
    }
});

//Test the mongodb connection
mongoose.connection.on('connected',() => {
    console.log('Mongoose is connected');
});

//The connection throws an error
mongoose.connection.on("error",function(err){
    console.log('Mongoose default connection error: ' + err);
});

//connection disconnected
mongoose.connection.on('disconnected',function(){
    console.log('Mongoose default connection is disconnected');
});

//Close the mongoose connection
process.on("SIGINT", function(){
    mongoose.connection.close(function(){
        console.log("Mongoose default connection disconnected through web application"
        );
        process.exit(0)
    });

})

app.use(morgan('dev')); //Used Morgan
//app.use('/uploads',express.static('uploads'));
app.use(bodyParser.urlencoded({extended: false}));  //this for encorded Url's supporting rech data
app.use(bodyParser.json());     //body paser for json data 

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