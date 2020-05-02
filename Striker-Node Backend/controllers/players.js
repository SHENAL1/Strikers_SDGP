const Player = require('../models/player');
const mongoose = require('mongoose');

//control mettod for get all player details
exports.getAllPlayersDetials = (req, res, next) => {
    Player.find()
        .select('_id Photo Short_name Long_name Age Height Weight Nationality Club Overall Potential Value Wage Preferred_Foot International_Reputation Weak_Foot Skill_Moves Position Jersey_Number Contract_Valid_Until Crossing Finishing Heading_Accuracy Short_Passing Volleys Dribbling Curve FK_Accuracy FK_Accuracy Long_Passing Ball_Control Acceleration Sprint_Speed Agility Reactions Balance Shot_Power Jumping Stamina Strength Long_Shots Aggression Interceptions Positioning Vision Penalties Composure Marking Standing_Tackle Sliding_Tackle GK_Diving GK_Handling GK_Kicking GK_Positioning GKReflexes')
        .exec()
        .then(doc => {
            if (doc) {
                res.status(200).json(doc);
            } else {
                res.status(404).json({message: 'No valid entry found in database'});
            }
        })
        .catch(err => {
            console.log(err);
                res.status(500).send({
                 message: 'Can\'t get player details, Please try again later' 
            });
        });
}

//control mettod for get all player details
exports.getPlayersDetialsByName = async (req, res, next) => {
    let query = Player.find();
    if(req.query.Short_name != null && req.query.Short_name !=''){
        query = query.regex('Short_name', new RegExp(req.query.Short_name,'i'));
    }
    try{
        const name = await query
        .exec()
            res.render('players/index',{
                name: name,
                searchOption: req.query
            })
    }catch{
        res.redirect('/');
    }
}

//control method for add player details
exports.addNewPlayerDetails = (req, res, next) => {
    const player = new Player({
        _id:new mongoose.Types.ObjectId(),
        Photo:req.body.Photo,
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
                            url:'http://localhost:4000/players/' + result._id
                    }
                }
        });
    })
    .catch(err => {
        console.log(err);
            res.status(501).json({
                message: 'Can\'t create a new  player details, Please try again later' 
        });
    });
}

//control metod for get selected player details
exports.getSelectedPlayerDetails = (req, res, next) => {
    const id = req.params.playerId;
    Player.findById(id)
        .select('_id Photo Short_name Long_name Age Height Weight Nationality Club Overall Potential Value Wage Preferred_Foot International_Reputation Weak_Foot Skill_Moves Position Jersey_Number Contract_Valid_Until Crossing Finishing Heading_Accuracy Short_Passing Volleys Dribbling Curve FK_Accuracy FK_Accuracy Long_Passing Ball_Control Acceleration Sprint_Speed Agility Reactions Balance Shot_Power Jumping Stamina Strength Long_Shots Aggression Interceptions Positioning Vision Penalties Composure Marking Standing_Tackle Sliding_Tackle GK_Diving GK_Handling GK_Kicking GK_Positioning GKReflexes')
        .exec()
        .then(doc => {
            console.log("From database", doc);
            if (doc) {
                res.status(200).json(doc);
            } else {
                res.status(404).json({message: 'No valid entry found for provided ID'});
            }
        })
        .catch(err => {
            console.log(err);
                res.status(500).send({
                 message: 'Can\'t get player selected details, Please try again later' 
            });
        });
}

//control mettod for edit selected player details
exports.editPlayerDetails = (req, res, next) => {
    const id = req.params.playerId;
    const player = new Player({
        Photo:req.body.Photo,
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

        const updatePlayer =  Player.findOneAndUpdate({_id:id}, player, {upsert:true, new: true, useFindAndModify:false})
        .exec()
        .then( result => {
            console.log(result);
            res.status(200).send({
            message: 'You are successfully edit player details',
            updated: updatePlayer,
            request: {

                type: 'GET',
                url:'http://localhost:4200/players/'+ id 
            }
        });
    })
    .catch(err => {
        console.log(err);
        res.status(501).send({
            message: 'Player details could not be updated, Please try again later' 
        });
    });
}

//control method for  delete slected player details
exports.deletePlayerDetails = (req, res, next) => {
    const id = req.params.playerId;
    Player.find({ _id: id})
    .exec()
    .then(player => { 
        if (player.length >= 1) {
                Player.remove({_id: id})
                .exec()
                .then( result => {
                    res.status(200).json({
                        message:'You are successfully deleted player details, You can add a player in this url',
                        request: {
                            type: 'POST',
                            url:'http://localhost:4000/players/'
                        }
                });
            })
            .catch(err => {
                    console.log(err);
                    res.status(500).json({
                        message: 'Player details could not be delete, Please try again later'
                    });
            });
        }else{
            return res.status(409).json({
                message: 'There are no selected player in the database'
             });
        }
    });
    
}

        
        