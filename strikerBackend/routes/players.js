const express = require('express');
const router = express.Router();
const multer = require('multer');

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

const upload = multer({storage: storage, limits: {
    fileSize:1024 * 1024 * 5
},
    fileFilter: fileFilter
});

router.get('/', playerController.getAllPlayersDetials);

router.post('/',cheakAuthentication,upload.single('Photo'), playerController.addNewPlayerDetails);

router.get('/:playerId', playerController.getSelectedPlayerDetails);

router.put('/:playerId', cheakAuthentication,playerController.getSelectedPlayerDetails);

router.delete('/:playerId', cheakAuthentication,playerController.deletePlayerDetails);


module.exports = router;