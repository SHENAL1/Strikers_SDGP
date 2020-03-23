const express = require('express');
const router = express.Router();

router.get('/',(req, res, next )=>{
    res.status(200).json({
        message: 'Handling GET reqests to /search'
    });
});

router.post('/', (req, res, next ) => {
    const product ={
        name: req.body.name,
        age: req.body.price
    };

    res.status(201).json({
        message: 'Handling GET reqests to /search',
        createdProduct: product
    });
});

router.get('/:playerId',(req, res, next ) => {
    const id = req.params.playerId;
    if(id === 'special'){
        res.status(200).json({
            message:'You discovered the special ID',
            id: id
        });
    }else{
        res.status(200).json({
            message: 'You passed an ID'
        });
    }
});

//This is to update a player
router.patch('/:playerId',(req, res, next ) => {
   
        res.status(200).json({
            message: 'Update player '
        });
           
});

//This is to delete player
router.delete('/:playerId',(req, res, next ) => {
   
    res.status(200).json({
        message: 'Delete player! '
    });
       
});

module.exports = router;