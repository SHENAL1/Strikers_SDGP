const express = require('express');
const router = express.Router();

const cheakAuthentication = require('../middleware/authentication');
const userController = require('../controllers/user');

router.post("/signup", userController.userSignUp);

router.post('/login', userController.userLogin);

router.delete(cheakAuthentication,'/:userId', userController.deleteUserAcc)

module.exports = router;