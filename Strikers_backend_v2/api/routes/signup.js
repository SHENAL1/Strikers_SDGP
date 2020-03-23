const express = require('express');
const router = express.Router();

//handle incoming GET request to /orders
router.get('/',(req, res, next ) => {
    res.status(200).json({
        message: 'Details were fetched'
    });
});

router.post('/',(req, res, next ) => {
    const order ={
        playerId: req.body.playerId,
        playerName: req.body.playerName
    }

    //the satus code for evrything is ok
    res.status(201).json({
        message: 'Player was created',
        order: order
    });
});

router.get('/:orderedId',(req, res, next ) => {
    res.status(200).json({
        message: 'Player details',
        orderedId: req.params.orderId
    });
});

router.delete('/:orderedId',(req, res, next ) => {
    res.status(200).json({
        message: 'Player delete',
        orderedId: req.params.orderId
    });
});

module.exports = router;