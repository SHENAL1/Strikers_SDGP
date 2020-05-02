/** 
 * @fileOverview Define the route for user
 * @description This contains the routes for user registration, login and authentication operation 
 * */

const express = require('express'); //Globle express route
const router = express.Router();//import express route
const cheakAuthentication = require('../middleware/authentication');
const userController = require('../controllers/user');

//create a user account
router.post("/signup", userController.userSignUp);

//to log to the web app
router.post('/login', userController.userLogin);

//delete the user account
router.delete('/:userId', cheakAuthentication,userController.deleteUserAcc)

module.exports = router;