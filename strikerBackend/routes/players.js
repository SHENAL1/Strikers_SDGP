/** 
 * @fileOverview Define the route for player
 * @description This contains the routes for player details create,get,delete and update operation 
 * */

const express = require('express'); //Globle express lib
const router = express.Router(); //import express router
const multer = require('multer'); //multer for uploading an image

const cheakAuthentication = require('../middleware/authentication');
const playerController = require('../controllers/players');

const storage = multer.diskStorage({
    destination: function(req, file, cb){
        cb(null, './uploads/');
    },
    filename: function(req, file, cb){
        cb(null, new Date().toISOString() + file.originalname);
    }
});

const fileFilter = (req, file, cb) => {
    //Reject a file when it is not right
    if (file.mimetype === 'image/jpeg' || file.mimetype === 'image/png'){
        cb(null, true);
    }else{
        cb(null, false);
    }
};

//Get the size and validate it
const upload = multer({storage: storage, limits: {
    fileSize:1024 * 1024 * 5
},
    fileFilter: fileFilter
});

//get player details
router.get('/', playerController.getAllPlayersDetials);

//Create player details
router.post('/',cheakAuthentication,upload.single('Photo'), playerController.addNewPlayerDetails);

//get selected player details
router.get('/:playerId', playerController.getSelectedPlayerDetails);

//get selected player by firstName
router.get('/:Short_name', playerController.getPlayersDetialsByName);

//update selected player details
router.put('/:playerId', cheakAuthentication,playerController.editPlayerDetails);


//delete selected player details
router.delete('/:playerId', cheakAuthentication,playerController.deletePlayerDetails);


module.exports = router;