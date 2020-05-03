const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const newUser = require('../models/user');

exports.userSignUp = (req, res, next) => {
    newUser.find({ userName:req.body.userName})
        .exec()
        .then(user => {
            if (user.length >= 1) {
                return res.status(409).json({
                    message: "This user name is exist"
                });
            }else{
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
            }
        })  
}

exports.userLogin = (req, res, next) => {
    newUser.find({ userName:req.body.userName })
    .exec()
    .then(user => {
        if (user.length < 1){
            return res.status(401).json({
                message: 'Authentication failed, Incorrect user name, please enter the valid user name.'
            });
        }
        bcrypt.compare(req.body.password, user[0].password, (err, result) => {
            if (err){
                return res.status(401).json({
                    message: 'Authentication failed, Please try again later.'
                });
            }
            if (result){
                const token = jwt.sign(
                {
                    userName:user[0].userName,
                    userId: user[0]._id
                }, 'secret',
                {
                    expiresIn:"1h"
                })
                return res.status(200).json({
                    auth:true,
                    message: 'Authentication successful',
                    token: token
                });
            }
            res.status(401).json({
                message: 'Authentication failed, Please enter the correct password.'
            });
        });
    })
    .catch(err => {
        console.log(err);
        res.status(500).json({
            error: err
        });
    });
}

exports.deleteUserAcc = (req, res, next) => {
    newUser.find({ _id: req.params.userId})
    .exec()
    .then(user => {
        if (user.length >= 1) {
                newUser.remove({_id: req.params.userId})
                .exec()
                .then(result => {
                res.status(200).json({
                    message:'The selected user is deleted'
                });
            })
            .catch(err => {
                console.log(err);
                res.status(500).json({
                    error: err
                });
            });
        }else{
            return res.status(409).json({
                message: 'There are no selected user in the database'
             });
        }
    });
 }