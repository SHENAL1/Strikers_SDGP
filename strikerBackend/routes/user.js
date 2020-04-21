const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

const newUser = require('../models/user');

router.post("/signup", (req, res, next) => {
    User.find({ userName:req.body.email})
        .exec()
        .then(user => {
            if (user) {
                return res.status(409).json({})
            }

        })
        .catch()
    bcrypt.hash(req.body.password, 10, (err, hash) => {
        if(err){
            return res.status(500).json({
                error:err
            });
        }else{
            const user = new newUser({
                _id:new mongoose.Types.ObjectId(),
                firstName:req.body.firstName,
                lastName:req.body.lastName,
                userName:req.body.userName,
                email:req.body.email,
                password:hash,
                created_Date:req.body.created_Date
            });
            user
                .save()
                .then(result => {
                    console.log(result);
                    res.status(201).json({
                        message: 'User has been Created'
                    });
                })
                .catch(err => {
                    console.log(err);
                    res.status(500).json({
                        error: err
                    });
                });
        }
    });
});

module.exports = router;