const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const multer = require('multer');

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

const Player = require('../models/player');

router.get('/', (req, res, next) => {
    Player.find()
        .select('_id Photo Short_name Long_name Age Height Weight Nationality Club Overall Potential Value Wage Preferred_Foot International_Reputation Weak_Foot Skill_Moves Position Jersey_Number Contract_Valid_Until Crossing Finishing Heading_Accuracy Short_Passing Volleys Dribbling Curve FK_Accuracy FK_Accuracy Long_Passing Ball_Control Acceleration Sprint_Speed Agility Reactions Balance Shot_Power Jumping Stamina Strength Long_Shots Aggression Interceptions Positioning Vision Penalties Composure Marking Standing_Tackle Sliding_Tackle GK_Diving GK_Handling GK_Kicking GK_Positioning GKReflexes')
        .exec()
        .then(docs => {
            const response = {
                count: docs.length,
                players: docs.map(doc => {
                    return {
                        _id:doc._id,
                        Photo:doc.Photo,
                        Short_name:doc.Short_name,
                        Long_name:doc.Long_name,
                        Age:doc.Age,
                        Height:doc.Height,
                        Weight:doc.Weight,
                        Nationality:doc.Nationality,
                        Club:doc.Club,
                        Overall:doc.Overall,
                        Potential:doc.Potential,
                        Value:doc.Value,
                        Wage:doc.Wage,
                        Preferred_Foot:doc.Preferred_Foot,
                        International_Reputation: doc.International_Reputation,
                        Weak_Foot:doc.Weak_Foot,
                        Skill_Moves:doc.Skill_Moves,
                        Position:doc.Position,
                        Jersey_Number:doc.Jersey_Number,
                        Contract_Valid_Until:doc.Contract_Valid_Until,
                        Crossing:doc.Crossing,
                        Finishing:doc.Finishing,
                        Heading_Accuracy:doc.Heading_Accuracy,
                        Short_Passing:doc.Short_Passing,
                        Volleys:doc.Volleys,
                        Dribbling:doc.Dribbling,
                        Curve:doc.Curve,
                        FK_Accuracy:doc.FK_Accuracy,
                        Long_Passing:doc.Long_Passing,
                        Ball_Control:doc.Ball_Control,
                        Acceleration:doc.Acceleration,
                        Sprint_Speed:doc.Sprint_Speed,
                        Agility:doc.Agility,
                        Reactions:doc.Reactions,
                        Balance:doc.Balance,
                        Shot_Power:doc.Shot_Power,
                        Jumping:doc.Jumping,
                        Stamina:doc.Stamina,
                        Strength:doc.Strength,
                        Long_Shots:doc.Long_Shots,
                        Aggression:doc.Aggression,
                        Interceptions:doc.Interceptions,
                        Positioning:doc.Positioning,
                        Vision:doc.Vision,
                        Penalties:doc.Penalties,
                        Composure:doc.Composure,
                        Marking:doc.Marking,
                        Standing_Tackle:doc.Standing_Tackle,
                        Sliding_Tackle:doc.Sliding_Tackle,
                        GK_Diving:doc.GK_Diving,
                        GK_Handling:doc.GK_Handling,
                        GK_Kicking:doc.GK_Kicking,
                        GK_Positioning:doc.GK_Positioning,
                        GKReflexes:doc.GKReflexes,
                        request: {
                            type: 'GET',
                            url:'http://localhost:3000/players/' + doc._id
                        }
                    }
                })
            }
            if (docs.length >= 0){
                res.status(200).json(response);
            } else {
                res.status(404).json({
                    message:'No enties found'
                });
            }
        })
        .catch(err => {
            console.log(err);
            res.status(500).json({
                error:err
            });
        });
});

router.post('/', upload.single('Photo'), (req, res, next) => {
    const player = new Player({
        _id:new mongoose.Types.ObjectId(),
        Photo:req.file.path,
        Short_name:req.body.Short_name,
        Long_name:req.body.Long_name,
        Age:req.body.Age,
        Height:req.body.Height,
        Weight:req.body.Weight,
        Nationality:req.body.Nationality,
        Club:req.body.Club,
        Overall:req.body.Overall,
        Potential:req.body.Potential,
        Value:req.body.Value,
        Wage:req.body.Wage,
        Preferred_Foot:req.body.Preferred_Foot,
        International_Reputation: req.body.International_Reputation,
        Weak_Foot:req.body.Weak_Foot,
        Skill_Moves:req.body.Skill_Moves,
        Position:req.body.Position,
        Jersey_Number:req.body.Jersey_Number,
        Contract_Valid_Until:req.body.Contract_Valid_Until,
        Crossing:req.body.Crossing,
        Finishing:req.body.Finishing,
        Heading_Accuracy:req.body.Heading_Accuracy,
        Short_Passing:req.body.Short_Passing,
        Volleys:req.body.Volleys,
        Dribbling:req.body.Dribbling,
        Curve:req.body.Curve,
        FK_Accuracy:req.body.FK_Accuracy,
        Long_Passing:req.body.Long_Passing,
        Ball_Control:req.body.Ball_Control,
        Acceleration:req.body.Acceleration,
        Sprint_Speed:req.body.Sprint_Speed,
        Agility:req.body.Agility,
        Reactions:req.body.Reactions,
        Balance:req.body.Balance,
        Shot_Power:req.body.Shot_Power,
        Jumping:req.body.Jumping,
        Stamina:req.body.Stamina,
        Strength:req.body.Strength,
        Long_Shots:req.body.Long_Shots,
        Aggression:req.body.Aggression,
        Interceptions:req.body.Interceptions,
        Positioning:req.body.Positioning,
        Vision:req.body.Vision,
        Penalties:req.body.Penalties,
        Composure:req.body.Composure,
        Marking:req.body.Marking,
        Standing_Tackle:req.body.Standing_Tackle,
        Sliding_Tackle:req.body.Sliding_Tackle,
        GK_Diving:req.body.GK_Diving,
        GK_Handling:req.body.GK_Handling,
        GK_Kicking:req.body.GK_Kicking,
        GK_Positioning:req.body.GK_Positioning,
        GKReflexes:req.body.GKReflexes
    });
    player
        .save()
        .then(result => {
            console.log(result);
            res.status(200).json({
                message: "Created player details successfully",
                createdPlayer: {
                    _id:result._id,
                    Photo:result.Photo,
                    Short_name:result.Short_name,
                    Long_name:result.Long_name,
                    Age:result.Age,
                    Height:result.Height,
                    Weight:result.Weight,
                    Nationality:result.Nationality,
                    Club:result.Club,
                    Overall:result.Overall,
                    Potential:result.Potential,
                    Value:result.Value,
                    Wage:result.Wage,
                    Preferred_Foot:result.Preferred_Foot,
                    International_Reputation: result.International_Reputation,
                    Weak_Foot:result.Weak_Foot,
                    Skill_Moves:result.Skill_Moves,
                    Position:result.Position,
                    Jersey_Number:result.Jersey_Number,
                    Contract_Valid_Until:result.Contract_Valid_Until,
                    Crossing:result.Crossing,
                    Finishing:result.Finishing,
                    Heading_Accuracy:result.Heading_Accuracy,
                    Short_Passing:result.Short_Passing,
                    Volleys:result.Volleys,
                    Dribbling:result.Dribbling,
                    Curve:result.Curve,
                    FK_Accuracy:result.FK_Accuracy,
                    Long_Passing:result.Long_Passing,
                    Ball_Control:result.Ball_Control,
                    Acceleration:result.Acceleration,
                    Sprint_Speed:result.Sprint_Speed,
                    Agility:result.Agility,
                    Reactions:result.Reactions,
                    Balance:result.Balance,
                    Shot_Power:result.Shot_Power,
                    Jumping:result.Jumping,
                    Stamina:result.Stamina,
                    Strength:result.Strength,
                    Long_Shots:result.Long_Shots,
                    Aggression:result.Aggression,
                    Interceptions:result.Interceptions,
                    Positioning:result.Positioning,
                    Vision:result.Vision,
                    Penalties:result.Penalties,
                    Composure:result.Composure,
                    Marking:result.Marking,
                    Standing_Tackle:result.Standing_Tackle,
                    Sliding_Tackle:result.Sliding_Tackle,
                    GK_Diving:result.GK_Diving,
                    GK_Handling:result.GK_Handling,
                    GK_Kicking:result.GK_Kicking,
                    GK_Positioning:result.GK_Positioning,
                    GKReflexes:result.GKReflexes,
                    request: {
                            type: 'GET',
                            url:'http://localhost:3000/players/' + result._id
                    }
                }

        });
    })
    .catch(err => {
        console.log(err);
        res.status(500).json({
            error: err
        });
    });
});

router.get('/:playerId', (req, res, next) => {
    const id = req.params.playerId;
    Player.findById(id)
        .select('_id Photo Short_name Long_name Age Height Weight Nationality Club Overall Potential Value Wage Preferred_Foot International_Reputation Weak_Foot Skill_Moves Position Jersey_Number Contract_Valid_Until Crossing Finishing Heading_Accuracy Short_Passing Volleys Dribbling Curve FK_Accuracy FK_Accuracy Long_Passing Ball_Control Acceleration Sprint_Speed Agility Reactions Balance Shot_Power Jumping Stamina Strength Long_Shots Aggression Interceptions Positioning Vision Penalties Composure Marking Standing_Tackle Sliding_Tackle GK_Diving GK_Handling GK_Kicking GK_Positioning GKReflexes')
        .exec()
        .then(doc => {
            console.log("From database", doc);
            if (doc) {
                res.status(200).json({
                    player: doc,
                    request: {
                        type: 'GET',
                        url:'http://localhost:3000/players/' + doc._id
                    }
                });
            } else {
                res.status(404).json({message: 'No valid entry found for provided ID'});
            }
        })
        .catch(err => {
            console.log(err);
            res.status(500).json({
                error:err
            });
        });
});

router.put('/:playerId', (req, res, next) => {
    const id = req.params.playerId;
    Player.findOneAndUpdate({_id: id},req.body,{new:true, useFindAndModify:false}, (err, result) => {
        if (err){
            res.send(err);
        }
        res.status(200).json({
            message:'Player details updated',
            request: {
                type: 'GET',
                url:'http://localhost:3000/players/' + id
            }
        });
    });
});

router.delete('/:playerId', (req, res, next) => {
    const id = req.params.playerId;
    Player.remove({_id: id})
    .exec()
    .then( result => {
        res.status(200).json({
            message:'Player Details Deleted',
            request: {
                type: 'POST',
                url:'http://localhost:3000/players/' 
            }
        })
        res.json({message: 'You are successfully deleted player details'})
    })
    .catch(err => {
        console.log(err);
        res.status(500).json({
            error:err
        });
    });
});


module.exports = router;